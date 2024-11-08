import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def fetch_movie_info():
    # 这里以豆瓣电影Top250为例
    url = 'https://movie.douban.com/top250'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())

    movies = []

    for item in soup.find_all('div', class_='item')[:100]:  # 控制爬取数据条数100条
        movie_name = item.find('span', class_='title').text

        director_and_country = item.find('p').text.strip().split("\n")[0].strip()

        director = director_and_country.split("   ")[0].replace("导演: ", "").strip()

        release_date_country = item.find('p').text.strip().split("\n")[1].strip()

        release_date = release_date_country.split("/")[0].strip()

        country = release_date_country.split("/")[1].strip()

        rating = item.find('span', class_='rating_num').text

        movies.append({
            '电影名称': movie_name,
            '上映年份': release_date,
            '导演': director,
            '豆瓣评分': rating,
            '制片国家/地区': country
        })

    return movies

# 保存为csv文件方法
def save_to_file_csv(movies, filename='douban_movies.csv'):
    # 指定完整的路径
    file_path = f'/Users/chenzhiyong/Desktop/{filename}'
    with open(file_path, 'a', encoding='utf-8') as f:
        for movie in movies:
            f.write(
                f"{movie['电影名称']},{movie['上映年份']},{movie['导演']},{movie['豆瓣评分']},{movie['制片国家/地区']}\n")


# 保存为xlsx文件方法
def save_to_file_xlsx(movies, filename='douban_movies.xlsx'):
    # 指定完整的路径
    file_path = f'/Users/chenzhiyong/Desktop/{filename}'

    # 将电影数据转换为 DataFrame
    df = pd.DataFrame(movies, columns=['电影名称', '上映年份', '导演', '豆瓣评分', '制片国家/地区'])

    # 将 DataFrame 保存为 Excel 文件
    df.to_excel(file_path, index=False, engine='openpyxl')


def main1():
    movies = fetch_movie_info()
    save_to_file_xlsx(movies)
    print(f"已保存{len(movies)}条数据")

def main2():
    # 每10分钟爬取一次
    while True:
        movies = fetch_movie_info()
        save_to_file_csv(movies)
        print(f"已保存{len(movies)}条数据")
        time.sleep(600)


if __name__ == "__main__":
    main1()
    # fetch_movie_info()