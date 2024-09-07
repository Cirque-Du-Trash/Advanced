from pymongo import MongoClient
from sqlalchemy import create_engine, inspect
from conf.config_loader import load_config 
import pymysql
import decimal
import datetime

def get_mysql_connection(source_db):
    config = load_config()
    return pymysql.connect(
        host=config[source_db]['source_database']['host'],
        user=config[source_db]['source_database']['username'],
        password=config[source_db]['source_database']['password'],
        database=config[source_db]['source_database']['database_name']
    )

def migrate_data(source_db, source_table, target_db, target_collection):
    config = load_config()
    mysql_conn = get_mysql_connection(source_db)
    
    mongo_client = MongoClient(
        host=config[source_db]['target_database']['host'],
        port=config[source_db]['target_database']['port'],
        username=config[source_db]['target_database']['username'],
        password=config[source_db]['target_database']['password']
    )
    mongo_db = mongo_client[config[source_db]['target_database']['database_name']]
    mongo_collection = mongo_db[target_collection]

    try:
        with mysql_conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {source_table}")
            rows = cursor.fetchall()
            for row in rows:
                document = dict(zip([column[0] for column in cursor.description], row))
                mongo_collection.insert_one(convert_data(document))
        print(f"마이그레이션 성공 {source_db}.{source_table} 에서 {target_db}.{target_collection}")
    except Exception as e:
        print(f"마이그레이션 중 오류가 발생했습니다: {e}")
    finally:
        mysql_conn.close()
        mongo_client.close()

def compare_schemas(source_db, source_table, target_db, target_collection):
    config = load_config()
    mysql_engine = create_engine(f"mysql+pymysql://{config[source_db]['source_database']['username']}:{config[source_db]['source_database']['password']}@{config[source_db]['source_database']['host']}:{config[source_db]['source_database']['port']}/{config[source_db]['source_database']['database_name']}")
    inspector = inspect(mysql_engine)
    mysql_columns = inspector.get_columns(source_table)

    mongo_client = MongoClient(
        host=config[source_db]['target_database']['host'],
        port=config[source_db]['target_database']['port'],
        username=config[source_db]['target_database']['username'],
        password=config[source_db]['target_database']['password']
    )
    mongo_db = mongo_client[config[source_db]['target_database']['database_name']]
    mongo_collection = mongo_db[target_collection]

    first_doc = mongo_collection.find_one()
    mongo_schema = {key: type(value).__name__ for key, value in first_doc.items()} if first_doc else {}

    comparison_result = [{
        'field': column['name'],
        'mysql_type': str(column['type']),
        'mongodb_type': mongo_schema.get(column['name'], 'Not present')
    } for column in mysql_columns]

    with open('README.md', 'a') as f:
        f.write(f"# 스키마 비교 결과\n\n")
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
    
def convert_data(data):
    if isinstance(data, dict):
        return {key: convert_data(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_data(element) for element in data]
    elif isinstance(data, decimal.Decimal):
        return float(data)
    elif isinstance(data, datetime.timedelta):
        return int(data.total_seconds())
    elif isinstance(data, datetime.date):
        return data.isoformat()
    return data