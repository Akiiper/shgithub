# -*- coding: utf-8 -*-

from config import config

'''
处理异常工具
'''

class TestUrlFail(Exception):
    def __str__(self):
        return "访问 %s 失败，请检查网络连接" %config.TEST_IP
    
class ConDbFail(Exception):
    def __str__(self):
        return "使用 DB_CONNECT_STRING: %s --连接数据库失败" %config.DB_CONFIG['DB_CONNECT_STRING']