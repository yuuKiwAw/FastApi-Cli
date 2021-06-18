from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# sqlserver
HOST = '192.168.228.153'
PORT = '6605'
USERNAME = 'sa'
PASSWORD = 'ccp12345'
DATABASE = 'DEMO2'
DB_URL_1 = f'mssql+pymssql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

# oracle

engine = create_engine(
    # echo=True表示引擎将用repr()函数记录所有语句及其参数列表到日志
    DB_URL_1, 
    encoding='utf-8', 
    echo=True
)
SessionLocal = sessionmaker(bind=engine)

# 创建基本映射类
Base = declarative_base(bind=engine, name='Base')
