# -*- coding: utf-8 -*-
import scrapy
from changhong.items import ChanghongItem

class ProductSpiderSpider(scrapy.Spider):
    name = 'product_spider'
    allowed_domains = ['cn.changhong.com']
    start_urls = ['http://cn.changhong.com/']

    def parse(self, response):
        subs = response.xpath('//div[@class="inner-pro-list"]') # 21 results
        for sub in subs:
            next_link = sub.xpath('./a/@href').extract()[0] # product link
            yield scrapy.Request(next_link, callback=self.parse_product)
    
    def parse_product(self, response):
        subs = response.xpath('//div[@class="pro-goods"]') # 8 results but maybe 0
        if subs is not None:
            item = ChanghongItem()
            for sub in subs:
                item['series'] = response.xpath('//head/title/text()').extract()[0]
                item['detail_name'] = sub.xpath('./div[@class="pro-goods-text"]/h1/a/text()').extract()[0]
                item['price'] = sub.xpath('./div[@class="pro-goods-text"]/p/span/text()').extract()[0]
                yield item
            next_page = response.xpath('//div[@id="fenye"]/a[@class="next-page"]/@href').extract()
            if next_page is not None:
                yield scrapy.Request(next_page[0], callback=self.parse_product)
    