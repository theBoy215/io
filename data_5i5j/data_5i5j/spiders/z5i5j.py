# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy_redis.spiders import RedisSpider
from ..items import DataZ5I5JItem


class Z5i5jSpider(RedisSpider):
    name = 'z5i5j'

    # allowed_domains = ['bj.5i5j.com']
    # redis_key = 'z5i5j:start_urls'
    # start_urls = ['https://bj.5i5j.com/zufang/changpingqu/u1/']

    # def start_requests(self):
    #     yield scrapy.Request(url='https://bj.5i5j.com/zufang/changpingqu/u1/', callback=self.parse,
    #                          dont_filter=True)

    def parse(self, response):
        for i in range(1, 45):  # 45
            url = 'https://bj.5i5j.com/zufang/changpingqu/u1n%d/?wscckey=b25733a4d3d6b723_1547370286' % i
            # url = 'https://bj.5i5j.com/zufang/changpingqu/u2n%d/' % i
            yield scrapy.Request(url, callback=self.next_data, dont_filter=True)

    def next_data(self, response):
        title = response.xpath('.//h3[@class="listTit"]/a/text()').extract()
        detail = response.xpath('.//h3[@class="listTit"]/a/@href').extract()
        house_li = response.xpath('.//div[@class="listX"]/p[1]/text()').extract()
        price = response.xpath('.//p[@class="redC"]/strong/text()').extract()
        communityname = response.xpath('.//div[@class="listX"]/p[2]/a/text()').extract()
        tit = ''
        houses = ''
        name = ''
        pr = ''
        for i in range(len(detail)):
            if title[i]:
                tit = title[i]
            if house_li[i]:
                houses = house_li[i]
            if communityname[i]:
                name = communityname[i]
            if price[i]:
                pr = price[i]
            new_url = response.urljoin(detail[i])
            yield scrapy.Request(url=new_url,
                                 meta={
                                     'title': tit,
                                     'house_li': houses,
                                     'communityname': name,
                                     'pr': pr},
                                 callback=self.data,
                                 dont_filter=True)

    def data(self, response):
        item = DataZ5I5JItem()
        house_li = response.meta['house_li']
        if house_li:
            hs = house_li.split('·')
        else:
            hs = []

        try:
            item['buildingtype'] = ''.join(re.sub(r'[\s\r\t\n]+', '', hs[0]))
        except:
            item['buildingtype'] = 'NULL'

        try:
            item['area'] = ''.join(re.sub(r'[\s\r\t\n]+', '', hs[1]))
        except:
            item['area'] = 'NULL'

        try:
            item['heading'] = hs[2].strip()
        except:
            item['heading'] = 'NULL'

        try:
            item['floor'] = hs[3].strip()
        except:
            item['floor'] = 'NULL'

        try:
            item['decoration'] = hs[4].strip()
        except:
            item['decoration'] = 'NULL'

        sub = response.xpath('.//div[@class="zushous"]/ul/li[@class="traffic"]/text()').extract_first()
        if sub:
            item['sub'] = ''.join(sub)
        else:
            item['sub'] = 'NULL'

        communityname = response.meta['communityname']
        if communityname:
            item['communityname'] = communityname
        else:
            item['communityname'] = 'NULL'

        title = response.meta['title']
        if title:
            item['title'] = title
        else:
            item['title'] = 'NULL'

        sub_t = response.xpath('.//div[@class="rent-top fl"]/p/text()').extract()
        if sub_t:
            item['sub_t'] = ''.join(sub_t)
        else:
            item['sub_t'] = 'NULL'

        price = response.meta['pr']
        if price:
            item['price'] = price
        else:
            item['price'] = 'NULL'

        pay = response.xpath(
            './/div[@class="jlyoubai fl "]/div[@class="jlquannei fonthongse"]/p[@class="jlinfo font18"]/text()').extract_first()
        if pay:
            item['pays'] = pay
        else:
            item['pays'] = 'NULL'

        print(item)
        import time
        time.sleep(2)
        yield item
