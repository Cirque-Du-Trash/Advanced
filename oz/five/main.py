import time
from conf.config_loader import load_config
from conf.alchemy_db import get_engine
from insert_data import insert_data
from menu import display_main_menu, handle_database_info, handle_migration, handle_schema_comparison

def process_choice(choice, engine, config):
    if choice == '1':
        handle_database_info(engine)
    elif choice == '2':
        start_time = time.perf_counter()
        insert_data(config)
        elapsed_time = time.perf_counter() - start_time
        print(f"소요 시간: {elapsed_time:.2f} 초")
    elif choice == '3':
        handle_migration()
    elif choice == '4':
        handle_schema_comparison()
    elif choice == '5':
        print("프로그램을 종료합니다.")
        return False
    else:
        print("유효하지 않은 선택입니다. 다시 시도해 주세요.")
    return True

def main():
    config = load_config()
    engine = get_engine(config['oz']['source_database'])

    while True:
        choice = display_main_menu()
        if not process_choice(choice, engine, config):
            break

if __name__ == '__main__':
    main()