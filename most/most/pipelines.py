# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import openpyxl


class MostPipeline(object):
    def __init__(self):
        self.work = openpyxl.Workbook()
        self.sheet1 = self.work.create_sheet('Sheet1')
        self.sheet1['A1'] = '信息名称'
        self.sheet1['B1'] = '信心类别'
        self.sheet1['C1'] = '实验室名称'
        self.sheet1['D1'] = '实验室主任'
        self.sheet1['E1'] = '依托单位'
        self.sheet1['F1'] = '主管部门'
        self.sheet1['G1'] = '附件'
        self.count = 2

    def process_item(self, item, spider):
        self.sheet1['A%d' % self.count] = item['title']
        self.sheet1['B%d' % self.count] = item['time']
        self.sheet1['C%d' % self.count] = item['name_text']
        self.sheet1['D%d' % self.count] = item['director_text']
        self.sheet1['E%d' % self.count] = item['unit_text']
        self.sheet1['F%d' % self.count] = item['sector_text']
        self.sheet1['G%d' % self.count] = item['addr']
        self.count += 1
        return item

    def __del__(self):
        self.work.save('省部共建.xlsx')
