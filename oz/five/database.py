from sqlalchemy import create_engine, MetaData, Table, text
from sqlalchemy.orm import sessionmaker
from data_generator import generate_dummy_data
from conf.app_config import db_username, db_password, db_host, db_port, db_name

# 데이터베이스 연결 설정 및 데이터 삽입
def insert_data(config):
    engine = create_engine(f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")
    metadata = MetaData()
    metadata.reflect(bind=engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    for table_name, table_config in config['tables'].items():
        table = Table(table_name, metadata, autoload_with=engine)
        
        if table_config.get('mode') == 'replace':
            session.execute(text(f"TRUNCATE TABLE {table_name};"))
        
        dummy_data = generate_dummy_data(table, table_config['rows'])
        session.execute(table.insert(), dummy_data)

    session.commit()
    session.close()