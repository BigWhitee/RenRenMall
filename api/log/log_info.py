# -*- coding: utf-8 -*-
"""
@Time : 2022/4/2 14:07 
@Author : YarnBlue 
@description : 
@File : log_info.py
"""
import sys

import requests

from api.RenRen_api import RenRenApi
from api.log.fetch_log_list import FetchLogList
from configs.configs import *


class LogInfo(RenRenApi):
    def log_info(self, id):
        rep = self.session.get(self.URL.log_info(), params={'id': id})
        return rep.json()


