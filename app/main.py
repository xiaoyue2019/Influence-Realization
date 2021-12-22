# -*- coding: utf-8 -*-
#
# 全局入口文件
# Author: xiaoyue
# Email: xiaoyue2019@outlook.com
# Created Time: 2021-12-14
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app_demo_event import GetEvent
from settings import DEBUG
from utils import parse_readme
from schema import VersionResp,EventResp,EventConResp

version = "0.5.0"     # 系统版本号
title, description = parse_readme()
app = FastAPI(
    debug=DEBUG,
    title=title,
    description=description,
    version=version,
    # dependencies=[Depends(get_query_token),
)

# 跨域问题
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# redis连接
# from common.connections import init_redis
# init_redis('192.168.1.242')   # 配置redis host

# 加载模块路由
# from test_module.router import router as test_router
# app.include_router(test_router, prefix="/test", tags=["测试模块"])

# 加载验证码模块
# from captcha_module.router import router as captcha_router
# app.include_router(captcha_router, prefix="/captcha", tags=["验证码模块"])


@app.get("/version", summary='获取系统版本号',
         response_model=VersionResp)
async def version_api():
    """获取系统版本号"""
    return {"version": version}

@app.get("/getIssueEventsPoll",summary='获取增发usdt数量',
            response_model=EventResp)
async def getIssueEventsPoll():
    "获取增发usdt数量"
    getfunc = GetEvent()
    resdata = getfunc.getIssueEventsPoll()
    return {"events":resdata}

@app.get("/getIssueEventsPollCon",summary='获取最新增发usdt数量',
            response_model=EventConResp)
async def getIssueEventsPollCon():
    "获取最新增发usdt数量"
    getfunc = GetEvent()
    resdata = getfunc.getIssueEventsPollCon()
    return {"events":int(resdata)}