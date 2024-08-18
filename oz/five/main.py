import time
from conf.app_config import get_config
from database import insert_data

# 메인 함수
def main():
    config = get_config()
    start_time = time.time()
    insert_data(config)
    end_time = time.time()
    print(f"소요 시간: {end_time - start_time:.2f} 초")

if __name__ == '__main__':
    main()