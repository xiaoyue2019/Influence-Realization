# -*- coding: utf-8 -*-
#
# 通用schema
# Author: xiaoyue
# Email: xiaoyue2019@outlook.com
# Created Time: 2021-12-14
from pydantic import BaseModel, Field


class MessageResp(BaseModel):
    message: str = Field(..., title='提示信息', description='提示信息')


class VersionResp(BaseModel):
    version: str = Field(..., title='版本信息', description='版本信息')

class EventResp(BaseModel):
    events: list

class EventConResp(BaseModel):
    events: int