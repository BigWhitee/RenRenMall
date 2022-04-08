# -*- coding: utf-8 -*-
"""
@Time : 2022/4/6 15:07 
@Author : YarnBlue 
@description : 
@File : test.py 
"""
import json
import random

from RenRen_Shop.factory import Factory


if __name__ == '__main__':
    with Factory() as client:
        if client.goods.edit_goods(10844, options__0__price=70):
            client.logger.info('Done!')
