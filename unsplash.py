import requests
import urllib3
import json
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def headers():
    headers = {
        'Referer': 'https://unsplash.com/t/wallpapers',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36Viewport-Width: 1366',
        'Upgrade-Insecure-Requests': '1',
    }
    return headers


if __name__ == '__main__':
    for i in range(1, 100):
        url = 'https://unsplash.com/napi/collections/1065976/photos?page=%d' % i
        req = requests.get(url, verify=False, headers=headers())
        content = json.loads(req.text)
        for i in content:
            id = i['id']
            img = i['links']['download']
            print(img)
            with requests.get(img, verify=False, headers=headers()) as new_img:
                with open('D:\壁纸\用户%s的图片.jpg' % id, 'ab+') as f:
                    f.write(new_img.content)
        time.sleep(1)

