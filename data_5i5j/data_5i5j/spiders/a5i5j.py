# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import Data5I5JItem


class A5i5jSpider(scrapy.Spider):
    name = '5i5j'
    allowed_domains = ['5i5j.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/changping/bp0ep100000ba0ea20000dp1/?noStatic=1']

    # def start_requests(self):
    #     # for i in range(1, 104):
    #         # url = 'https://bj.5i5j.com/map/ajax/location/sale?onMove=false&locationId=100000802&locationLevel=3&bounds={"e":116.735537,"w":116.541215,"s":40.304966,"n":40.340171}&boundsLevel=4&pageSize=20&page=%d' % i
    #         # url = 'https://bj.5i5j.com/map/ajax/location/sale?onMove=false&locationId=100000801&locationLevel=3&bounds={"e":117.227272,"w":117.03295,"s":40.132405,"n":40.164171}&boundsLevel=4&pageSize=20&page=%d' % i
    #         # url = 'https://bj.5i5j.com/map/ajax/location/sale?onMove=false&locationId=1010&locationLevel=3&bounds={"e":116.755407,"w":116.561373,"s":40.11981,"n":40.146068}&boundsLevel=4&pageSize=20&page=%d' % i
    #           yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        print(response.url)
        json_data = json.loads(response.text)
        for i in json_data['data']['res']['houses']['list']:
            hid = i['id']
            title = i['title']
            location_x, location_y = i['location'][0], i['location'][1]
            img_url = i['img_url']
            yield scrapy.FormRequest(url='https://appapi.5i5j.com/appapi/vr/1/v1/supportdata',
                                     formdata={'houseid': str(hid)},
                                     meta={'title': title, 'location': (location_x, location_y), 'img_url': img_url},
                                     callback=self.detail_data)

    def detail_data(self, response):
        item = Data5I5JItem()
        title = response.meta['title']
        if title:
            item['title'] = title
        else:
            item['title'] = 'NULL'

        location = response.meta['location']
        if location:
            item['location'] = str(location)
        else:
            item['location'] = ()

        img_url = response.meta['img_url']
        if img_url:
            item['img_url'] = img_url
        else:
            item['img_url'] = 'NULL'

        detail_json_data = json.loads(response.text)

        price = detail_json_data['data']['houseInfo']['price']
        if price:
            item['price'] = price
        else:
            item['price'] = 'NULL'

        unitprice = detail_json_data['data']['houseInfo']['unitprice']
        if unitprice:
            item['unitprice'] = unitprice
        else:
            item['unitprice'] = 'NULL'

        tags = detail_json_data['data']['houseInfo']['tags']
        if tags:
            item['tags'] = tags
        else:
            item['tags'] = 'NULL'

        layout = detail_json_data['data']['houseInfo']['layout']
        if layout:
            item['layout'] = layout
        else:
            item['layout'] = 'NULL'

        area = detail_json_data['data']['houseInfo']['area']
        if area:
            item['area'] = area
        else:
            item['area'] = 'NULL'

        heading = detail_json_data['data']['houseInfo']['heading']
        if heading:
            item['heading'] = heading
        else:
            item['heading'] = 'NULL'

        decoration = detail_json_data['data']['houseInfo']['decoration']
        if decoration:
            item['decoration'] = decoration
        else:
            item['decoration'] = 'NULL'

        buildingtype = detail_json_data['data']['houseInfo']['buildingtype']
        if buildingtype:
            item['buildingtype'] = buildingtype
        else:
            item['buildingtype'] = 'NULL'

        floor = detail_json_data['data']['houseInfo']['floor']
        if floor:
            item['floor'] = floor
        else:
            item['floor'] = 'NULL'

        buildyear = detail_json_data['data']['houseInfo']['buildyear']
        if buildyear:
            item['buildyear'] = buildyear
        else:
            item['buildyear'] = 'NULL'

        sq = detail_json_data['data']['houseInfo']['sq']
        if sq:
            item['sq'] = sq
        else:
            item['sq'] = 'NULL'

        communityname = detail_json_data['data']['houseInfo']['communityname']
        if communityname:
            item['communityname'] = communityname
        else:
            item['communityname'] = 'NULL'
        print(item)
        yield item
