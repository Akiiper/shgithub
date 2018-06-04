# -*- coding: utf-8 -*-

'''
数据库存取
'''

import sys
from config import config
from util.exception import ConDbFail

try:
    if config.DB_CONFIG['DB_CONNECT_TYPE'] == 'pymongo':
        '''
        todo
        '''
        pass
    elif config.DB_CONFIG['DB_CONNECT_TYPE'] == 'redis':
        from db.RedisHelper import RedisHelper
        sqlhelper = RedisHelper()
    else:
        from db.SqlHelper import SqlHelper
        sqlhelper = SqlHelper()
    
    sqlhelper.init_db()
    
except Exception as e:
    raise ConDbFail

def store_data(queue2, db_proxy_num):
    '''
    读取队列中的数据，写入数据库中
    :param queue2:
    :return:
    '''
    successNum = 0
    failNum = 0
    while True:
        try:
            proxy = queue2.get(timeout=300)
            if proxy:
                sqlhelper.insert(proxy)
                successNum += 1
            else:
                failNum += 1
            
            str = 'IPProxyPool----->>>>>>>>Success ip num: %d, Fail ip num: %d' %(successNum, failNum)
            sys.stdout.write(str + "\r")
            sys.stdout.flush()
        except BaseException as e:
            if db_proxy_num.value !=0:
                successNum += db_proxy_num.value
                db_proxy_num.value = 0
                str = 'IPProxyPool----->>>>>>>>Success ip num : %d, Fail ip num: %d' %(successNum, failNum)
                sys.stdout.write(str + "\r")
                sys.stdout.flush()
                successNum = 0
                failNum = 0
