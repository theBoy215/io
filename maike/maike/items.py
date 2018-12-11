# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaikeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    classes = scrapy.Field()
    titles = scrapy.Field()
    location = scrapy.Field()
    age = scrapy.Field()
    deceased = scrapy.Field()
    area = scrapy.Field()
    affi = scrapy.Field()
