#!/usr/bin/python3.8.5
# author:yuki
# -*- coding:utf-8 -*-

import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controller import app01

app = FastAPI(
    title='FastApi Cli By Yuki',
    description='yuki自己的FastApi脚手架',
    version='block1'
)


# 跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1",
        "http://127.0.0.1:8080"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 加载api路由模块
app.include_router(app01, prefix='/example', tags=['Examples'])

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, debug=True, workers=1)
