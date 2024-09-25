oz/
├── conf/

│   ├── alchemy_db.py       # 엔진, 세션, 메타데이터 생성
│   └── config_loader.py    # 설정 파일 로더
├── init.py

├── api.py                  # Flask를 이용한 API
├── data_generator.py       # 더미 데이터 생성
├── insert_data.py          # DB 연결 및 더미데이터 삽입
├── inspector.py            # DB 인스펙터
├── main.py                 # 메인 실행 함수
├── menu.py                 # TUI 메뉴
├── migration.py            # 데이터 마이그레이션
├── README.md

├── requirements.txt        # 라이브러리 목록
├── schema_compare.md       # 스키마 비교 결과 출력
└── resources/              # 설정 파일
└── config.json        # JSON 설정 파일
