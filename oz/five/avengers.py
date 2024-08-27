import os
import json
import random
import string
import time
from sqlalchemy import create_engine, MetaData, Table, text
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

# 고정 길이 문자열 생성
def generate_fixed_length_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# 유니크 문자열 생성
def generate_unique_string(existing_values, length=10):
    while True:
        unique_str = generate_fixed_length_string(length)
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
            
            dummy_data = generate_dummy_data(table, table_config['rows'])
            for i in range(0, len(dummy_data), 5000):
                batch = dummy_data[i:i + 5000] 
                session.execute(table.insert(), batch)
            
        session.commit()
        session.close()
        
# 메인 함수
def main():  
    config = load_config()
    start_time = time.time()
    insert_data(config)
    end_time = time.time()
    print(f"소요 시간: {end_time - start_time:.2f} 초")
        
if __name__ == '__main__':
    main()