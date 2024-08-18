from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from data_generator import generate_dummy_data

# 데이터베이스 연결 설정 및 데이터 삽입
def insert_data(config):
    db_config = config['database']
    engine = create_engine(f"mysql+pymysql://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database_name']}")
    metadata = MetaData()
    metadata.reflect(bind=engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    for table_name, table_config in config['tables'].items():
        table = Table(table_name, metadata, autoload_with=engine)
        if table_config.get('mode') == 'replace':
            session.execute(table.delete())
        
        dummy_data = generate_dummy_data(table, table_config['rows'])
        
        batch_size = 5000
        for i in range(0, len(dummy_data), batch_size):
            batch = dummy_data[i:i + batch_size]
            session.execute(table.insert(), batch)

    session.commit()
    session.close()