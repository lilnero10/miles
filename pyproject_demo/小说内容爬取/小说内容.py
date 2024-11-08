import requests
from bs4 import BeautifulSoup

# 发送给谁
url = 'https://www.85xs.cc/book/douluodalu1/1.html'

while True:
    # 伪装自己
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    }
    # 发送请求
    resp = requests.get(url, headers=headers)
    # 解码
    resp.encoding = 'utf-8'

    soup = BeautifulSoup(resp.text, 'lxml')
    # print(soup.prettify())
    # 响应
    info = []
    for text in soup.select('div.m-post'):
        info.append(text.get_text().strip())

    title = soup.select('div.entry-text > table.wenxue2 > tbody > tr > td > a')[1].text.strip()
    url = f"https://dl.131437.xyz{soup.select('div.entry-text > table.wenxue2 > tbody > tr > td > a')[1].get('href')}"
    # print(title)
    # 保存
    file_path = f'/Users/chenzhiyong/Desktop/小说内容.txt'

    with open(file_path, 'a', encoding='utf-8') as file:
        for text in info:
            file.write(title + '\n\n' + text + '\n\n')

    if url == 'https://dl.131437.xyz/book/douluodalu1/':
        break