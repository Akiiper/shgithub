# -*- coding: utf-8 -*-
import scrapy
from tencent_video.items import TencentVideoItem

'''
爬取腾讯视频网站上的最受好评的电视剧,
网址:http://v.qq.com/x/list/tv?offset=0&sort=16,
爬取的内容包括电视剧名字, 豆瓣评分
'''

class VideoSpiderSpider(scrapy.Spider):
    name = 'video_spider'
    allowed_domains = ['v.qq.com']
    start_urls = ["http://v.qq.com/x/list/tv?offset=0&sort=16"]

    def parse(self, response):
        subselect = response.xpath('//div[@class="figure_title_score"]')
        items = []
        for sub in subselect:
            item = TencentVideoItem()
            item['video_name'] = sub.xpath('./strong/a/text()').extract()[0]
            item['douban_score'] = sub.xpath('./div/em[@class="score_l"]/text()').extract()[0] + \
            sub.xpath('./div/em[@class="score_s"]/text()').extract()[0]
            items.append(item)
        return items
