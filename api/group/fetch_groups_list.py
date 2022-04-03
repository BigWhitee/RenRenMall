# -*- coding: utf-8 -*-
"""
@Time : 2022/4/1 20:10 
@Author : YarnBlue 
@description : 
@File : fetch_groups_list.py
"""
import time

import requests

from common.fetch import Fetch
from configs.configs import *


class FetchGroupsList(Fetch):
    def __init__(self, cookie: str, session: requests.Session, session_id: str, shop_id: str, **kwargs):
        """

        :param cookie:
        :param session:
        :param session_id:
        :param shop_id:
        :param kwargs:
        """
        super().__init__(cookie, session, session_id, shop_id, **kwargs)
        self.first = self.URL.group_list()
        self.Temp = {
            'pagesize': 10,
            'page': 1,
            'pager': 1,
            'name': '',
        }
        self.next_page = 1
        self.is_end = False

    def fetch(self, url, **kwargs):
        rep = self.session.get(url, params=kwargs).json()
        self.data = rep['list']
        self.next_page = self.Temp['page'] + 1
        self.previous_page = self.Temp['page'] - 1
        try:
            if rep['total'] < rep['page_size']:
                self.is_end = True
            else:
                self.is_end = False
        except:
            self.is_end = True
        if self.Temp['page'] == 1:
            self.is_start = True
        else:
            self.is_start = False

    def start(self, **kwargs):
        """

        :param kwargs: 可接受参数如下：

        =========================
        pagesize: 每页数据量
        page: 页码
        pager: ?,默认为1
        name: 商品组名称
        =========================

        :return:
        """
        if kwargs:
            for index, (key, value) in enumerate(kwargs.items()):
                self.Temp[key] = value
        self.fetch(self.first, **self.Temp)

    def next(self, **kwargs):
        if self.is_end:
            return False
        else:
            if kwargs:
                for index, (key, value) in enumerate(kwargs.items()):
                    self.Temp[key] = value
            self.Temp['page'] = self.next_page
            self.fetch(self.first, **self.Temp)
            return True

    def previous(self) -> bool:

        if self.is_start:
            return False
        else:
            self.Temp['page'] = self.previous_page
            self.fetch(self.first, **self.Temp)
            return True

    def result(self):
        return self.data

if __name__ == '__main__':
    fetcher = FetchGroupsList(COOKIE, requests.Session(), SESSION_ID, SHOP_ID)
    while fetcher.next(name='分销组'):
        print(fetcher.result())

