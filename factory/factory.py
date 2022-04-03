#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 21:10
# @Author  : YarnBlue
# @Site    : api常用功能集合
# @File    : factory.py
# @Software: PyCharm
import time
from typing import TypeVar

import requests

from api.url.url import URL
from api.goods import *
from api.group import *
from api.log import *
from api.photo_album import *
from api.app import *
from api.uploader import *

Myshop = TypeVar('Myshop', int, str)


class Factory:
    def __init__(self, username, password, **kwargs):
        self.username = username
        self.password = password
        self.kwargs = kwargs
        self.session = requests.Session()
        self.URL = URL()
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/100.0.4896.60 Safari/537.36',
            'client-type': '50'
        }
        self.session_id = None
        self.cookie = None
        self.shop_id = None
        self.session.headers = self.headers
        self.request_session_id()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__logout()

    def __enter__(self):
        self.__login()
        self.__get_shop_id()
        self.__shop_init(self.shop_ids[0])
        return self

    def request_session_id(self):
        rep = self.session.get(self.URL.get_session_id(), **self.kwargs)
        self.session_id = rep.json()['session_id']
        self.headers['session-id'] = self.session_id
        self.session.headers = self.headers

    def __login(self):
        data = {
            'username': self.username,
            'password': self.password
        }
        rep = self.session.post(self.URL.login(), data=data, **self.kwargs)
        if rep.json()['error'] == 0:
            return True

    def __get_shop_id(self):
        t = int(time.time())
        rep = self.session.get(self.URL.shop_index(), params={'t': t})
        shop_list = rep.json()['list']
        self.shop = {}
        self.shop_ids = []
        self.shop_names = []
        for shop in shop_list:
            self.shop_ids.append(int(shop['shop_id']))
            self.shop_names.append(shop['name'])
            self.shop[shop['shop_id']] = shop['name']

    def __logout(self):
        rep = requests.post(self.URL.logout(), headers=self.headers, **self.kwargs)
        if rep.json()['error'] == 0:
            print('账号登出成功')
            return True
        else:
            print(rep.text)
            return False

    def switch_shop(self, myshop: Myshop):
        """
        切换需要管理的店铺，支持店铺ID或店铺名切换

        :param myshop:
        :return:
        """
        self.__shop_init(myshop)

    def __shop_init(self, myshop: Myshop):
        if isinstance(myshop, int):
            self.shop_id = myshop
            self.shop_name = self.shop[str(myshop)]
        if isinstance(myshop, str):
            self.shop_name = myshop
            self.shop_id = self.shop_ids[self.shop_names.index(myshop)]
        self.headers['shop-id'] = str(self.shop_id)
        self.goods = self.Goods(self.session, **self.kwargs)
        self.group = self.Groups(self.session, **self.kwargs)
        self.log = self.Log(self.session, **self.kwargs)

    class Goods:
        def __init__(self, session, **kwargs):
            """
            商品功能模块

            :param session:
            """
            self.session = session
            self.kwargs = kwargs
            self.AddGoods = AddGoods(self.session, **self.kwargs)
            self.EditGoods = EditGoods(self.session, **self.kwargs)
            self.FetchGoods = FetchGoodsList(self.session, **self.kwargs)
            self.GoodsInfo = GoodsInfo(self.session, **self.kwargs)

    class Groups:
        def __init__(self, session, **kwargs):
            """
            商品分组功能模块

            :param session:
            """
            self.session = session
            self.kwargs = kwargs
            self.AddGroup = AddGroup(self.session, **self.kwargs)
            self.FetchGroupsList = FetchGroupsList(self.session, **self.kwargs)
            self.GroupsInfo = GroupsInfo(self.session, **self.kwargs)

    class Log:
        def __init__(self, session, **kwargs):
            """
            店铺操作日志功能版块

            :param session:
            :param kwargs:
            """
            self.session = session
            self.kwargs = kwargs
            self.FetchLogList = FetchLogList(self.session, **self.kwargs)
            self.LogInfo = LogInfo(self.session, **self.kwargs)

    class PhotoAlbum:
        def __init__(self, session, **kwargs):
            """
            相册功能模块

            """
            self.session = session
            self.kwargs = kwargs
            self.AddAlbum = AddAlbum(self.session, **self.kwargs)

    class Upload:
        def __init__(self, session, **kwargs):
            """
            文件上传功能模块

            :param session:
            :param kwargs:
            """
            self.session = session
            self.kwargs = kwargs
            self.ImgUploader = ImgUploader(self.session, **self.kwargs)

    class App:
        def __init__(self, session, **kwargs):
            """
            常用应用功能模块

            :param session:
            :param kwargs:
            """
            self.session = session
            self.kwargs = kwargs
            self.MassUpdate_goods = MassUpdateGoods(self.session, **self.kwargs)




