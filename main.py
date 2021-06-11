# First, process single URL based and retrieve links to articles

import requests
from bs4 import BeautifulSoup as bs

url = "https://www.inform.kz/ru/archive"
params = {'date': '01.01.2020'}

body = requests.get(url, params = params)

soup = bs(body.content, 'html_parser')


link_divs = soup.find_all('div', class_ = 'lenta_news_block')

for d in link_divs:
    print(d.li.a['href'])
