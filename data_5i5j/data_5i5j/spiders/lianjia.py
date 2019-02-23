# -*- coding: utf-8 -*-
import scrapy
from ..items import DatalianjiaItem
import re


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['bj.lianjia.com']
    start_urls = ['']

    def start_requests(self):
        yield scrapy.Request(url='https://bj.lianjia.com/ershoufang/rs久长花园/',
                             callback=self.next_data, dont_filter=True)

    def next_data(self, response):
        for i in range(1, 3):
            next_url = response.xpath('.//div[@class="page-box house-lst-page-box"]/@page-url').extract_first()
            new_next_url = re.sub(r'{page}', str(i), next_url)
            new_url = response.urljoin(new_next_url)
            yield scrapy.Request(url=new_url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        detail_url = response.xpath('.//a[@class="img"]/@href').extract()
        for j in range(len(detail_url)):
            yield scrapy.Request(url=detail_url[j], callback=self.detail_data, dont_filter=True)

    def detail_data(self, response):
        item = DatalianjiaItem()
        title = response.xpath('.//h1[@class="main"]/text()').extract_first()
        if title:
            item['title'] = title
        else:
            item['title'] = 'NULL'

        sub_title = response.xpath('.//div[@class="sub"]/text()').extract_first()
        if sub_title:
            item['sub'] = sub_title
        else:
            item['sub'] = 'NULL'

        tl = response.xpath('.//div[@class="price "]/span[@class="total"]/text()').extract_first()
        bit = response.xpath('.//div[@class="price "]/span[@class="unit"]/span/text()').extract_first()
        total = tl + bit
        if total:
            item['total'] = total
        else:
            item['total'] = 'NULL'

        unitprice = response.xpath('.//span[@class="unitPriceValue"]//text()').extract()
        unitprice = ''.join(unitprice)
        if unitprice:
            item['unitprice'] = unitprice
        else:
            item['unitprice'] = 'NULL'

        room = response.xpath('.//div[@class="room"]//text()').extract()
        room = ' '.join(room)
        if room:
            item['room'] = room
        else:
            item['room'] = 'NULL'

        types = response.xpath('.//div[@class="houseInfo"]/div[@class="type"]//text()').extract()
        types = ' '.join(types)
        if type:
            item['types'] = types
        else:
            item['types'] = 'NULL'

        area = response.xpath('.//div[@class="area"]//text()').extract()
        area = ' '.join(area)
        if area:
            item['area'] = area
        else:
            item['area'] = 'NULL'

        name = response.xpath('.//div[@class="communityName"]/a[1]/text()').extract_first()
        if name:
            item['name'] = name
        else:
            item['name'] = 'NULL'

        areaName = response.xpath('.//div[@class="areaName"]/span[@class="info"]//text()').extract()
        areaName = ''.join(areaName)
        areaName = re.sub(r'\xa0', '', areaName)
        subName = response.xpath('.//a[@class="supplement"]/text()').extract_first()
        if subName:
            areaName = areaName + ' ' + subName
        if areaName:
            item['areaName'] = areaName
        else:
            item['areaName'] = 'NULL'

        text = response.xpath('.//div[@class="transaction"]/div[@class="content"]/ul/li[2]/span[2]/text()').extract_first()
        # print(text)
        # if text == '限价商品房':
        print(item)
        yield item

