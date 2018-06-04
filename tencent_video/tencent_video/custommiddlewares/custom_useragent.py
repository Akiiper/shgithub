# -*- coding: utf-8 -*-

'''
user-agent 中间件
'''

import tencent_video.resouces.useragent_pool as up
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class CustomUserAgentMiddleware(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = up.random_agent()
        print('使用 User-Agent: %s' %ua)
        request.headers.setdefault(b'User-Agent', ua)