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
        if client.commission.add_goods_commission(9582):
            client.logger.info('Done!')
