# -*- coding: utf-8 -*-
import scrapy
from xcmenpiao.items import XcmenpiaoItem

class MenpiaoSpider(scrapy.Spider):
    name = 'menpiao'
    allowed_domains = ['ctrip.com']
    base_url = "http://piao.ctrip.com/"
    city_list = ["anhui","beijing","chongqing","fujian","gansu","guangdong","guangxi","guizhou","hainan","hebei","henan","heilongjiang","hubei","hunan","jilin","jiangsu","jiangxi","liaoning","neimenggu","ningxia","qinghai","shandong","shanxi","shaanxi","shanghai","sichuan","tianjin","xizang","xinjiang","yunnan","zhejiang","oversea"]
    start_urls = [ base_url + city+"/" for city in city_list]


    def parse(self, response):
        list_url = response.xpath("//div[@class='ticket_bd bd_middle']/dl")[1].xpath("./dt/a/@href").extract_first()
        # print list_url
        yield scrapy.Request(url=list_url,callback = self.parse_list)

    def parse_list(self, response):
        jinqu_list = response.xpath("//div[@class='searchresult_product04']")
        for jinqu in jinqu_list:
            item = XcmenpiaoItem()
            item['score'] = jinqu.xpath() if jinqu.xpath() else None
            item['scenic_name'] = jinqu.xpath() if jinqu.xpath() else None
            item['scenic_addr'] = jinqu.xpath() if jinqu.xpath() else None
            item['introduce'] = jinqu.xpath() if jinqu.xpath() else None
            item['menpiao_list']=list()
            # 判断列表页是否有门票信息 
            btn_chakan = jinqu.xpath()
            if xxxxx:
                for menpiao in menpiao_list:
                    pass
            else:
                yield scrapy.Request(url=,callback=self.parse_detail, meta={'_item': item})
        # 下一页:
        if not response.xpath("//div[@class='pkg_page basefix']/a[@class='down down_nocurrent']/@href"):
            next_url = response.xpath("//div[@class='pkg_page basefix']/a[@class='down']/@href")
            yield scrapy.Request(url=base_url[:-1]+next_url,callback=self.parse_list)

    def parse_detail(self,response):
        item = response.meta.get("_item")
        pass

