# -*- coding: utf-8 -*-
import scrapy
from ..items import DataZlianjiaItem


class ZlianjiaSpider(scrapy.Spider):
    name = 'zlianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['']

    def start_requests(self):
        for i in range(1, 101):
            url = 'https://m.lianjia.com/chuzu/bj/zufang/changping/pg%srt200600000001/?ajax=1' % i
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        detail_url = response.xpath('.//div[@class="content__item"]/a/@href').extract()
        for i in detail_url:
            url = response.urljoin(i)
            yield scrapy.Request(url=url, callback=self.detail_content)

    def detail_content(self, response):
        item = DataZlianjiaItem()
        title = response.xpath('.//h2[@class="page-title-h2"]/text()').extract_first()
        item['title'] = title
        tag = response.xpath('.//p[@class="content__item__tag--wrapper"]//text()').extract()
        new_tag = ''
        for i in tag:
            new_tag += i.strip()
            new_tag += ' '
        item['tag'] = new_tag
        zprice = response.xpath('.//div[@class="box content__detail--info"]/ul/li[1]/span[2]/text()').extract_first()
        item['zprice'] = zprice
        types = response.xpath('.//div[@class="box content__detail--info"]/ul/li[2]/span[2]/text()').extract_first()
        item['types'] = types.strip()
        area = response.xpath('.//div[@class="box content__detail--info"]/ul/li[3]/span[2]/text()').extract_first()
        item['area'] = area
        threading = title.split(' ')[2]
        item['threading'] = threading
        floor = response.xpath('.//li[@class="oneline"][4]/span/text()').extract_first()
        item['floor'] = floor
        floors = floor.split('/')[1]
        item['floors'] = floors
        areaName = response.xpath('.//p[@class="resblock"]/a/text()').extract_first()
        item['areaName'] = areaName.strip()
        lift = response.xpath('.//li[@class="oneline"][5]/span/text()').extract_first()
        item['lift'] = lift
        coord = response.xpath('.//a[@class="map--container"]/@href').extract_first()
        item['coord'] = coord.split('=')[1]
        sub_met = response.xpath('.//ul[@class="box page-map-list"]/li[1]/span[@class="fr"][1]/text()').extract_first()
        item['sub_met'] = sub_met
        div_li = response.xpath('.//div[@class="box detail"]/a/text()').extract_first()
        item['yiy'] = 0
        item['bus'] = 0
        item['shop'] = 0
        if div_li:
            try:
                if '医院' in div_li:
                    item['yiy'] = 1
            except:
                pass

            try:
                if '公交' in div_li:
                    item['bus'] = 1
            except:
                pass

            try:
                if '超市' in div_li:
                    item['shop'] = 1
            except:
                pass

        pry_type = response.xpath('.//td[@class="cost-name"]/text()').extract_first()
        item['pry_type'] = pry_type
        y_price = response.xpath('.//td[@class="td-right"]/text()').extract_first()
        item['y_price'] = y_price
        print(item)
        yield item
