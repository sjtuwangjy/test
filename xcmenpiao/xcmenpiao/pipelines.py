# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter
from datetime import datetime

class XcmenpiaoPipeline(object):
    def process_item(self, item, spider):
        item["source"] = spider.name
        item["utc_time"] = str(datetime.utcnow())
        return item


class XcmenpiaoCsvPipeline(object):
    def open_spider(self, spider):
        self.filename = open("xcmenpiao.csv", "w")
        self.csv_exporter = CsvItemExporter(self.filename)
        self.csv_exporter.start_exporting()

    def process_item(self, item, spider):
        self.csv_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.csv_exporter.finish_exporting()
        self.filename.close()