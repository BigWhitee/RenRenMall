# -*- coding: utf-8 -*-
"""
@Time : 2022/4/1 14:49 
@Author : YarnBlue 
@description : 
@File : goods_info.py 
"""
import json

import requests

from api.RenRen_api import RenRenApi
from configs.configs import *


class GoodsInfo(RenRenApi):
    def goods_info(self, id):
        rep = self.session.get(self.URL.goods_info(), params={'id': id})
        return rep.json()


