import time
from conf.config_loader import load_config
from conf.alchemy_db import get_engine
from insert_data import insert_data
from inspector import display_main_menu, handle_database_info

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
            start_time = time.time()
            insert_data(config)
            end_time = time.time()
            print(f"소요 시간: {end_time - start_time:.2f} 초")

        elif choice == '3':
            print("프로그램을 종료합니다.")
            break

        else:
            print("유효하지 않은 선택입니다.")

if __name__ == '__main__':
    main()