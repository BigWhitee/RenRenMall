# -*- coding: utf-8 -*-
"""
@Time : 2022/4/1 20:29 
@Author : YarnBlue 
@description : 
@File : update_groups.py
"""
import requests

from api.RenRen_api import RenRenApi
from configs.configs import *

class UpdateGroups(RenRenApi):
    def update_groups(self, id, *goods_ids, **kwargs):
        """
        更新商品组信息

        :param id: 商品组id
        :param goods_ids: 内含商品id列表
        :param kwargs: 根据需求传入对应属性值
        :return:
        """
        data = {
            'id': id,
            'shop_id': 480,
            'status': 1,
            'name': '分销组',
            'desc': '',
            'sort_type': 0,
        }
        for index, value in enumerate(goods_ids):
            data[f'goods_id[{index}]'] = value
        for index, (key, value) in enumerate(kwargs.items()):
            data[key] = value
        print(data)
        rep = self.session.post(self.URL.update_groups(), data=data)
        if rep.json()['error'] == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    client = UpdateGroups(COOKIE, requests.Session(), SESSION_ID, SHOP_ID)
    client.update_groups(72, 9602, 9603, 9604, name='分销组', desc='开启分销的商品')
