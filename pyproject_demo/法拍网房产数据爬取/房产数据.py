# 发送请求
import requests
from bs4 import BeautifulSoup

cookies = {
    '__jsluid_s': 'c38380e66ec980b3a089f3657b5cc69a',
    '__jsl_clearance_s': '1731046706.88|0|BXjSO33t9S754SgpXeWSXvkJ2rw%3D',
    'ASP.NET_SessionId': 'xhs42ycksaz4mcqralkjkxs3',
    'Cookies-01': '76891161',
    'Hm_lvt_5698cdfa8b95bb873f5ca4ecf94ac150': '1731046777',
    'HMACCOUNT': 'D7CF222DBBBDBD2A',
    'Hm_lpvt_5698cdfa8b95bb873f5ca4ecf94ac150': '1731048774',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www1.rmfysszc.gov.cn',
    'Referer': 'https://www1.rmfysszc.gov.cn/projects.shtml?dh=3&gpstate=1&wsbm_slt=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

data = {
    'type': '0',
    'name': '',
    'area': '',
    'xmxz': '0',
    'state': '0',
    'money': '',
    'money1': '',
    'number': '0',
    'fid1': '',
    'fid2': '',
    'fid3': '',
    'order': '0',
    'page': '1',
    'include': '0',
}

response = requests.post('https://www1.rmfysszc.gov.cn/ProjectHandle.shtml', cookies=cookies, headers=headers, data=data)
# print(response.status_code)

response.encoding = 'utf-8'

# 查看结果
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

# 提取数据
price = soup.select('div.prod-guj')
# data要改，有反爬


# 处理数据