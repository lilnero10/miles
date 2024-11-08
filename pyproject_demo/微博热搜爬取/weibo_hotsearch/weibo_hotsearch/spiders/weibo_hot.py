import scrapy
from bs4 import BeautifulSoup

class WeiboHotSpider(scrapy.Spider):
    name = "weibo_hot"
    allowed_domains = ["s.weibo.com"]
    start_urls = ["https://s.weibo.com/top/summary"]

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        hot_searches = soup.select("#pl_top_realtimehot > table > tbody > tr > td.td-02 > a")

        for item in hot_searches:
            title = item.select_one("td.td-02 > a").get_text(strip=True)

            yield {
                'title': title
            }
