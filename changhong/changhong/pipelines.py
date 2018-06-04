# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class ChanghongPipeline(object):
    
    def __init__(self):
        with open("changhong.csv", "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["系列",
                             "名称",
                             "价格"])
    
    def process_item(self, item, spider):
        with open("changhong.csv", "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([item["series"],
                             item["detail_name"],
                             item["price"]])
                             
        return item
