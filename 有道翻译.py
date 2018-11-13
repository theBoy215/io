from urllib import request, parse
import json
import time
import hashlib

#   有道翻译的url
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

#   通过反爬虫，伪造表单
def search():
    i = input('请输入单词:') #  用户输入的单词名称
    salt = str(int((time.time() * 1000)))   # 伪造加密盐
    md5 = hashlib.md5() # 创建md5
    md5.update(('fanyideskweb' + i + salt + '6x(ZHw]mwzX#u0V7@yfwK').encode('utf-8'))   # 使用md5加密
    sign = md5.hexdigest()  #  转换成16进制

    #   伪造表单内容
    data = {
        'i': i,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false',
    }

    #   在url上连接表单内容
    new_data = parse.urlencode(data)

    #   伪装请求头
    headers = {
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-493176930@10.168.8.63; OUTFOX_SEARCH_USER_ID_NCOO=38624120.26076847; SESSION_FROM_COOKIE=unknown; JSESSIONID=aaabYcV4ZOU-JbQUha2uw; ___rl__test__cookies=1534210912076',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }

    #   发送请求
    req = request.Request(url, bytes(new_data, 'utf-8'), headers)
    html = request.urlopen(req).read().decode('utf-8')  #   对请求的数据进行解码
    htmls = json.loads(html)    #   将读取的内容转换成python数据类型
    strs = ''

    #   提取数据
    try:
        for value in htmls['smartResult']['entries']:
            strs += value
        return strs
    except:
        html_1 = htmls['translateResult'][0][0]['tgt']
        return html_1


if __name__ == '__main__':
    while True:
        obj = search()
        print(obj)
