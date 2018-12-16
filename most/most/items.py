# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MostItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    name_text = scrapy.Field()
    director_text = scrapy.Field()
    unit_text = scrapy.Field()
    sector_text = scrapy.Field()
    addr = scrapy.Field()
