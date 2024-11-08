import requests
import pandas as pd
from bs4 import BeautifulSoup

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

    # 爬取内容
    hot_names = []
    for item in soup.select("#pl_top_realtimehot > table > tbody > tr > td.td-02 > a"):
        hot_names.append(item.get_text())
    return hot_names


def save_to_file_xlsx(hot_names, filename='微博热搜.xlsx'):
    # 指定完整的路径
    file_path = f'/Users/chenzhiyong/Desktop/{filename}'

    # 将电影数据转换为 DataFrame
    df = pd.DataFrame(hot_names, columns=['热搜名称'])

    # 将 DataFrame 保存为 Excel 文件
    df.to_excel(file_path, index=False, engine='openpyxl')

    print('数据已存储到微博热搜.xlsx')

#保存txt文件方法
def save_to_file_txt(hot_names, filename='微博热搜.txt'):
    # 指定完整的路径
    file_path = f'/Users/chenzhiyong/Desktop/{filename}'

    # 存储到txt文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('热搜名称\n')
        for name in hot_names:
            file.write(name + '\n')

    print('数据已存储到微博热搜.txt')

def main():
    hot_names = scrape_weibo_hotline()
    save_to_file_txt(hot_names)


if __name__ == '__main__':
    main()