# -*- coding: utf-8 -*-
import scrapy
from live.items import LiveItem
from scrapy.contrib.loader import ItemLoader


class DouyuOverwatchSpider(scrapy.Spider):
    name = 'douyu_wzry'

    def start_requests(self):
        start_urls = ['https://www.douyu.com/directory/game/wzry/']
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = ItemLoader(item=LiveItem(),response=response)
        for content in response.xpath('//*[@id="live-list-contentbox"]/li/a'):
                i = ItemLoader(item=LiveItem(),selector=content)
                #标题
                i.add_xpath('title','div/div/h3/text()')
                #用户名
                i.add_xpath('username','div[1]/p/span[1]/text()')
                #热度
                i.add_xpath('num','div[1]/p/span[2]/text()')
                #图片的地址
                i.add_xpath('pic_addr','span/img/@data-original')
                #直播间的相对地址
                i.add_xpath('addr','@href')
                #直播平台
                i.add_value('platform','douyu')
                yield i.load_item()
            

    
