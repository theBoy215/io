# -*- coding: utf-8 -*-
import scrapy
from urllib import request
from aip import AipOcr
import re, time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from lxml import etree
from ..items import DataZiruItem


class ZiruSpider(scrapy.Spider):
    name = 'ziru'
    allowed_domains = ['ziroom.com']
    start_urls = ['']

    def start_requests(self):
        for i in range(1, 51):
            url = 'http://www.ziroom.com/z/nl/z2-d23008629.html?p=%s' % i
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        detail_url = response.xpath('.//p[@class="more"]/a/@href').extract()
        img = re.findall('"image":"(.*)",', response.text)
        img = response.urljoin(img[0])
        req = request.urlopen(img).read()
        with open('1.png', 'wb') as f:
            f.write(req)
        img = open('1.png', 'rb')
        APP_ID = '15781033'
        API_KEY = 'kTRkyVCd3h6HignBl8b9qFE8'
        SECRET_KEY = 'wAk6TtlSnwqTxmZQDCmpiXCHijsNVipD '
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        options = {}
        options["detect_direction"] = "true"
        options["probability"] = "true"
        content = client.basicAccurate(img.read(), options)
        im_list = [int(i) for i in content['words_result'][0]['words']]
        price = re.findall('"offset":(.*)}', response.text)
        pr_ls = eval(price[0])
        for i in range(len(detail_url)):
            price = ''
            for j in range(4):
                price += str(im_list[pr_ls[i][j]])
            url = response.urljoin(detail_url[i])
            yield scrapy.Request(url=url, meta={'price': price, 'url': url}, callback=self.detail_data)

    def detail_data(self, response):
        item = DataZiruItem()
        url = response.meta['url']
        price = response.meta['price']
        item['price'] = price
        title = response.xpath('.//div[@class="room_name"]/h2/text()').extract_first()
        title = title.strip()
        item['title'] = title
        meter = response.xpath('.//ul[@class="detail_room"]/li[1]/text()').extract_first()
        meter = ''.join([i.strip() for i in meter][3:-1])
        item['meter'] = meter
        threading = response.xpath('.//ul[@class="detail_room"]/li[2]/text()').extract_first()
        threading = ''.join([i for i in threading][3:])
        item['threading'] = threading
        types = response.xpath('.//ul[@class="detail_room"]/li[3]/text()').extract_first()
        types = ''.join([i for i in types][3:])
        s = '0'
        t = '0'
        for i in range(len(types)):
            if '室' in types:
                if types[i] == '室':
                    s = types[i - 1]
            if '厅' in types:
                if types[i] == '厅':
                    t = types[i - 1]
        item['type_s'] = s
        item['type_t'] = t
        floor_ls = response.xpath('.//ul[@class="detail_room"]/li[4]/text()').extract_first()
        floor_ls = ''.join([i for i in floor_ls][3:])
        floor_ls = re.sub('层', '', floor_ls).strip()
        floor_ls = floor_ls.split('/')
        item['floor'] = floor_ls[0]
        item['floors'] = floor_ls[1]
        sub = response.xpath('.//ul[@class="detail_room"]/li[5]/span[1]/text()').extract_first()
        sub = ''.join([re.sub('\s.*', '', i) for i in sub.strip()][4:-1])
        sub = ''.join([re.sub('[\u4e00-\u9fa5].*', '', i) for i in sub[3:]])
        item['sub'] = sub
        position_x = response.xpath('.//div[@class="msCon clearfix"]/input[1]/@data-lng').extract_first()
        item['position_x'] = position_x
        position_y = response.xpath('.//div[@class="msCon clearfix"]/input[1]/@data-lat').extract_first()
        item['position_y'] = position_y

        # chrome_options = Options()
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
        # chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        # chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
        # chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        # chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        #
        # driver = Chrome(executable_path=r'C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver.exe',
        #                 chrome_options=chrome_options)
        # driver.get(url)
        # time.sleep(0.2)
        # driver.execute_script('window.scrollTo(0,2000)')
        # time.sleep(0.2)
        # item['wj_time'] = get_time(driver, '望京-地铁站')
        # time.sleep(0.5)
        # item['sd_time'] = get_time(driver, '上地-地铁站')
        # time.sleep(0.5)
        # item['zgc_time'] = get_time(driver, '中关村-地铁站')
        # time.sleep(0.5)
        # item['xeq_time'] = get_time(driver, '西二旗-地铁站')
        # time.sleep(0.5)
        # item['gm_time'] = get_time(driver, '国贸-地铁站')
        # time.sleep(0.5)
        # item['xd_time'] = get_time(driver, '西单-地铁站')
        #
        # driver.quit()
        print(item)
        yield item


def get_time(driver, names):
    driver.find_element_by_id('mapsearchText').click()
    time.sleep(0.2)
    driver.find_element_by_id('mapsearchText').clear()
    time.sleep(0.5)
    driver.find_element_by_id('mapsearchText').send_keys(names)
    time.sleep(0.2)
    driver.find_element_by_id('toBus').click()
    time.sleep(3)
    tree = etree.HTML(driver.page_source)
    times = tree.xpath('.//div[@class="reasultsmallbox_h"]/text()')
    times = times[0].strip()
    return times
