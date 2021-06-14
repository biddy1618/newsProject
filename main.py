# First, process single URL based and retrieve links to articles

import requests
import random

from bs4 import BeautifulSoup as bs

from crawler import Crawler
from helper import Helper


crawler = Crawler()

def link_test(): 
    url = "https://www.inform.kz/ru/archive"
    params = {'date': '01.01.2020'}

    body = requests.get(url, params = params)

    soup = bs(body.content, 'html.parser')


    link_divs = soup.find_all('div', class_ = 'lenta_news_block')

    for d in link_divs:
        print(d.li.a['href'])

def article_test():
    dates = Helper.generate_dates("01.01.2019", "01.01.2020")
    output = ''
    for i, d in enumerate(dates):
        
        r = crawler.get_url(
            "https://www.inform.kz/" + "ru/archive",
            {'date': d}
        )
    
        links = crawler.extract_links(r)
    
        for l in links:
            url = "https://www.inform.kz" + l
            response = requests.get(url)
            article_text = ''

            soup = bs(response.content, 'html.parser')

            title = soup.find('div', class_ = 'article_title')
            print(f'URL:\n {url}')
            article_text += 'URL:\n' + url +'\n'
            print(f'TITLE:\n {title.getText().strip()}')
            article_text += 'TITLE:\n' + title.getText().strip() +'\n'
            date = soup.find('div', class_ = 'date_public_art')
            article_text += 'DATE:\n' + date.getText().strip() +'\n'
            print(f'DATE:\n {date.getText().strip()}')
            links = soup.find('div', class_ = 'frame_news_article')
            if links:
                res = set()
                for a in links.find_all('a'):
                    res.add(a['href'])
                article_text += 'LINKS:\n'
                print(f'LINKS:')
                for l in res:
                    print(f'{l}')
                    article_text += l + '\n'
                links.decompose()
            body = soup.find('div', class_ = 'article_news_body')
            article_text += 'BODY:\n' + body.getText().strip() +'\n'
            print(f'BODY:\n {body.getText().strip()}')
            keyword = soup.find('div', class_ = 'keyword_art')
            article_text += 'TAGS:\n'
            print(f'TAGS:')
            for t in  [t.strip() for t in keyword.getText().split('#')]:
                article_text += t + '\n'
                print(f'{t}')
            author = soup.find('p', class_ = 'name_p')
            if author:
                article_text += 'AUTHOR:\n'
                article_text += author.getText().strip() + '\n'
                print(f'AUTHOR:\n {author.getText().strip()}')
            article_text += '-' * 50 + '\n'
            output += article_text
        if i % 10 == 0:
            with open('result.txt', 'a') as f:
                f.write(output)
                output = ''
    with open('result.txt', 'a') as f:
        f.write(output)
        output = ''

article_test()