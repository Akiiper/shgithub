# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChanghongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    series = scrapy.Field() # 产品系列
    detail_name = scrapy.Field() # 产品名称
    price = scrapy.Field() # 价格
