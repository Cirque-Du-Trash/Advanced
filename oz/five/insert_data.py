from sqlalchemy import Table, text
from data_generator import generate_dummy_data
from conf.alchemy_db import get_engine, get_session, get_metadata


# 데이터베이스 연결 설정 및 데이터 삽입
def insert_data(config):
    for key in list(config):
        sub_config = config[key]
        db_config = sub_config['database']
        
        engine = get_engine(db_config)
        metadata = get_metadata(engine)
        session = get_session(engine)
        
        for table_name, table_config in sub_config['tables'].items():
            table = Table(table_name, metadata, autoload_with=engine)
            if table_config.get('mode') == 'replace':
                session.execute(text(f"TRUNCATE TABLE {table_name};"))
            
            dummy_data = generate_dummy_data(table, table_config['rows'])
            for i in range(0, len(dummy_data), 5000):
                batch = dummy_data[i:i + 5000] 
                session.execute(table.insert(), batch)
            
        session.commit()
        session.close()