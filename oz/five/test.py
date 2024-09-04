import os
import json
import random
import string
import time
from sqlalchemy import create_engine, MetaData, Table, text, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import String, Integer, Float, Date, DateTime, Boolean, SmallInteger, DECIMAL, Enum, Time, TIMESTAMP
from faker import Faker

faker = Faker()

def get_config_file():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    resource_dir = os.path.join(base_dir, "..", "resources")
    return os.path.join(resource_dir, "config.json")

def load_config():
    config_file = get_config_file()
    with open(config_file, "r") as f:
        return json.load(f)
    
def get_engine(db_config):
    return create_engine(f"mysql+pymysql://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database_name']}")

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()

def get_metadata(engine):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    return metadata

# 유니크 스트링 생성
def generate_unique_string(existing_values, length=10):
    while True:
        unique_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        if unique_str not in existing_values:
            return unique_str

# 유니크 인티저 생성
def generate_unique_integer(existing_values, max_value=30000):
    unique_int = faker.random_int(min=0, max=max_value)
    while unique_int in existing_values:
        unique_int = faker.random_int(min=0, max=max_value)
    return unique_int

# 컬럼 타입에 따른 더미 데이터 생성
def generate_column_data(col_type, existing_values):
    if isinstance(col_type, Enum):
        return random.choice(col_type.enums)
    
    elif isinstance(col_type, String):
        length = col_type.length
        if length:
            if existing_values is not None:
                return generate_unique_string(existing_values, length)
            else:
                if length < 5:
                    return faker.word()[:length]
                else:
                    return faker.text(max_nb_chars=length)
        return faker.text(max_nb_chars=50)
    
    elif isinstance(col_type, (Integer, Float, SmallInteger)):
        return (generate_unique_integer(existing_values) if existing_values 
                else random.choice([0, 1]) if 'TINYINT' in str(col_type) 
                else faker.random_int(min=0, max=30000))
    
    elif isinstance(col_type, DECIMAL):
        return faker.latitude()
    
    elif isinstance(col_type, Boolean):
        return faker.boolean()
    
    elif isinstance(col_type, Date):
        return faker.date()
    
    elif isinstance(col_type, DateTime):
        return faker.date_time()
    
    elif isinstance(col_type, Time):
        return faker.time()
    
    return faker.text()

# 테이블에 맞는 더미 데이터 생성
def generate_dummy_data(table, num_rows):
    data = []
    existing_values = {col.name: set() for col in table.columns}
    unique_columns = {col.name for col in table.primary_key.columns}
    inserted_count = 0  # 데이터 삽입 카운트
    
    for index in table.indexes:
        if index.unique:
            unique_columns.update(col.name for col in index.columns)
            
    for _ in range(num_rows):
        row = {}
        for col in table.columns:
            if col.autoincrement == True:
                continue
            elif isinstance(col.type, TIMESTAMP): #autoincrement와 CURRENT_TIME 속성을 가진 컬럼들은 skip
                continue
            else:
                if col.name in unique_columns:
                # 유니크 제약 조건이 있는 컬럼에 대해 기존 값을 참조하여 유니크한 값을 생성
                    row[col.name] = generate_column_data(col.type, existing_values[col.name])
                else:
                    row[col.name] = generate_column_data(col.type, None)

            existing_values[col.name].add(row[col.name])
        data.append(row)
        
        inserted_count += 1
        
        print(f"테이블 {table.name}에 대해 {inserted_count}개의 데이터가 생성됨.")
    return data

# 데이터베이스 연결 설정 및 데이터 삽입
def insert_data(config):
    for key in list(config):
        sub_config = config[key]
        db_config = sub_config['database']
        
        engine = get_engine(db_config)
        metadata = get_metadata(engine)
        session = get_session(engine)
        
        for table_name, table_config in sub_config['tables'].items():
            table = Table(table_name, metadata, autoload_with=engine)
            if table_config.get('mode') == 'replace':
                session.execute(text(f"TRUNCATE TABLE {table_name};"))
            
            BATCH_SIZE = 5000
            dummy_data = generate_dummy_data(table, table_config['rows'])
            for i in range(0, len(dummy_data), BATCH_SIZE):
                batch = dummy_data[i:i + BATCH_SIZE] 
                session.execute(table.insert(), batch)
            
        session.commit()
        session.close()
        
# 특정 데이터베이스에 속한 schema 목록 반환
def get_schemas(engine):
    return inspect(engine).get_schema_names()

# 특정 데이터베이스의 schema에 속한 테이블 목록 반환
def get_tables(engine, schema):
    return inspect(engine).get_table_names(schema=schema)

# 특정 데이터베이스의 schema에 속한 뷰 목록 반환
def get_views(engine, schema):
    return inspect(engine).get_view_names(schema=schema)

