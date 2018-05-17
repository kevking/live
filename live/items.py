# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose

class LiveItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field(
        input_processor = MapCompose(lambda x:x.strip())
    )
    username = scrapy.Field()
    num = scrapy.Field()
    pic_addr = scrapy.Field()
    addr = scrapy.Field()
