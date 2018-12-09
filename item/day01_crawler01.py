import requests
from lxml import etree
import urllib3
import json
from openpyxl import Workbook

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2767.400',
    'Referer': 'https://yz.chsi.com.cn/zsml/queryAction.do',
}

count = 2
book = Workbook()
sheet1 = book.active
sheet1.title = 'sheet1'
sheet1['A1'] = '学术学位'
sheet1['B1'] = '学科类别'
sheet1['C1'] = '招生单位'


####学术学位
def degree():
    url = 'https://yz.chsi.com.cn/zsml/pages/getMl.jsp'
    req = requests.post(url, headers=headers, verify=False).text
    mc_list = json.loads(req)
    for mc in mc_list:
        Subject(mc['dm'], mc['mc'])


def Subject(sub_dm, sub):
    sub_dm, mc = sub_dm, sub
    url = 'https://yz.chsi.com.cn/zsml/pages/getZy.jsp'
    data = {
        'mldm': sub_dm
    }
    req = requests.post(url, data=data, headers=headers, verify=False).text
    mc_list = json.loads(req)
    for mc in mc_list:
        Unit(sub, mc['mc'], sub_dm, mc['dm'])


def Unit(sub, mc, sub_dm, dm):
    sub, mc, sub_dm, dm = sub, mc, sub_dm, dm
    # print(sub, ' ', mc, ' ', sub_dm, ' ', dm)
    url = 'https://yz.chsi.com.cn/zsml/queryAction.do'
    data = {
        'mldm': sub_dm,
        'yjxkdm': dm
    }
    req = requests.post(url, data=data, headers=headers, verify=False).text
    tree = etree.HTML(req)
    li_len = tree.xpath('.//ul[@class="ch-page"]/li/a/text()')
    Sec_Unit(sub, mc, sub_dm, dm, li_len[-1])


def Sec_Unit(sub, mc, sub_dm, dm, i):
    sub, mc, sub_dm, dm, i = sub, mc, sub_dm, dm, i
    # print(sub, ' ', mc, ' ', sub_dm, ' ', dm, ' ', i)
    global count
    url = 'https://yz.chsi.com.cn/zsml/queryAction.do'
    for pg in range(1, int(i) + 1):
        data = {
            'mldm': sub_dm,
            'yjxkdm': dm,
            'pageno': str(pg)
        }
        print('页码：', pg)
        req = requests.post(url, data=data, headers=headers, verify=False).text
        tree = etree.HTML(req)
        content = tree.xpath('.//form[@name="form3"]/a/text()')
        for i in range(len(content)):
            sheet1['A%d' % count] = sub
            sheet1['B%d' % count] = mc
            sheet1['C%d' % count] = content[i]
            count += 1


if __name__ == '__main__':
    degree()
    book.save('2019年硕士专业目录查询.xls')
