import random
from sqlalchemy.sql.sqltypes import String, Integer, Float, Date, DateTime, Boolean, SmallInteger, DECIMAL, Enum, Time
from utils import generate_unique_string, generate_unique_integer
from faker import Faker

faker = Faker()

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
        return faker.text(max_nb_chars=100)

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
            if col.autoincrement:
                row[col.name] = None
            if col.name in unique_columns:
                # 유니크 제약 조건이 있는 컬럼에 대해 기존 값을 참조하여 유니크한 값을 생성
                row[col.name] = generate_column_data(col.type, existing_values[col.name])
            else:
                row[col.name] = generate_column_data(col.type, None)
                
            existing_values[col.name].add(row[col.name])
        data.append(row)
        
        inserted_count += 1
        
        print(f"테이블 {table.name}에 대해 {inserted_count}개의 행이 생성됨.")
    return data