# -*- coding: utf-8 -*-
"""
@Time : 2022/3/30 11:05 
@Author : YarnBlue 
@description : 
@File : uploader.py 
"""
from abc import ABC

import requests

from api.url.url import URL


class Uploader(ABC):
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.URL = URL()
        self.cookie = self.kwargs['cookie']
        self.session_id = kwargs['session_id']
        self.shop_id = kwargs['shop_id']
        self.session: requests.Session = self.kwargs['session']
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
            'cookie': self.cookie,
            'session_id': self.session_id,
            'shop_id': self.shop_id
        }
        self.session.headers = self.headers

    def upload(self, file, from_web=False, **kwargs):
        pass
