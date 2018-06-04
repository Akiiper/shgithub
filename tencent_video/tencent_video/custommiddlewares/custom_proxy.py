# -*- coding: utf-8 -*-

import tencent_video.resouces.proxy_pool as pp

'''
代理服务器
'''

class CustomProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = pp.random_proxy()
        print('设置代理 IP：%s' %proxy)
        request.meta['proxy'] = proxy