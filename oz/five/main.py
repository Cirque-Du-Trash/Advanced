import json
import argparse
import yaml
import random
import string
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import String, Integer, Float, Date, DateTime, Boolean, SmallInteger
from faker import Faker

# 설정 파일 로드
def load_config(file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            return json.load(file)
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    else:
        raise ValueError("Unsupported file type. Use JSON or YAML.")

 # 고정 길이 문자열 생성
def generate_fixed_length_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

 # 유니크 문자열 생성 함수
def generate_unique_string(existing_values, length=10):
    while True:
        unique_str = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if unique_str not in existing_values:
            return unique_str
    

 # 유니크 인티저 생성 함수
def generate_unique_integer(existing_values, min_value=0, max_value=10000):
    while True:
        unique_int = random.randint(min_value, max_value)
        if unique_int not in existing_values:
            return unique_int

# 컬럼 타입에 따른 더미 데이터 생성기
def generate_column_data(col_type, existing_values):
    faker = Faker()
    
    if isinstance(col_type, String):
        length = col_type.length
        if length and existing_values is not None:
            return generate_unique_string(existing_values, length)
        return generate_fixed_length_string(length) if length else faker.text(max_nb_chars=255)
    
    elif isinstance(col_type, Integer) or isinstance(col_type, Float) or isinstance(col_type, SmallInteger):
        if existing_values is not None:
            return generate_unique_integer(existing_values)
        return faker.random_int(min=0, max=10000)
    
    elif isinstance(col_type, Boolean):
        return faker.boolean()
    
    elif isinstance(col_type, Date):
        return faker.date()
    
    elif isinstance(col_type, DateTime):
        return faker.date_time()
    
    else:
        return None  # 또는 기본값으로 채울 수 있음


# 테이블에 맞는 더미 데이터 생성기
def generate_dummy_data(table, num_rows):
    data = []
    existing_values = {col.name: set() for col in table.columns}
    
    for _ in range(num_rows):
        row = {}
        for col in table.columns:
            # 유니크 제약 조건이 있는 컬럼의 경우, 기존 값을 참조하여 유니크한 값을 생성
            print(col.constraints)
            print(existing_values)
            if any(constraint.name == 'uq_' + col.name for constraint in table.constraints):
                row[col.name] = generate_column_data(col.type, existing_values[col.name])
            else:
                row[col.name] = generate_column_data(col.type, None)
            
                
            existing_values[col.name].add(row[col.name])
        data.append(row)
    return data


# 데이터베이스 연결 설정 및 데이터 삽입
def insert_data(config):
    db_config = config['database']
    engine = create_engine(f"mysql+pymysql://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database_name']}")
    metadata = MetaData()
    metadata.reflect(bind=engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    for table_name, table_config in config['tables'].items():
        table = Table(table_name, metadata, autoload_with=engine)
        num_rows = table_config['rows']
        mode = table_config['mode']
        
        if mode == 'replace':
            session.execute(table.delete())
        
        dummy_data = generate_dummy_data(table, num_rows)
        session.execute(table.insert(), dummy_data)
    
    session.commit()
    session.close()

# 메인 함수
def main():
    parser = argparse.ArgumentParser(description='Generate and insert dummy data into MySQL tables.')
    parser.add_argument('config', type=str, help='Path to the configuration file (JSON or YAML).')
    args = parser.parse_args()
    
    config = load_config(args.config)
    insert_data(config)

if __name__ == '__main__':
    main()