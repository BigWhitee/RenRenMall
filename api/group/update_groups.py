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
from api.group.groups_info import GroupsInfo

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

    def add_goods_to_groups(self, group_id, *goods_id):
        InfoGetter = GroupsInfo(self.session, **self.kwargs)
        inofs = InfoGetter.groups_info(group_id)


