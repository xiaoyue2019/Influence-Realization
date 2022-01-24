# -*- coding: utf-8 -*-
#
# 全局入口文件
# Author: xiaoyue
# Email: xiaoyue2019@outlook.com
# Created Time: 2021-12-14
from telnetlib import TM
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app_demo_event import GetEvent
from settings import DEBUG
from utils import parse_readme
from schema import VersionResp,EventResp,EventConResp,MKTCAP

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

@app.get("/getUSDTMKTCAP",summary='获取USDT总流通市值',
            response_model=MKTCAP)
async def getUSDTMKTCAP():
    "获取USDT总流通市值"
    import requests,json
    url = "https://min-api.cryptocompare.com/data/top/exchanges/full?fsym=USDT&tsym=USD"
    data = json.loads(requests.get(url).text)
    data = data['Data']['AggregatedData']['MKTCAP']
    print(data)
    return {"MKTCAP":float(data)}

@app.get("/getETHMKTCAP",summary='获取ETH总流通市值',
            response_model=MKTCAP)
async def getETHMKTCAP():
    "获取ETH总流通市值"
    import requests,json
    url = "https://min-api.cryptocompare.com/data/top/exchanges/full?fsym=ETH&tsym=USD"
    data = json.loads(requests.get(url).text)
    data = data['Data']['AggregatedData']['MKTCAP']
    print(data)
    return {"MKTCAP":float(data)}


@app.get("/getReserve",summary='获取USDT准备金金额',
            response_model=MKTCAP)
async def getReserve():
    "获取usdt准备金金额"
    data = 69156771674
    return {"MKTCAP":data}

@app.get("/risk_factor",summary='获取风险系数',
            response_model=MKTCAP)
async def risk_factor():
    "获取风险系数"
    import requests,json
    url = "https://min-api.cryptocompare.com/data/top/exchanges/full?fsym=ETH&tsym=USD"
    data = json.loads(requests.get(url).text)
    _TM = data['Data']['AggregatedData']['MKTCAP']
    url = "https://min-api.cryptocompare.com/data/top/exchanges/full?fsym=USDT&tsym=USD"
    data = json.loads(requests.get(url).text)
    _UM = data['Data']['AggregatedData']['MKTCAP']
    _ULM = _UM
    _RM = 69156771674

    data = (_ULM/_TM)*(_UM/_RM)
    return {"MKTCAP":float(data)}