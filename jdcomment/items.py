# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdcommentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    commen_type = scrapy.Field()
    id = scrapy.Field()
    guid = scrapy.Field()
    content = scrapy.Field()
    creationTime = scrapy.Field()
    isDelete = scrapy.Field()
    name = scrapy.Field()
    isTop = scrapy.Field()
    userImageUrl = scrapy.Field()
    topped = scrapy.Field()
