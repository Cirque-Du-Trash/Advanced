from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from conf.app_config import db_username, db_password, db_host, db_port, db_name

engine = create_engine(f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")
metadata = MetaData()
metadata.reflect(bind=engine)
    
Session = sessionmaker(bind=engine)