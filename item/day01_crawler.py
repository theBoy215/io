import requests
from urllib import parse
from lxml import etree
import xlwt
import time

url = 'http://zt.zjzs.net/xuanke2018/'

req = requests.get(url).content.decode('utf-8')
tree = etree.HTML(req)

book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1',cell_overwrite_ok=True)
col0 = ['地区','学校代码','学校名称','网址','层次','专业(类)名称','选考科目数','选考科目范围','类中所含专业']
for i in range(len(col0)):
    sheet1.write(0,i,col0[i])


content = tree.xpath('.//table[@style="text-align:center;"]/tr[@bgcolor="#FFFFFF"]')
count = 1
for i in content:
    area = i[0].text
    code = i[1].text
    colleage = i[2].text
    area_url = i[3].xpath('./a/@href')[0]
    req_url = i[4].xpath('./a/@href')[0]
    new_url = parse.urljoin(url,req_url)
    new_req = requests.get(new_url).content.decode('utf-8')
    tree1 = etree.HTML(new_req)
    detail = tree1.xpath('//tr[@bgcolor="#FFFFFF"]')
    for j in detail:
        cen = j[0].text
        subject = j[1].text
        sub_num = j[2].text
        sub_round = j[3].text
        sub_pro = j[4].text
        sheet1.write(count,0,area)
        sheet1.write(count,1,code)
        sheet1.write(count,2,colleage)
        sheet1.write(count,3,area_url)
        sheet1.write(count,4,cen)
        sheet1.write(count,5,subject)
        sheet1.write(count,6,sub_num)
        sheet1.write(count,7,sub_round)
        sheet1.write(count,8,sub_pro)
        count += 1
    time.sleep(1)
book.save('2018年拟在浙招生普通高校专业（类）选考科目范围.xls')

