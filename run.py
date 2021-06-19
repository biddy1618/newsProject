# First, process single URL based and retrieve links to articles

import requests
import logging

from bs4 import BeautifulSoup as bs

from app.crawler.crawler import Crawler
from app.helper import Helper

import re

crawler = Crawler()

logging.basicConfig(
    format='{levelname:<10} {asctime}: {message}', 
    level=logging.INFO, 
    datefmt='%m/%d/%Y %H:%M:%S',
    style='{')
logger = logging.getLogger(__name__)


def crawler_test(dateFirst = '01.01.2020', dateLast = '02.01.2020'):
    dates = Helper.generate_dates(dateFirst, dateLast)

    for d in dates:
        res = set()
        
        r_link_date = crawler.get_url(
            crawler.URL_ARCHIVE,
            {'date': d}
        )
    
        links = crawler.get_links(r_link_date)
        
        for l in links:
            if l in res:
                logger.warning(Helper._message(f'Duplicate article URL: {l}'))
                continue
            r_page = crawler.get_url(l)
            res.add(l)
            crawler.extract_article(r_page)
        
def cralwer_test_article(url):
    r_page = crawler.get_url(url)
    article = crawler.extract_article(r_page)
    return article

crawler_test()