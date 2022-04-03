# -*- coding: utf-8 -*-
"""
@Time : 2022/3/30 14:27 
@Author : YarnBlue 
@description : 
@File : RenRen_api.py
"""
import requests

from api.url.url import URL


class RenRenApi:
    def __init__(self, cookie: str, session: requests.Session, session_id: str, shop_id: str, **kwargs):
        self.cookie = cookie
        self.session = session
        self.session_id = session_id
        self.shop_id = shop_id
        self.kwargs = kwargs
        self.headers = {
            'cookie': cookie,
            'session-id': session_id,
            'shop-id': shop_id,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/99.0.4844.84 Safari/537.36',
            'client-type': '50'
        }
        self.session.headers = self.headers
        self.URL = URL()
