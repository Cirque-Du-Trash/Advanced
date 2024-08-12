import json
import argparse
import random
import time
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import String, Integer, Float, Date, DateTime, Boolean, SmallInteger, DECIMAL, Enum, Time
from faker import Faker
faker = Faker()

# 설정 파일 로드
def load_config(file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        raise ValueError("Unsupported file type. Use JSON or YAML.")

# Unicode character ranges for various scripts
def get_unicode_characters():
    unicode_blocks = {
        'Chinese': (0x4E00, 0x9FFF)
    }

    characters = []
    for start_end in unicode_blocks.values():
        start, end = start_end  # Unpack the tuple
        characters.extend(chr(code_point) for code_point in range(start, end + 1))
    
    return characters

def generate_multilingual_text(length=100):
    all_chars = get_unicode_characters()
    return ''.join(random.choice(all_chars) for _ in range(length))

 # 유니크 문자열 생성 함수
def generate_unique_string(existing_values, length=10):
    existing_values_lower = {v.lower() for v in existing_values}
    unique_str = generate_multilingual_text(length)
    while unique_str.lower() in existing_values_lower:
        unique_str = generate_multilingual_text(length)
    return unique_str

 # 유니크 인티저 생성 함수
def generate_unique_integer(existing_values, max_value=30000):
    while True:
        unique_int = faker.random_int(min=0, max=max_value)
        if unique_int not in existing_values:
            return unique_int

# 컬럼 타입에 따른 더미 데이터 생성 함수
def generate_column_data(col_type, existing_values):
    if isinstance(col_type, Enum):
        enum_values = col_type.enums
        return random.choice(enum_values)
    
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
        return faker.text(max_nb_chars=100)

    elif isinstance(col_type, Integer) or isinstance(col_type, Float) or isinstance(col_type, SmallInteger):
        if existing_values is not None:
            return generate_unique_integer(existing_values)
        if 'TINYINT' in str(col_type):
            return random.choice([0, 1])
        return faker.random_int(min=0, max=30000)
    
    elif isinstance(col_type, DECIMAL):
        return faker.latitude() # Faker 위도 생성 메소드

    elif isinstance(col_type, Boolean):
        return faker.boolean()
    
    elif isinstance(col_type, Date):
        return faker.date()
    
    elif isinstance(col_type, DateTime):
        return faker.date_time()
    
    elif isinstance(col_type, Time):
        return faker.time()
    
    else:
        return faker.text()


# 테이블에 맞는 더미 데이터 생성 함수
def generate_dummy_data(table, num_rows):
    data = []
    existing_values = {col.name: set() for col in table.columns}
    auto_increment_columns = {col.name for col in table.columns if col.autoincrement}

    inserted_count = 0  # 데이터 삽입 카운트
    
    # 유니크 인덱스가 있는 컬럼 찾기
    unique_columns = set()

    for col in table.primary_key.columns:
        unique_columns.add(col.name)

    for index in table.indexes:
        if index.unique:
            unique_columns.update(col.name for col in index.columns)

    for _ in range(num_rows):
        row = {}
        for col in table.columns:
            if col.name in auto_increment_columns:
                # 자동 증가 필드에 대해서는 값을 생성하지 않음
                row[col.name] = None
            if col.name in unique_columns:
                # 유니크 제약 조건이 있는 컬럼에 대해 기존 값을 참조하여 유니크한 값을 생성
                row[col.name] = generate_column_data(col.type, existing_values[col.name])
            else:
                row[col.name] = generate_column_data(col.type, None)
                
            existing_values[col.name].add(row[col.name])
        data.append(row)

        inserted_count += 1
        
        # 데이터 생성 후 카운트 출력
        print(f"테이블 {table.name}에 대해 {inserted_count}개의 행이 생성됨.")
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
    start_time = time.time()
    insert_data(config)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"소요 시간: {elapsed_time:.2f} 초")

if __name__ == '__main__':
    main()