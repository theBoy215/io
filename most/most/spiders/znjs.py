# -*- coding: utf-8 -*-
import scrapy
from ..items import MostItem


class ZnjsSpider(scrapy.Spider):
    name = 'znjs'
    allowed_domains = ['znjs.most.gov.cn']

    # start_urls = ['http://znjs.most.gov.cn/wasdemo/search']

    def start_requests(self):
        for i in range(1, 4):
            yield scrapy.FormRequest(
                url='http://znjs.most.gov.cn/wasdemo/search',
                formdata={
                    'channelid': '44374',
                    'searchword': '省部共建国家重点实验室名单',
                    'sortfield': '-DOCRELTIME',
                    'prepage': '10',
                    'page': str(i),
                },
                callback=self.parse
            )

    def parse(self, response):
        a_list = response.xpath('.//td[@width="530"]/a/@href').extract()
        for i in a_list:
            yield scrapy.Request(url=i, callback=self.get_data, dont_filter=True)

    def get_data(self, response):
        most = MostItem()
        data_title = response.xpath('.//div[@id="Title"]/text()').extract_first()
        if data_title:
            most['title'] = data_title
        else:
            most['title'] = 'NULL'
        data_time = response.xpath('.//td[@width="250"][last()]/text()').extract_first()
        if data_time:
            most['time'] = data_time[-4:]
        else:
            most['time'] = 'NULL'
        p_text = response.xpath('.//p[@target="_self"]/a/@href').extract_first()
        if p_text:
            most['name_text'] = 'NULL'
            most['director_text'] = 'NULL'
            most['unit_text'] = 'NULL'
            most['sector_text'] = 'NULL'
            most['addr'] = response.urljoin(p_text)
            yield most
        else:
            name_text = response.xpath('.//table[@align="center"]/tbody/tr[2]/td[1]/p//text()').extract()
            dir_text = response.xpath('.//table[@align="center"]/tbody/tr[2]/td[2]/p//text()').extract()
            unit_text = response.xpath('.//table[@align="center"]/tbody/tr[2]/td[3]/p//text()').extract()
            sector_text = response.xpath('.//table[@align="center"]/tbody/tr[2]/td[4]/p//text()').extract()

            if name_text:
                most['name_text'] = ''.join(''.join(name_text).split())
            else:
                most['name_text'] = 'NULL'
            if dir_text:
                most['director_text'] = ''.join(''.join(dir_text).split())
            else:
                most['director_text'] = 'NULL'
            if unit_text:
                most['unit_text'] = ''.join(''.join(unit_text).split())
            else:
                most['unit_text'] = 'NULL'
            if sector_text:
                most['sector_text'] = ''.join(''.join(sector_text).split())
            else:
                most['sector_text'] = 'NULL'
            most['addr'] = 'NULL'
            yield most
