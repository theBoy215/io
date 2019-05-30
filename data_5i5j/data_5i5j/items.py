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
    price = scrapy.Field()
    unitprice = scrapy.Field()
    s = scrapy.Field()
    t = scrapy.Field()
    area = scrapy.Field()
    threading = scrapy.Field()
    floor = scrapy.Field()
    floors = scrapy.Field()
    lift = scrapy.Field()
    areaName = scrapy.Field()
    sub_met = scrapy.Field()
    coord_x = scrapy.Field()
    coord_y = scrapy.Field()

class DataZlianjiaItem(scrapy.Item):
    title = scrapy.Field()
    tag = scrapy.Field()
    zprice = scrapy.Field()
    type_s = scrapy.Field()
    type_t = scrapy.Field()
    type_w = scrapy.Field()
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
    type_s = scrapy.Field()
    type_t = scrapy.Field()
    floor = scrapy.Field()
    floors = scrapy.Field()
    sub = scrapy.Field()
    position_x = scrapy.Field()
    position_y = scrapy.Field()
    wj_time = scrapy.Field()
    sd_time = scrapy.Field()
    zgc_time = scrapy.Field()
    xeq_time = scrapy.Field()
    gm_time = scrapy.Field()
    xd_time = scrapy.Field()


class DataCjLianJiaItem(scrapy.Item):
    title = scrapy.Field()
    gptime = scrapy.Field()
    cjtime = scrapy.Field()
    gprice = scrapy.Field()
    cjprice = scrapy.Field()
    dprice = scrapy.Field()
    zq = scrapy.Field()
    tj = scrapy.Field()
    watch = scrapy.Field()
    gz = scrapy.Field()
    ll = scrapy.Field()
    type_s = scrapy.Field()
    type_t = scrapy.Field()
    type_c = scrapy.Field()
    type_w = scrapy.Field()
    floor = scrapy.Field()
    floors = scrapy.Field()
    area = scrapy.Field()
    threading = scrapy.Field()
    year = scrapy.Field()
    decoration = scrapy.Field()
    lift = scrapy.Field()
    coord_x = scrapy.Field()
    coord_y = scrapy.Field()
    name = scrapy.Field()


