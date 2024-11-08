import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def fetch_movie_info():

    cookies = {
        'doaj-cookie-consent': '"By using our website\\054 you have agreed to our cookie policy."',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://www.doaj.org/search/articles?ref=homepage-box&source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22biomedicine%22%2C%22default_operator%22%3A%22AND%22%7D%7D%2C%22track_total_hits%22%3Atrue%7D',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }

    response = requests.get('https://www.doaj.org/article/000160f6a3134943b580f32198dabcee', cookies=cookies,
                            headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 爬取内容
    articles = []
    for item in soup.select("#maincontent > div > div.container > div > section > p.article-details__abstract"):
        articles.append(item.get_text())
    return articles
    # print(articles)


def main():
    fetch_movie_info()


if __name__ == '__main__':
    main()
