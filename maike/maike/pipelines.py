# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import openpyxl


class MaikePipeline(object):
    def __init__(self):
        self.book = openpyxl.Workbook()
        self.sheet1 = self.book.create_sheet('Sheet')
        self.sheet1['A1'] = 'name'
        self.sheet1['B1'] = 'class'
        self.sheet1['C1'] = 'titles'
        self.sheet1['D1'] = 'location'
        self.sheet1['E1'] = 'age'
        self.sheet1['F1'] = 'deceased'
        self.sheet1['G1'] = 'area'
        self.sheet1['H1'] = 'affiliation'
        self.count = 2

    def process_item(self, item, spider):
        self.sheet1['A%d' % self.count] = item['name']
        self.sheet1['B%d' % self.count] = item['classes']
        self.sheet1['C%d' % self.count] = item['titles']
        self.sheet1['D%d' % self.count] = item['location']
        self.sheet1['E%d' % self.count] = item['age']
        self.sheet1['F%d' % self.count] = item['deceased']
        self.sheet1['G%d' % self.count] = item['area']
        self.sheet1['H%d' % self.count] = item['affi']
        self.count += 1
        return item

    def __del__(self):
        self.book.save('麦克阿瑟奖项目.xlsx')

