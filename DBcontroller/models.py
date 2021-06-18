from sqlalchemy import Column,String,INT
from sqlalchemy.ext.declarative import declarative_base
from .DataBaseManager import  Base

# 自定义表映射模板类
# usertest表
class Usertest(Base):    #定义一个类，继承Base
    __tablename__='usertest'
    ID = Column(INT(),primary_key=True)
    USER = Column(String(50))
    PASSWD = Column(String(50))
 
    def __repr__(self):
        return f'{self.ID}{self.USER}{self.PASSWD}'
