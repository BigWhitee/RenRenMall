#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 0:01
# @Author  : YarnBlue
# @Des     :
# @Site    : 
# @File    : main.py
# @Software: PyCharm
from factory import Factory

if __name__ == '__main__':
    with Factory(13207797541, 'zqb090325') as client:
        print('当前店铺管理的店铺名：', client.shop_name)
        goods = client.goods.FetchGoods
        goods.next(pagesize=5)
        print('获取5条最新的商品信息：', goods.result())
