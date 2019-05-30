# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DataHouseItem(scrapy.Item):
    # define the fields for your item here like:
    price = scrapy.Field()
    sprice = scrapy.Field()
    meter = scrapy.Field()
    pos_x = scrapy.Field()
    pos_y = scrapy.Field()