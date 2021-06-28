import sqlalchemy
from app.crawler.crawler import Crawler
from app.helper import Helper
from app.db import db, models
import logging

logger = logging.getLogger(__name__)

crawler = Crawler()
s = db.Session()

def crawler_test(dateFirst = '01.01.2012', dateLast = '01.01.2013'):
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
                print(f'Duplicate article URL: {l}')
                continue
            r_page = crawler.get_url(l)
            res.add(l)
            crawler.extract_article(r_page)
        
def cralwer_test_article(url):
    r_page = crawler.get_url(url)
    article = crawler.extract_article(r_page)
    return article

# models.Base.metadata.drop_all(db.engine)
models.Base.metadata.create_all(db.engine)
s = db.Session()

# db.crawl_and_save_to_db("01.01.2012", end_date="01.01.2013", s=s)
db.crawl_and_save_to_db("17.02.2012", end_date="01.01.2013", s=s)