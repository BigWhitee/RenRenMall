# -*- coding: utf-8 -*-
"""
@Time : 2022/3/30 11:07 
@Author : YarnBlue 
@description : 
@File : img_uploader.py 
"""
import os.path

import requests, io
from PIL import Image

from api.uploader.uploader import Uploader
from api.url.url import URL
from configs.configs import *


class ImgUploader(Uploader):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
            'cookie': self.cookie,
            'session-id': self.session_id,
            'shop-id': self.shop_id,
            'client-type': '50'
        }
        self.session.headers = self.headers

    @staticmethod
    def get_format(file, byte=False) -> str:
        if byte:
            img_io = io.BytesIO(file)
            i = Image.open(img_io)
        else:
            i = Image.open(file)
        return i.format

    def upload(self, file, from_web=False, **kwargs):
        """
        上传图片到服务器
        返回格式为：
        ===================
        {
            'error': 0,
            'id': 91703,
            'path': 'image/480/2022/03/5b0e0cc36474ba25bb1316654261dadb.jpeg'
        }
        ===================
        :param file:
        :param from_web:
        :param kwargs: 需指定group_id, type；如果是网络图片，还需指定filename
        :return:
        """
        type = kwargs['type']  # 10为图片上传
        group_id = kwargs['group_id']
        if from_web:
            content = requests.get(file).content
            img_format = self.get_format(content, byte=True)
            files = {
                'type': (None, type),
                'group_id': (None, group_id),
                'file': (f'{kwargs["filename"]}.{img_format.lower()}', content, f'image/{img_format}')
            }
        else:
            filename = os.path.basename(file)
            with open(file, 'rb') as f:
                content = f.read()

            files = {
                'type': (None, type),
                'group_id': (None, group_id),
                'file': (filename, content, f'image/{self.get_format(file)}')
            }
        rep = self.session.post(self.URL.upload_img(), files=files)
        return rep.json()


if __name__ == '__main__':
    cookie = COOKIE
    Uploader = ImgUploader(cookie=cookie, session=requests.Session(), session_id=SESSION_ID, shop_id=SHOP_ID)

    file = 'https://wx.hi-bro.club/attachment/images/6/2022/03/CP38d7sp30D3wSBdKCWH3udpR3DmX3.jpg'
    rep = Uploader.upload(file, from_web=True, type=10, group_id=487, filename='网络图片')
    print(rep)
