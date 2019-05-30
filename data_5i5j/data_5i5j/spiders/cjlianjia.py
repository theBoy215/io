# -*- coding: utf-8 -*-
from ..items import DataCjLianJiaItem
import scrapy
import re
import time


class CjlianjiaSpider(scrapy.Spider):
    name = 'cjlianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['']

    def start_requests(self):
        for i in range(1, 101):
            url = 'https://bj.lianjia.com/chengjiao/xicheng/pg%d/a2p8/' % i
            yield scrapy.Request(url, callback=self.parse)
            time.sleep(0.1)

    def parse(self, response):
        ls_a = response.xpath('.//div[@class="title"]/a/@href').extract()
        for a in ls_a:
            yield scrapy.Request(url=a, callback=self.detail)
            time.sleep(0.1)

    def detail(self, response):
        item = DataCjLianJiaItem()
        title = response.xpath('.//div[@class="wrapper"]/text()').extract_first()
        item['title'] = title.strip()  # 标题
        gptime = response.xpath('.//div[@class="transaction"]/div[@class="content"]/ul/li[3]/text()').extract_first()
        item['gptime'] = gptime.strip()  # 挂牌时间
        cjtime = response.xpath('.//div[@class="wrapper"]/span/text()').extract_first()
        cjtime = re.sub('\s|成交', '', cjtime)
        item['cjtime'] = cjtime  # 成交时间
        cjprice = response.xpath('.//span[@class="dealTotalPrice"]/i/text()').extract_first()
        item['cjprice'] = cjprice  # 成交价格
        dprice = response.xpath('.//div[@class="price"]/b/text()').extract_first()
        item['dprice'] = dprice  # 单价
        gprice = response.xpath('.//div[@class="msg"]/span[1]/label/text()').extract_first()
        item['gprice'] = gprice  # 挂牌价格
        zq = response.xpath('.//div[@class="msg"]/span[2]/label/text()').extract_first()
        item['zq'] = zq  # 成交周期
        tj = response.xpath('.//div[@class="msg"]/span[3]/label/text()').extract_first()
        item['tj'] = tj  # 调价
        watch = response.xpath('.//div[@class="msg"]/span[4]/label/text()').extract_first()
        item['watch'] = watch  # 带看次数
        gz = response.xpath('.//div[@class="msg"]/span[5]/label/text()').extract_first()
        item['gz'] = gz  # 关注人数
        ll = response.xpath('.//div[@class="msg"]/span[6]/label/text()').extract_first()
        item['ll'] = ll  # 浏览次数
        type_ls = response.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[1]/text()').extract_first()
        type_ls = re.split(r'[^\d]', type_ls.strip())
        type_s = type_ls[0]  # 室
        item['type_s'] = type_s
        type_t = type_ls[1]  # 厅
        item['type_t'] = type_t
        type_c = type_ls[2]  # 厨
        item['type_c'] = type_c
        type_w = type_ls[3]  # 卫
        item['type_w'] = type_w
        floor_ls = response.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[2]/text()').extract_first()
        floor_ls = re.sub('(\()|(\))', '', floor_ls)
        floor_ls = re.sub('共', '/', floor_ls)
        floor = floor_ls.split('/')[0]  # 楼层数
        item['floor'] = floor.strip()
        floors = floor_ls.split('/')[1]  # 总楼层
        item['floors'] = floors.strip()
        area = response.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[3]/text()').extract_first()
        area = re.sub('㎡', '', area)  # 面积
        item['area'] = area.strip()
        threading = response.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[7]/text()').extract_first()
        item['threading'] = threading.strip()  # 房屋朝向
        year = response.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[8]/text()').extract_first()
        item['year'] = year.strip()  # 建造年限
        decoration = response.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[9]/text()').extract_first()
        item['decoration'] = decoration.strip()  # 装修情况
        lift = response.xpath('.//div[@class="base"]/div[@class="content"]/ul/li[14]/text()').extract_first()
        item['lift'] = lift.strip()  # 有无电梯
        coord_ls = re.findall('resblockPosition:(.*),', response.text)
        coord_ls = re.sub('\"|\'', '', coord_ls[0])
        coord_x = coord_ls.split(',')[0]  # 经度
        item['coord_x'] = coord_x
        coord_y = coord_ls.split(',')[1]  # 纬度
        item['coord_y'] = coord_y
        name = re.findall('resblockName:(.*),', response.text)
        name = re.sub('\"|\'', '', name[0])
        item['name'] = name.strip()
        print(item)
        yield item
