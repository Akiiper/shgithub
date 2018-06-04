# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class TencentVideoPipeline(object):
    
    def __init__(self):
        with open("tencent-video.csv", "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["电视剧", "豆瓣评分"])
    
    def process_item(self, item, spider):
        video_name = item['video_name']
        douban_score = item['douban_score']
        with open("tencent-video.csv", "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([video_name, douban_score])
        return item
