# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XcmenpiaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 景区名
    scenic_name = scrapy.Field()
    # 景区地址
    scenic_addr = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 特色
    introduce = scrapy.Field()
    # 门票信息 list
    menpiao_list = scrapy.Field()
 	# 数据源
    source = scrapy.Field()
    # utc时间
    utc_time = scrapy.Field()
