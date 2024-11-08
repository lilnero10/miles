import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template,request

app = Flask(__name__)

def get_phone(phone):
    url = f'https://www.ip138.com/mobile.asp?mobile={phone}&action=mobile'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    }
    resp = requests.get(url, headers = headers)

    resp.encoding = 'utf-8'

    soup = BeautifulSoup(resp.text, 'lxml')

    info =[]
    for data in soup.select('div.table > table > tbody > tr > td > a'):
        info.append(data.text.strip())

    base = soup.select('div.table > table > tbody > tr > td > span')[0].text

    output1 = f'{base},{','.join(info)}'

    return output1


@app.route('/')
def index():
    return render_template('search_phone.html')

@app.route('/search_phone')
def search_phone():
    phone = request.args.get('phone')
    data = get_phone(phone)
    return data


app.run(debug=True)



