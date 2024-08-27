from sqlalchemy import inspect

# 특정 데이터베이스에 속한 schema 목록 반환
def get_schemas(engine):
    return inspect(engine).get_schema_names()

# 특정 데이터베이스의 schema에 속한 테이블 목록 반환
def get_tables(engine, schema):
    return inspect(engine).get_table_names(schema=schema)

# 특정 데이터베이스의 schema에 속한 뷰 목록 반환
def get_views(engine, schema):
    return inspect(engine).get_view_names(schema=schema)

# 특정 데이터베이스의 schema에 속한 테이블 목록과 테이블 별 컬럼정보, 코멘트를 반환
def get_table_info(engine, schema):
    inspector = inspect(engine)
    tables_info = {}
    for table_name in inspector.get_table_names(schema=schema):
        columns = inspector.get_columns(table_name, schema=schema)
        tables_info[table_name] = {
            "columns": [
                {
                    "name": col['name'],
                    "type": str(col['type']),
                    "nullable": col['nullable'],
                    "primary_key": col.get('primary_key', False),  # 기본값을 False로 설정
                    "comment": col.get('comment', '')
                } for col in columns
            ],
            "indexes": inspector.get_indexes(table_name, schema=schema)
        }
    return tables_info


# 특정 데이터베이스의 schema에 속한 뷰 목록과 뷰 별 컬럼정보, 코멘트를 반환
def get_view_info(engine, schema):
    inspector = inspect(engine)
    views_info = {}
    for view_name in inspector.get_view_names(schema=schema):
        columns = inspector.get_columns(view_name, schema=schema)
        views_info[view_name] = {
            "columns": [
                {
                    "name": col['name'],
                    "type": str(col['type']),
                    "nullable": col['nullable'],
                    "comment": col.get('comment', '')
                } for col in columns
            ]
        }
    return views_info

# 특정 테이블의 컬럼정보, 코멘트를 조회하는 함수
def get_column_info(engine, table_name, schema):
    inspector = inspect(engine)
    columns = inspector.get_columns(table_name, schema=schema)
    return [
        {
            "name": col['name'],
            "type": str(col['type']),
            "nullable": col['nullable'],
            "primary_key": col['primary_key', False],
            "comment": col.get('comment', '')
        } for col in columns
    ]

# 특정 테이블의 DDL 스크립트 생성 함수
def get_ddl(engine, table_name, schema):
    inspector = inspect(engine)
    ddl = f"CREATE TABLE {schema}.{table_name} (\n"
    columns = inspector.get_columns(table_name, schema=schema)
    for col in columns:
        ddl += f"  {col['name']} {col['type']}"
        if not col['nullable']:
            ddl += " NOT NULL"
        if 'primary_key' in col and col['primary_key']:
            ddl += " PRIMARY KEY"
        ddl += ",\n"
    ddl = ddl.rstrip(",\n") + "\n);"
    return ddl

# TUI 관련 함수

def display_main_menu():
    print("=== 데이터베이스 관리 도구 ===")
    print("1. 데이터베이스 정보 조회")
    print("2. 더미 데이터 생성 및 삽입")
    print("3. 종료")
    choice = input("원하는 작업을 선택하세요 (1-3): ")
    return choice

def display_menu():
    print("=== 데이터베이스 정보 조회 ===")
    print("1. 스키마 목록 조회")
    print("2. 특정 스키마의 테이블 목록 조회")
    print("3. 특정 테이블의 정보 조회")
    print("4. 특정 테이블의 DDL 스크립트 생성")
    print("5. 종료")
    choice = input("원하는 작업을 선택하세요 (1-5): ")
    return choice

def handle_database_info(engine):
    while True:
        db_choice = display_menu()
        if db_choice == '1':
            schemas = get_schemas(engine)
            print("Schemas:", schemas)

        elif db_choice == '2':
            schemas = get_schemas(engine)
            schema = input("조회할 스키마를 입력하세요: ")
            if schema in schemas:
                tables = get_tables(engine, schema)
                print(f"Tables in {schema}:", tables)
            else:
                print("유효하지 않은 스키마입니다.")

        elif db_choice == '3':
            schemas = get_schemas(engine)
            schema = input("조회할 스키마를 입력하세요: ")
            if schema in schemas:
                table_name = input("조회할 테이블 이름을 입력하세요: ")
                table_info = get_table_info(engine, schema)
                if table_name in table_info:
                    print(f"Table Info in {schema} for {table_name}:", table_info[table_name])
                else:
                    print("유효하지 않은 테이블입니다.")
            else:
                print("유효하지 않은 스키마입니다.")

        elif db_choice == '4':
            schemas = get_schemas(engine)
            schema = input("조회할 스키마를 입력하세요: ")
            if schema in schemas:
                table_name = input("DDL 스크립트를 생성할 테이블 이름을 입력하세요: ")
                ddl = get_ddl(engine, table_name, schema)
                print(f"DDL for {table_name} in {schema}:\n{ddl}")
            else:
                print("유효하지 않은 스키마입니다.")

        elif db_choice == '5':
            break

        else:
            print("유효하지 않은 선택입니다.")