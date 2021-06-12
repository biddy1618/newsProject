import requests
from bs4 import BeautifulSoup as bs

class Crawler():
    def __init__():
        pass

    def getUrl(url, params):
        body = requests.get(url, params = params)
        return body

    def extractLinks(body):
        soup = bs(body.content, 'html.parser')
        link_divs = soup.find_all('div', class_ = 'lenta_news_block')

        links = [l.strip() for l in link_divs]

        return links
    
    def extractArticle(body):
        
        return None


