# -*- coding: utf-8 -*-
import scrapy
from live.items import LiveItem
from scrapy.contrib.loader import ItemLoader


class yyjdqscjzcSpider(scrapy.Spider):
    name = 'yy_jdqscjzc'

    def start_requests(self):
        start_urls = ['http://www.yy.com/chicken/cjzc']

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = ItemLoader(item=LiveItem(),response=response)
        for content in response.xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/ul/li/a'):
                i = ItemLoader(item=LiveItem(),selector=content)
                #标题
                i.add_xpath('title','span[3]/text()')
                #用户名
                i.add_xpath('username','span[5]/text()')
                #热度
                i.add_xpath('num','span[2]/text()')
                #图片的地址
                i.add_xpath('pic_addr','span[1]/span[1]/img/@data-original')
                #直播间的相对地址
                i.add_xpath('addr','@href')
                #直播平台
                i.add_value('platform','yy')
                yield i.load_item()
            

    
