#encoding=utf-8
import  scrapy

class ZxlhdSpider(scrapy.Spider):
    name = "zxlhd"

    def start_requests(self):
        urls = [
#            'https://www.douyu.com/directory/game/jdqscjzc',
#            'https://www.douyu.com/directory/game/LOL',
#            'https://www.douyu.com/directory/game/DOTA2',
#            'https://www.douyu.com/directory/game/blzy',
#            'https://www.douyu.com/directory/game/TVgame',
            'https://www.douyu.com/directory/game/Overwatch'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #page = response.url.split("/")[-1]
        #filename = 'quotes-%s.html' % page
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #self.log('Saved file %s' % filename)
        for content in response.xpath('//*[@id="live-list-contentbox"]/li/a'):
            yield{
                #标题
                'title': content.xpath('div/div/h3/text()').extract_first().strip(),
                #用户名
                'username':content.xpath('div[1]/p/span[1]/text()').extract_first(),  
                #热度
                'num':content.xpath('div[1]/p/span[2]/text()').extract_first(),  
                #图片的地址
                'pic_addr':content.xpath('span/img/@data-original').extract_first(), 
                #直播间的相对地址
                'addr':content.xpath('@href').extract_first() 

            }
