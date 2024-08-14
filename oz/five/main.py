import argparse
import time
from config import load_config
from database import insert_data

# 메인 함수
def main():
    parser = argparse.ArgumentParser(description='Generate and insert dummy data into MySQL tables.')
    parser.add_argument('config', type=str, help='Path to the configuration file (JSON).')
    args = parser.parse_args()
    
    config = load_config(args.config)
    start_time = time.time()
    insert_data(config)
    end_time = time.time()
    print(f"소요 시간: {end_time - start_time:.2f} 초")

if __name__ == '__main__':
    main()