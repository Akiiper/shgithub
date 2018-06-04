# -*- coding: utf-8 -*-

'''
代理 ip 池
'''
import random

class RandomProxy(object):
    
    def __init__(self):
        self.proxylist = \
        ['https://125.118.150.165:6666',
         'https://36.6.141.158:61234',
         'https://183.159.85.170:18118',
         'https://223.241.117.32:8010',
         'https://183.159.85.201:808',
         \
         'https://183.128.33.20:18118',
         'https://27.209.235.229:61234',
         'https://183.159.88.105:18118',
         'https://125.118.42.222:8118',
         'https://114.239.215.78:61234']
        
    def random_proxy(self):
        return random.choice(self.proxylist)
    
_inst = RandomProxy()
random_proxy = _inst.random_proxy