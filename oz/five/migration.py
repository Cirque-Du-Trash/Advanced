from pymongo import MongoClient
from sqlalchemy import create_engine, inspect
from conf.config_loader import load_config 
import pymysql

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
                mongo_collection.insert_one(document)

        print(f"Successfully migrated data from {source_db}.{source_table} to {target_db}.{target_collection}")
    
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
    with open('README.md', 'a') as f:
        f.write(f"\n\n## Schema Comparison: {source_db}.{source_table} vs {target_db}.{target_collection}\n\n")
        f.write("| Field | MySQL Type | MongoDB Type |\n")
        f.write("|-------|------------|---------------|\n")
        for item in comparison_result:
            f.write(f"| {item['field']} | {item['mysql_type']} | {item['mongodb_type']} |\n")
    
    print(f"Schema comparison for {source_db}.{source_table} vs {target_db}.{target_collection} has been added to README.md")

def compare_all_schemas():
    config = load_config()
    for db_name, db_config in config.items():
        for table_name, table_config in db_config['tables'].items():
            target_collection = table_config['target_collection']
            compare_schemas(db_name, table_name, f"{db_name}_mongo", target_collection)

if __name__ == "__main__":
    compare_all_schemas()