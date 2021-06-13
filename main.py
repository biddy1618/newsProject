# First, process single URL based and retrieve links to articles

import requests
import random

from bs4 import BeautifulSoup as bs

from crawler import Crawler
from helper import Helper


crawler = Crawler()

def linkTest(): 
    url = "https://www.inform.kz/ru/archive"
    params = {'date': '01.01.2020'}

    body = requests.get(url, params = params)

    soup = bs(body.content, 'html.parser')


    link_divs = soup.find_all('div', class_ = 'lenta_news_block')

    for d in link_divs:
        print(d.li.a['href'])

def articleTest():
    dates = Helper.generateDates("01.01.2019", "01.02.2021")
        
    res = set()

    for d in random.sample(dates, 10):
        r = crawler.getUrl(
            "https://www.inform.kz/" + "ru/archive",
            {'date': d}
        )
    
        links = crawler.extractLinks(r)
    
        for l in random.sample(links, 2):
            url = "https://www.inform.kz/" + l
            body = requests.get(url)

            soup = bs(body.content, 'html.parser')

            
            title = soup.find('div', class_ = 'article_title')
            print('URL')
            print(url)
            print("TITLE:")
            print(title.getText().strip())
            date = soup.find('div', class_ = 'date_public_art')
            print("DATE:")
            print(date.getText().strip())
            links = soup.find('div', class_ = 'frame_news_article')
            if links:
                res = set()
                for a in links.find_all('a'):
                    res.add(a['href'])
                print("LINKS:")
                for l in res:
                    print(l)
                links.decompose()
            body = soup.find('div', class_ = 'article_news_body')
            print("BODY:")
            print(body.getText().strip())
            keyword = soup.find('div', class_ = 'keyword_art')
            print("TAGS:")
            for t in  [t.strip() for t in keyword.getText().split('#')]:
                print(t)
            author = soup.find('p', class_ = 'name_p')
            if author:
                print("AUTHOR:")
                print(author.getText().strip())
            print('-'*50)
    
    # url = "https://www.inform.kz/ru/serdechnyy-pristup-stal-vinoy-smertel-nogo-dtp-v-akmolinskoy-oblasti_a3690672"
    # body = requests.get(url)

    # soup = bs(body.content, 'html.parser')

    # title = soup.find('div', class_ = 'article_title')
    # print(title.getText().strip())
    # date = soup.find('div', class_ = 'date_public_art')
    # print(date.getText().strip())
    # links = soup.find('div', class_ = 'frame_news_article')
    # res = set()
    # for a in links.find_all('a'):
    #     res.add(a['href'])
    # print(res)
    # links.decompose()
    # body = soup.find('div', class_ = 'article_news_body')
    # print(body.getText().strip())
    # keyword = soup.find('div', class_ = 'keyword_art')
    # for t in  [t.strip() for t in keyword.getText().split('#')]:
    #     print(t)

articleTest()



