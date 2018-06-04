# -*- coding: utf-8 -*-

'''
User-Agent 列表
'''
import random

class RandomUserAgent(object):
    def __init__(self):
        self.agentlist = \
        ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
         'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
         'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
         'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
         \
         'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
         'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
         \
         'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
         'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
         \
         'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11',
         'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)',
         'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
         'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)']
    
    def random_agent(self):
        '''
        从 agentlist 随机取出一个 User-Agent
        '''
        return random.choice(self.agentlist)
    
# 暴露接口
_inst = RandomUserAgent()
random_agent = _inst.random_agent
        
