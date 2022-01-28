# -*- coding: utf-8 -*-
#
# use schema
# Author: xiaoyue
# Email: xiaoyue2019@outlook.com
# Created Time: 2021-12-14
from pydantic import BaseModel, Field


class MessageResp(BaseModel):
    message: str = Field(..., title='Tip Message', description='tip Message')


class VersionResp(BaseModel):
    version: str = Field(..., title='Version information', description='version information')

class EventResp(BaseModel):
    events: list

class EventConResp(BaseModel):
    events: int

class MKTCAP(BaseModel):
    MKTCAP: float