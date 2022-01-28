# -*- coding: utf-8 -*-
#
# Global Entry File
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

version = "0.5.0"     # System version number
title, description = parse_readme()
app_backend = FastAPI(
    debug=DEBUG,
    title=title,
    description=description,
    version=version,
    # dependencies=[Depends(get_query_token),
)

# Cross-domain issues
origins = ['*']
app_backend.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app_backend.get("/version", summary='Get system version number',
         response_model=VersionResp)
async def version_api():
    """Get system version number"""
    return {"version": version}

@app_backend.get("/getIssueEventsPoll",summary='Get the number of additional usdt',
            response_model=EventResp)
async def getIssueEventsPoll():
    "Get the number of additional usdt"
    getfunc = GetEvent()
    resdata = getfunc.getIssueEventsPoll()
    return {"events":resdata}

@app_backend.get("/getIssueEventsPollCon",summary='Get the latest number of additional usdt issues',
            response_model=EventConResp)
async def getIssueEventsPollCon():
    "Get the latest number of additional usdt issues"
    getfunc = GetEvent()
    resdata = getfunc.getIssueEventsPollCon()
    return {"events":int(resdata)}

@app_backend.get("/getUSDTMKTCAP",summary='Get the total market cap of USDT outstanding',
            response_model=MKTCAP)
async def getUSDTMKTCAP():
    "Get the total market value of USDT outstanding"
    import requests,json
    url = "https://min-api.cryptocompare.com/data/top/exchanges/full?fsym=USDT&tsym=USD"
    data = json.loads(requests.get(url).text)
    data = data['Data']['AggregatedData']['MKTCAP']
    print(data)
    return {"MKTCAP":float(data)}

@app_backend.get("/getETHMKTCAP",summary='Get the total market cap of ETH outstanding',
            response_model=MKTCAP)
async def getETHMKTCAP():
    "Get the total market cap of ETH outstanding"
    import requests,json
    url = "https://min-api.cryptocompare.com/data/top/exchanges/full?fsym=ETH&tsym=USD"
    data = json.loads(requests.get(url).text)
    data = data['Data']['AggregatedData']['MKTCAP']
    print(data)
    return {"MKTCAP":float(data)}


@app_backend.get("/getReserve",summary='Get USDT reserve amount',
            response_model=MKTCAP)
async def getReserve():
    "Get USDT reserve amount"
    data = 69156771674
    return {"MKTCAP":data}

@app_backend.get("/risk_factor",summary='Get Risk Factor',
            response_model=MKTCAP)
async def risk_factor():
    "Get Risk Factor"
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