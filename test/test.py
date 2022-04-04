# -*- coding: utf-8 -*-
"""
@Time : 2022/4/4 16:51 
@Author : YarnBlue 
@description : 
@File : test.py 
"""
from factory.factory import Factory

if __name__ == '__main__':
    with Factory() as client:
        loginfo = client.log.LogInfo.log_info(146467)
        print(loginfo)
        