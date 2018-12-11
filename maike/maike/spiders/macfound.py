# -*- coding: utf-8 -*-
import scrapy
from ..items import MaikeItem


class MacfoundSpider(scrapy.Spider):
    name = 'macfound'
    allowed_domains = ['macfound.org']
    start_urls = ['https://www.macfound.org/fellows/search/all?page=1#fellows-search']

    def parse(self, response):
        href_list = response.xpath('.//div[@class="layout-flexbox layout-flexbox__columns--four"]/a/@href').extract()
        li_next = response.xpath('.//li[@class="pager__item pager__item--next"]/a/@href').extract_first()
        for i in href_list:
            new_a = response.urljoin(i)
            yield scrapy.Request(url=new_a, callback=self.get_data)
        if li_next:
            new_url = response.urljoin(li_next)
            self.start_urls.append(new_url)
            yield scrapy.Request(url=new_url, callback=self.parse)

    def get_data(self, response):
        items = MaikeItem()
        ###姓名
        winner = response.xpath('.//h1[@class="content-block__title has-top-margin"]/text()').extract_first()
        items['name'] = winner
        ###年级
        classes = response.xpath('.//h2[@class="content-block__subtitle has-top-margin"]/a/text()').extract_first()
        items['classes'] = classes
        ###详情页内容
        div_text = response.xpath('.//div[@class="photo-bio__content"]//text()').extract()
        new_div = []
        for i in range(len(div_text)):
            strs = div_text[i].strip()
            if strs != '':
                new_div.append(strs)
        new_text = []
        for i in range(len(new_div)):
            if new_div[i] == 'Website':
                break
            new_text.append(new_div[i])

        titles = 'NULL'
        location = 'NULL'
        age = 'NULL'
        deceased = 'NULL'
        area = 'NULL'
        affiliation = 'NULL'
        for index in range(len(new_text)):
            if new_text[index] == 'Title':
                titles = new_text[index + 1]
            items['titles'] = titles

            if new_text[index] == 'Location':
                location = new_text[index + 1]
            items['location'] = location

            if new_text[index] == 'Age':
                age = new_text[index + 1]
            items['age'] = age

            if new_text[index] == 'Deceased':
                deceased = new_text[index + 1]
            items['deceased'] = deceased

            if new_text[index] == 'Area of Focus':
                area = ''.join(new_text[index + 1:])
            items['area'] = area

            if new_text[index] == 'Affiliation':
                affiliation = new_text[index + 1]
            items['affi'] = affiliation
        print(items)
        yield items
