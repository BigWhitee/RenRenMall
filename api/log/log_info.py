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


if __name__ == '__main__':
    fetcher = FetchLogList(COOKIE, requests.Session(), SESSION_ID, SHOP_ID)
    logInfo = LogInfo(COOKIE, requests.Session(), SESSION_ID, SHOP_ID)
    while fetcher.next(identify_code=200001, pagesize=100, **{'create_time[0]': '2022-04-01 00:00:00', 'create_time[1]': '2022-04-02 12:00:00'}):
        results = fetcher.result()
        for result in results:
            id = result['id']
            infos = logInfo.log_info(id)
            goods_id = infos['relation_ids']
            if goods_id == '9726':
                print(id)
                print(infos['dirty_primary']['基本设置']['商品规格'])
                sys.exit()

