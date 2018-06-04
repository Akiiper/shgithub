# -*- coding: utf-8 -*-

from changhong.middlewares.resources import PROXY_IPS
import random

'''
代理池
'''
class RandomProxy(object):
    
    def process_request(self, request, spider):
        
        proxy = random.choice(PROXY_IPS)
        request.meta['proxy'] = 'http://%s' %proxy
        print('代理 ip: %s \n' %proxy)
        
        
'''
selenium
'''
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging import getLogger
from scrapy.http import HtmlResponse
import time


class SeleniumMiddleware():
    def __init__(self, timeout=None, service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.browser = webdriver.Firefox()
        #self.browser.set_window_size(1400, 700)
        #self.browser.set_page_load_timeout(self.timeout)
        #self.wait = WebDriverWait(self.browser, self.timeout)
        
    def __del__(self):
        self.browser.close()
    
    def process_request(self, request, spider):
        '''
        用 Chrome 抓取页面
        :param request: Request 对象
        :param spider: Spider 对象
        :return: HtmelResponse 对象
        '''
        if request.url == 'http://cn.changhong.com/':
            self.logger.debug('不用 selenium')
            pass
        else:
            self.browser = webdriver.Firefox()
            self.logger.debug('Chrome is Starting')
            try:
                self.browser.get(request.url)
                #self.browser.implicitly_wait(60)
                time.sleep(10)
                page_source = self.browser.page_source
                self.browser.quit()
                return HtmlResponse(url=request.url, body=page_source, 
                                request=request, encoding='utf-8', status=200)
            
            except TimeoutException:
                self.browser.quit()
                return HtmlResponse(url=request.url, status=500, request=request)
    
    
        