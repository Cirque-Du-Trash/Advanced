from pymongo import MongoClient
from sqlalchemy import create_engine, inspect
from conf.config_loader import load_config 
import pymysql
import decimal
import datetime

# Decimal과 Datetime은 MongoDB에서 미지원
def convert_data(data):
    if isinstance(data, dict):
        return {key: convert_data(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_data(element) for element in data]
    elif isinstance(data, decimal.Decimal):
        return float(data)
    elif isinstance(data, datetime.timedelta):
        return int(data.total_seconds())  # timedelta를 초로 변환
    elif isinstance(data, datetime.date):
        return data.isoformat()  # date를 문자열로 변환
    else:
        return data

def migrate_data(source_db, source_table, target_db, target_collection):
    config = load_config()
    
    # MySQL 연결
    mysql_conn = pymysql.connect(
        host=config[source_db]['source_database']['host'],
        user=config[source_db]['source_database']['username'],
        password=config[source_db]['source_database']['password'],
        database=config[source_db]['source_database']['database_name']
    )
    
    # MongoDB 연결
    mongo_client = MongoClient("mongodb://root:root@localhost:27017/airportdb_mongo")
    mongo_db = mongo_client[config[source_db]['target_database']['database_name']]
    mongo_collection = mongo_db[target_collection]

    try:
        with mysql_conn.cursor() as cursor:
            # MySQL에서 데이터 가져오기
            cursor.execute(f"SELECT * FROM {source_table}")
            rows = cursor.fetchall()

            # MongoDB로 데이터 삽입
            for row in rows:
                document = dict(zip([column[0] for column in cursor.description], row))
                document = convert_data(document)
                mongo_collection.insert_one(document)

        print(f"마이그레이션 성공 {source_db}.{source_table} 에서 {target_db}.{target_collection}")
        
    except Exception as e:
        print(f"마이그레이션 중 오류가 발생했습니다: {e}")
    
    finally:
        mysql_conn.close()
        mongo_client.close()

def compare_schemas(source_db, source_table, target_db, target_collection):
    config = load_config()
    
    # MySQL 연결 및 스키마 정보 가져오기
    mysql_engine = create_engine(f"mysql+pymysql://{config[source_db]['source_database']['username']}:{config[source_db]['source_database']['password']}@{config[source_db]['source_database']['host']}:{config[source_db]['source_database']['port']}/{config[source_db]['source_database']['database_name']}")
    inspector = inspect(mysql_engine)
    mysql_columns = inspector.get_columns(source_table)
    
    # MongoDB 연결 및 스키마 정보 가져오기
    mongo_client = MongoClient("mongodb://root:root@localhost:27017/airportdb_mongo")
    mongo_db = mongo_client[config[source_db]['target_database']['database_name']]
    mongo_collection = mongo_db[target_collection]
    
    # MongoDB 스키마 추론 (첫 번째 문서 기반)
    mongo_schema = {}
    first_doc = mongo_collection.find_one()
    if first_doc:
        for key, value in first_doc.items():
            mongo_schema[key] = type(value).__name__
    
    # 스키마 비교
    comparison_result = []
    for column in mysql_columns:
        mysql_type = str(column['type'])
        mongo_type = mongo_schema.get(column['name'], 'Not present')
        comparison_result.append({
            'field': column['name'],
            'mysql_type': mysql_type,
            'mongodb_type': mongo_type
        })
    
    # 결과를 README.md 파일에 작성
    with open('README.md', 'a') as f:  # 'w' 모드를 사용하여 파일을 새로 작성
        f.write(f"# 스키마 비교 결과\n\n")  # 파일의 처음에 제목 추가
        f.write(f"## 스키마 비교: {source_db}.{source_table} vs {target_db}.{target_collection}\n\n")
        f.write("| 필드 | MySQL 타입 | MongoDB 타입 |\n")
        f.write("|-------|------------|---------------|\n")
        for item in comparison_result:
            f.write(f"| {item['field']} | {item['mysql_type']} | {item['mongodb_type']} |\n")

    print(f"스키마 {source_db}.{source_table}와 {target_db}.{target_collection}의 비교 결과가 README.md에 추가되었습니다.")

def compare_all_schemas():
    config = load_config()
    for db_name, db_config in config.items():
        for table_name, table_config in db_config['tables'].items():
            target_collection = table_config['target_collection']
            compare_schemas(db_name, table_name, f"{db_name}_mongo", target_collection)

if __name__ == "__main__":
    compare_all_schemas()