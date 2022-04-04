#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 0:01
# @Author  : YarnBlue
# @Des     :
# @Site    : 
# @File    : main.py
# @Software: PyCharm
from factory import Factory
from configs.configs import *

if __name__ == '__main__':
    with Factory(USERNAME, PASSWORD) as client:
        rep = client.goods.GoodsInfo.goods_info(9726)
