# -*- coding: utf-8 -*-
import scrapy
from ..items import DatalianjiaItem
import re


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['bj.lianjia.com']
    start_urls = ['']

    def start_requests(self):
        for i in range(1, 101):
            yield scrapy.Request(url='https://m.lianjia.com/bj/ershoufang/yanqing/pg%s/' % i,
                                 callback=self.parse, dont_filter=True)

    def parse(self, response):
        detail_url = response.xpath('.//li[@class="pictext"]/a/@href').extract()
        for j in range(len(detail_url)):
            yield scrapy.Request(url=response.urljoin(detail_url[j]), callback=self.detail_data, dont_filter=True)

    def detail_data(self, response):

        item = DatalianjiaItem()
        title = response.xpath('.//h3[@class="house_desc lazyload_ulog"]/text()').extract_first()
        title = title.strip()
        item['title'] = title

        price = response.xpath('.//div[@class="similar_data_detail"]//span[@data-mark="price"]/text()').extract_first()
        price = re.sub('[^\d]', '', price)
        item['price'] = price

        unitprice = response.xpath('.//li[@class="short"]/text()').extract_first()
        unitprice = re.sub('[^\d]', '', unitprice)
        item['unitprice'] = unitprice

        types = response.xpath('.//div[@class="similar_data_detail"]/p[2]/text()').extract_first()
        new_types = re.sub('厅', '', types)
        s = new_types.split('室')[0]
        t = new_types.split('室')[1]
        item['s'] = s
        item['t'] = t

        area = response.xpath('.//div[@class="similar_data_detail"]/p[@class="red big"]/text()').extract()
        area = area[1]
        area = re.sub('m²', '', area)
        item['area'] = area

        threading = response.xpath('.//li[@class="short"][3]/text()').extract_first()
        threading = threading.strip()
        item['threading'] = threading

        floor_ls = response.xpath('.//li[@class="short"][4]/text()').extract_first()
        floor = floor_ls.split('/')[0]
        floors = floor_ls.split('/')[1]
        item['floor'] = floor
        item['floors'] = floors

        lift = response.xpath('.//li[@class="short"][6]/text()').extract_first()
        item['lift'] = lift

        areaName = response.xpath('.//li[@class="long  arrow "]/a/text()').extract_first()
        item['areaName'] = areaName

        sub_met = response.xpath('.//div[@class="mod_cont"]/p[@class="small gray"]/text()').extract_first()
        if sub_met:
            sub_met = sub_met.strip()
            sub_met = re.sub('[^\d]', '', sub_met[7:])
        item['sub_met'] = sub_met

        coords = response.xpath('.//div[@class="mod_cont"]/a[@class="post_ulog"]/img/@src').extract_first()
        coords = re.findall('center=(.*)&width', coords)
        coord_x = coords[0].split(',')[0]
        coord_y = coords[0].split(',')[1]
        item['coord_x'] = coord_x
        item['coord_y'] = coord_y

        print(item)
        yield item
