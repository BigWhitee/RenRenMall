# -*- coding: utf-8 -*-
"""
@Time : 2022/3/30 11:11 
@Author : YarnBlue 
@description : 
@File : url.py 
"""
import random
import time


class URL:
    def __init__(self):
        self.host = 'https://rr.hanchenshop.com'

    def upload_img(self):
        return self.host + f'/shop/api/utility/attachment/list/upload'

    def add_album(self):
        return self.host + f'/shop/api/utility/attachment/group/add'

    def add_goods(self):
        return self.host + f'/shop/api/goods/index/add'

    def edit_goods(self):
        return self.host + f'/shop/api/goods/index/edit'

    def category_list(self):
        return self.host + f'/shop/api/goods/category/get-list'

    def goods_info(self):
        return self.host + '/shop/api/goods/index/get'

    def goods_list(self):
        return self.host + '/shop/api/goods/index/list'

    def add_group(self):
        return self.host + '/shop/api/goods/group/create'

    def group_list(self):
        return self.host + '/shop/api/goods/group/get-list'

    def groups_info(self):
        return self.host + '/shop/api/goods/group/get-one'

    def update_groups(self):
        return self.host + '/shop/api/goods/group/update'

    def log_list(self):
        return self.host + '/shop/api/sysset/log/list?page=1&pagesize=10'

    def log_info(self):
        return self.host + '/shop/api/sysset/log/detail'


if __name__ == '__main__':
    text = '3656,3659'
    test_ = text.split(',')
    print(text)
