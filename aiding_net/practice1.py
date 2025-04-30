import time

import requests
from base64 import b64encode
import hashlib

url = "https://www.python-spider.com/api/challenge1"

num = 0
for i in range(1, 101):
    timestamp = str(int(time.time()))
    b64_data = b64encode(('9622'+timestamp).encode())
    safe = hashlib.md5(b64_data).hexdigest()
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://www.python-spider.com",
        "priority": "u=1, i",
        "referer": "https://www.python-spider.com/challenge/1",
        "safe": safe,
        "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "timestamp": timestamp,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    cookies = {
        "Hm_lvt_337e99a01a907a08d00bed4a1a52e35d": "1742911169,1745330171",
        "HMACCOUNT": "7A59054D2F1E85A2",
        "sessionid": "4qcddspt7mow5npbua6iiwi1uxa8lppx",
        "no-alert": "true",
        "Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d": "1745330296"
    }
    data = {
        "page": f"{i}"
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)

    res_data = response.json()
    page_data = res_data.get("data")
    if not page_data:
        continue
    page_data = [int(i.get('value').strip('\r')) for i in page_data if i.get('value')]
    num = num + sum(page_data)
print(num)