# 컬럼 정보를 반환하는 헬퍼 함수
def _get_columns_info(inspector, table_name, schema):
    columns = inspector.get_columns(table_name, schema=schema)
    return [
        {
            "name": col['name'],
            "type": str(col['type']),
            "nullable": col['nullable'],
            "primary_key": col.get('primary_key', False),
            "comment": col.get('comment', '')
        } for col in columns
    ]
# 특정 데이터베이스의 schema에 속한 테이블 목록과 테이블 별 컬럼정보, 코멘트를 반환
def get_table_info(engine, schema):
    inspector = inspect(engine)
    tables_info = {}
    
    for table_name in inspector.get_table_names(schema=schema):
        tables_info[table_name] = {
            "columns": _get_columns_info(inspector, table_name, schema),
            "indexes": inspector.get_indexes(table_name, schema=schema)
        }
    
    return tables_info

# 특정 데이터베이스의 schema에 속한 뷰 목록과 뷰 별 컬럼정보, 코멘트를 반환
def get_view_info(engine, schema):
    inspector = inspect(engine)
    views_info = {}
    
    for view_name in inspector.get_view_names(schema=schema):
        views_info[view_name] = {
            "columns": _get_columns_info(inspector, view_name, schema)
        }
    
    return views_info

# 특정 테이블의 컬럼정보, 코멘트를 조회하는 함수
def get_column_info(engine, table_name, schema):
    inspector = inspect(engine)
    return _get_columns_info(inspector, table_name, schema)

# 특정 테이블의 DDL 스크립트 생성 함수
def get_ddl(engine, table_name, schema):
    inspector = inspect(engine)
    ddl = f"CREATE TABLE {schema}.{table_name} (\n"
    
    columns = inspector.get_columns(table_name, schema=schema)
    for col in columns:
        ddl += f"  {col['name']} {col['type']}"
        if not col['nullable']:
            ddl += " NOT NULL"
        if col.get('primary_key', False):
            ddl += " PRIMARY KEY"
        ddl += ",\n"
    
    return ddl.rstrip(",\n") + "\n);"

# TUI 관련 함수

def display_main_menu():
    print("=== 데이터베이스 관리 도구 ===")
    print("1. 데이터베이스 정보 조회")
    print("2. 더미 데이터 생성 및 삽입")
    print("3. 종료")
    return input("원하는 작업을 선택하세요 (1-3): ")

def display_menu():
    print("=== 데이터베이스 정보 조회 ===")
    print("1. 스키마 목록 조회")
    print("2. 특정 스키마의 테이블 목록 조회")
    print("3. 특정 테이블의 정보 조회")
    print("4. 특정 테이블의 DDL 스크립트 생성")
    print("5. 종료")
    return input("원하는 작업을 선택하세요 (1-5): ")

def get_valid_schema(engine):
    schemas = get_schemas(engine)
    schema = input("조회할 스키마를 입력하세요: ")
    if schema in schemas:
        return schema
    else:
        print("유효하지 않은 스키마입니다.")
        return None

def handle_database_info(engine):
    while True:
        db_choice = display_menu()
        
        if db_choice == '5':
            break
        
        if db_choice == '1':
            print("Schemas:", get_schemas(engine))

        elif db_choice in ['2', '3', '4']:
            schema = get_valid_schema(engine)
            if schema is None:
                continue
            
            if db_choice == '2':
                print(f"Tables in {schema}:", get_tables(engine, schema))

            elif db_choice == '3':
                table_name = input("조회할 테이블 이름을 입력하세요: ")
                table_info = get_table_info(engine, schema)
                if table_name in table_info:
                    print(f"Table Info in {schema} for {table_name}:", table_info[table_name])
                else:
                    print("유효하지 않은 테이블입니다.")

            elif db_choice == '4':
                table_name = input("DDL 스크립트를 생성할 테이블 이름을 입력하세요: ")
                table_info = get_table_info(engine, schema)
                if table_name in table_info:
                    ddl = get_ddl(engine, table_name, schema)
                    print(f"DDL for {table_name} in {schema}:\n{ddl}")
                else:
                    print("유효하지 않은 테이블입니다.")

            else:
                print("유효하지 않은 선택입니다.")
        
# 메인 함수
def main():
    config = load_config()
    db_key = 'oz'
    db_config = config[db_key]['database']
    engine = get_engine(db_config)

    while True:
        choice = display_main_menu()

        if choice == '1':
            handle_database_info(engine)

        elif choice == '2':
            start_time = time.perf_counter()
            insert_data(config)
            elapsed_time = time.perf_counter() - start_time
            print(f"소요 시간: {elapsed_time:.2f} 초")

        elif choice == '3':
            print("프로그램을 종료합니다.")
            break

        else:
            print("유효하지 않은 선택입니다. 다시 시도해 주세요.")

if __name__ == '__main__':
    main()