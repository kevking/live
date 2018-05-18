# -*- coding: utf-8 -*-
import scrapy
from live.items import LiveItem
from scrapy.contrib.loader import ItemLoader


class PandaTVgameSpider(scrapy.Spider):
    name = 'panda_TVgame'

    def start_requests(self):
        start_urls = ['https://www.panda.tv/cate/TVgame']

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = ItemLoader(item=LiveItem(),response=response)
        for content in response.xpath('//*[@id="sortdetail-container"]/li/a'):
                i = ItemLoader(item=LiveItem(),selector=content)
                #标题
                i.add_xpath('title','div[2]/span[1]/text()')
                #用户名
                i.add_xpath('username','div[2]/span[2]/@title')
                #热度
                i.add_xpath('num','div[2]/span[4]/i/text()')
                #图片的地址
                i.add_xpath('pic_addr','div[1]/img/@data-original')
                #直播间的相对地址
                i.add_xpath('addr','@href')
                #直播平台
                i.add_value('platform','panda')
                yield i.load_item()
            

    
