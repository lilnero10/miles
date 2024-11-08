import requests
from bs4 import BeautifulSoup
import pymysql

#爬取微博热搜数据方法
def scrape_weibo_hotline():
    #爬虫头数据
    cookies = {
        'SINAGLOBAL': '1268631067322.501.1721994345351',
        'SUB': '_2AkMR57f_f8NxqwFRmf0Wz2ngaIR2zA3EieKnu0YkJRMxHRl-yT9yqhcltRB6OmeZEDxnfDUQVUUq3AE--CUsLxeoADYu',
        'SUBP': '0033WrSXqPxfM72-Ws9jqgMF55529P9D9W51NoihndlwblhvL5dTyNpe',
        '_s_tentry': 'passport.weibo.com',
        'Apache': '856918090705.9581.1723545801433',
        'ULV': '1723545801437:2:1:1:856918090705.9581.1723545801433:1721994345352',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://passport.weibo.com/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }
    params = (
        ('cate', 'realtimehot'),
    )

    #获取网页
    response = requests.get('https://s.weibo.com/top/summary', headers=headers, params=params, cookies=cookies)
    #解析网页
    response.encoding='utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    # 爬取的内容
    hot_names = []
    for item in soup.select("#pl_top_realtimehot > table > tbody > tr > td.td-02 > a"):
        hot_names.append(item.get_text())
    return hot_names

# 将爬取数据保存到数据库方法
def save_to_mysql(hot_names):
    # 连接到MySQL数据库
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='010920hei',
        database='mydb_1',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # 创建表（如果不存在）
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS weibo_hot_search (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    hot_name VARCHAR(255) NOT NULL,
                    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # 插入数据
            for hot_name in hot_names:
                cursor.execute(
                    "INSERT INTO weibo_hot_search (hot_name) VALUES (%s)",
                    (hot_name,)
                )

        # 提交事务
        connection.commit()

    finally:
        # 关闭连接
        connection.close()

def main():
    hot_names = scrape_weibo_hotline()
    save_to_mysql(hot_names)

if __name__ == '__main__':
    main()