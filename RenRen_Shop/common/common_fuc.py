# -*- coding: utf-8 -*-
"""
@Time : 2022/4/7 15:02 
@Author : YarnBlue 
@description : 
@File : common_fuc.py 
"""
import json
import os
import time
from RenRen_Shop.common.log import log
logger = log().log()


def str_2_time(dt):
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(timeArray)
    return timestamp


def time_2_str(timestamp):
    # 转换为localtime
    time_local = time.localtime(timestamp)
    # 转换为新的时间格式
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt


def template(Type, filePath) -> json:
    with open(os.path.join(filePath, f'template/{Type}_template.json'), 'rb') as f:
        data = json.load(f)
    return data


def exchange_params(data, split='__', **kwargs):
    for index, (keys, value) in enumerate(kwargs.items()):
        key_split = keys.split(split)
        level_count = len(key_split)
        if level_count == 1:
            data[key_split[0]] = value
        elif level_count == 2:
            data[key_split[0]][key_split[1]] = value
        elif level_count == 3:
            data[key_split[0]][key_split[1]][key_split[2]] = value
        else:
            logger.error('参数级数超过3')
    return data
