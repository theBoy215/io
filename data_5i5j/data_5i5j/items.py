# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Data5I5JItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    location = scrapy.Field()
    img_url = scrapy.Field()
    price = scrapy.Field()
    unitprice = scrapy.Field()
    tags = scrapy.Field()
    layout = scrapy.Field()
    area = scrapy.Field()
    heading = scrapy.Field()
    decoration = scrapy.Field()
    buildingtype = scrapy.Field()
    floor = scrapy.Field()
    buildyear = scrapy.Field()
    sq = scrapy.Field()
    communityname = scrapy.Field()


class DataZ5I5JItem(scrapy.Item):
    title = scrapy.Field()
    sub_t = scrapy.Field()
    price = scrapy.Field()
    buildingtype = scrapy.Field()
    area = scrapy.Field()
    pays = scrapy.Field()
    communityname = scrapy.Field()
    floor = scrapy.Field()
    heading = scrapy.Field()
    decoration = scrapy.Field()
    sub = scrapy.Field()


class DatalianjiaItem(scrapy.Item):
    title = scrapy.Field()
    sub = scrapy.Field()
    total = scrapy.Field()
    unitprice = scrapy.Field()
    room = scrapy.Field()
    types = scrapy.Field()
    area = scrapy.Field()
    name = scrapy.Field()
    areaName = scrapy.Field()

class DataZlianjiaItem(scrapy.Item):
    title = scrapy.Field()
    tag = scrapy.Field()
    zprice = scrapy.Field()
    types = scrapy.Field()
    area = scrapy.Field()
    threading = scrapy.Field()
    floor = scrapy.Field()
    floors = scrapy.Field()
    areaName = scrapy.Field()
    lift = scrapy.Field()
    coord = scrapy.Field()
    sub_met = scrapy.Field()
    yiy = scrapy.Field()
    bus = scrapy.Field()
    shop = scrapy.Field()
    pry_type = scrapy.Field()
    y_price = scrapy.Field()

class DataZiruItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    meter = scrapy.Field()
    threading = scrapy.Field()
    types = scrapy.Field()
    floor = scrapy.Field()
    sub = scrapy.Field()
    position_x = scrapy.Field()
    position_y = scrapy.Field()
    wj_time = scrapy.Field()
    sd_time = scrapy.Field()
    zgc_time = scrapy.Field()
    xeq_time = scrapy.Field()
    gm_time = scrapy.Field()
    xd_time = scrapy.Field()