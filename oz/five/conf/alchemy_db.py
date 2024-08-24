from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

def get_engine(db_config):
    return create_engine(f"mysql+pymysql://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database_name']}")

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()

def get_metadata(engine):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    return metadata