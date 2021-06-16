#!/usr/bin/python3.8.5
# author:yuki
# -*- coding:utf-8 -*-

from fastapi import APIRouter, HTTPException, status

from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, Field

app01 = APIRouter()


"""Request请求模型"""
@app01.get("/helloworld")
async def helloworld():
    return {'message': 'Hello World!'}

# 路径传递
@app01.get("/base1/{str}")
async def req_parmas01(str: str):
    return {str}

@app01.get("/base/hello")
async def req_parmas02(strval: str, code: Optional[int] = None, color: str = "red"):
    return {"info": strval, "code": code, color:"color"}

# 枚举类型传递
class DataInfo(str, Enum):
    Zero1 = "XX"
    Zero2 = "YY"
@app01.get("/enum/{data}")
async def enumdata(data: DataInfo):
    if data == DataInfo.Zero1:
        return {'Message': data, "code": "01"}
    if data == DataInfo.Zero2:
        return {'Message': data, "code": "02"}

# 定义请求体类
class FakeData(BaseModel):
    name: str = Field(..., example="Yuki")  # example注解作用，  ...表示必填
    country: str = None
    address: str = None
# 请求体
@app01.post("/request_body")
async def fakedata(name: FakeData):
    return name.dict()


""""错误处理"""
@app01.get("/exception")
async def http_exception(strval: Optional[str] = None):
    if strval != "EXE":
        raise HTTPException(status_code=404, detail="wrong", headers={"X-Error": "Error"})
    return {strval}