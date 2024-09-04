from inspector import get_schemas, get_tables, get_table_info, get_ddl
from conf.config_loader import load_config
from migration import migrate_data, compare_all_schemas, compare_schemas

def display_main_menu():
    print("=== 데이터베이스 관리 도구 ===")
    print("1. 데이터베이스 정보 조회")
    print("2. 더미 데이터 생성 및 삽입")
    print("3. MySQL에서 MongoDB로 데이터 마이그레이션")
    print("4. 스키마 비교")
    print("5. 종료")
    return input("원하는 작업을 선택하세요 (1-5): ")

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
    
def handle_migration():
    config = load_config()
    print("=== MySQL에서 MongoDB로 데이터 마이그레이션 ===")
    print("데이터베이스 선택:")
    for i, db_name in enumerate(config.keys(), 1):
        print(f"{i}. {db_name}")
    print("3. 전체 마이그레이션")
    
    try:
        db_choice = int(input("선택: ")) - 1

        if db_choice == 2:  # 전체 마이그레이션 선택
            for db_name in config.keys():
                print(f"\n{db_name}의 테이블 선택:")
                tables = list(config[db_name]['tables'].keys())
                for table_name in tables:
                    target_collection = config[db_name]['tables'][table_name]['target_collection']
                    print(f"마이그레이션 중: {table_name} -> {target_collection}")
                    migrate_data(db_name, table_name, f"{db_name}_mongo", target_collection)
            print("전체 마이그레이션이 완료되었습니다.")
            return

        db_name = list(config.keys())[db_choice]

        print(f"\n{db_name}의 테이블 선택:")
        tables = list(config[db_name]['tables'].keys())
        for i, table_name in enumerate(tables, 1):
            print(f"{i}. {table_name}")
        
        table_choice = int(input("선택: ")) - 1

        if table_choice < 0 or table_choice >= len(tables):
            print("잘못된 선택입니다. 다시 시도해 주세요.")
            return

        table_name = tables[table_choice]
        target_collection = config[db_name]['tables'][table_name]['target_collection']
        
        migrate_data(db_name, table_name, f"{db_name}_mongo", target_collection)
        print(f"{table_name}의 마이그레이션이 완료되었습니다.")

    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력해 주세요.")
    except IndexError:
        print("잘못된 선택입니다. 다시 시도해 주세요.")

def handle_schema_comparison():
    print("=== 스키마 비교 ===")
    print("1. 모든 스키마 비교")
    print("2. 특정 테이블 스키마 비교")
    
    choice = input("선택: ")

    if choice == '1':
        compare_all_schemas()
    elif choice == '2':
        config = load_config()
        print("데이터베이스 선택:")
        for i, db_name in enumerate(config.keys(), 1):
            print(f"{i}. {db_name}")
        
        try:
            db_choice = int(input("선택: ")) - 1
            db_name = list(config.keys())[db_choice]

            print(f"\n{db_name}의 테이블 선택:")
            tables = list(config[db_name]['tables'].keys())
            for i, table_name in enumerate(tables, 1):
                print(f"{i}. {table_name}")

            table_choice = int(input("선택: ")) - 1

            if table_choice < 0 or table_choice >= len(tables):
                print("잘못된 선택입니다. 다시 시도해 주세요.")
                return

            table_name = tables[table_choice]
            target_collection = config[db_name]['tables'][table_name]['target_collection']
            compare_schemas(db_name, table_name, f"{db_name}_mongo", target_collection)

        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해 주세요.")
        except IndexError:
            print("잘못된 선택입니다. 다시 시도해 주세요.")
    else:
        print("잘못된 선택입니다. 1 또는 2를 입력해 주세요.")

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