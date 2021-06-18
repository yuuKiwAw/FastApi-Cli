from pydantic import BaseModel

class Userinfo(BaseModel):
    ID: int = 0
    USER: int = 0
    PASSWD: int = 0