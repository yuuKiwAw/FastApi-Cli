from sqlalchemy.orm import Session
from DBcontroller import models, schemas

# 获取Usertest表所有信息
def get_userinfo(db: Session):
    return db.query(models.Usertest).all()