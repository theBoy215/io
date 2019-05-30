# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import DataHouseItem


class AnjukSpider(scrapy.Spider):
    name = 'anjuk'
    allowed_domains = ['anjuke.com']
    start_urls = ['']

    def start_requests(self):
        for i in range(1, 51):
            url = 'https://langfang.anjuke.com/sale/sanheyuao/a477-b393-m523-p%d/#filtersort' % i
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        detail_url = response.xpath('.//div[@class="house-title"]/a/@href').extract()
        for detail in detail_url:
            yield scrapy.Request(url=detail, callback=self.detail_data, dont_filter=True)

    def detail_data(self, response):
        item = DataHouseItem()
        price = response.xpath('.//span[@class="light info-tag"]/em/text()').extract_first()
        item['price'] = price

        meter = response.xpath('.//span[@class="info-tag"]/em/text()').extract()
        item['meter'] = meter[2]

        sprice = response.xpath('.//div[@class="houseInfo-content"]/text()').extract()
        sprice = re.sub(' 元/m²', '', sprice[3])
        item['sprice'] = sprice

        pos_ls = response.xpath('.//meta[@name="location"]/@content').extract_first()
        pos = re.findall(r'coord=(.*)', pos_ls)[0]
        pos_x = pos.split(',')[0]
        item['pos_x'] = pos_x
        pos_y = pos.split(',')[1]
        item['pos_y'] = pos_y
        print(item)
        yield item
