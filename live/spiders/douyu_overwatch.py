# -*- coding: utf-8 -*-
import scrapy


class DouyuOverwatchSpider(scrapy.Spider):
    name = 'douyu_overwatch'
    allowed_domains = ['https://www.douyu.com/directory/game/Overwatch']
    start_urls = ['http://https://www.douyu.com/directory/game/Overwatch/']

    def start_requests(self):
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #page = response.url.split("/")[-1]
        #filename = 'quotes-%s.html' % page
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #self.log('Saved file %s' % filename)
        
        items = ItemLoader(item=LiveItem(),response=response)
        for content in response.xpath('//*[@id="live-list-contentbox"]/li/a'):
                i = ItemLoader(item=LiveItem(),selector=content)
                #标题
                i.add_xpath('title','div/div/h3/text()')
                #'title': content.xpath('div/div/h3/text()').extract_first().strip(),
                #用户名
                i.add_xpath('username','div[1]/p/span[1]/text()')
                #'username':content.xpath('div[1]/p/span[1]/text()').extract_first(),  
                #热度
                i.add_xpath('num','div[1]/p/span[2]/text()')
                #'num':content.xpath('div[1]/p/span[2]/text()').extract_first(),  
                #图片的地址
                i.add_xpath('pic_addr','span/img/@data-original')
                #'pic_addr':content.xpath('span/img/@data-original').extract_first(), 
                #直播间的相对地址
                i.add_xpath('addr','@href')
                #'addr':content.xpath('@href').extract_first() 
                yield i.load_item()
            

    
