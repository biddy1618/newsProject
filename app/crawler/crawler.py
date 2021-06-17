import requests
import logging

from bs4 import BeautifulSoup as bs

from typing import Dict, List
import urllib.parse as urlparse

from app.helper import Helper


logging.basicConfig(
    format='{levelname:<10} {asctime}: {message}', 
    level=logging.DEBUG, 
    datefmt="%m/%d/%Y %H:%M:%S",
    style="{")
log = logging.getLogger(__name__)

class Crawler():
    """
    Generic class defining crawler.
    """
    def __init__(self):
        self.URL_MAIN = "https://www.inform.kz"
        self.URL_ARCHIVE = "https://www.inform.kz/ru/archive"
        self.session = requests.Session()

    def get_url(self, url: str, params: Dict[str, str] = None) -> requests.Response:
        """
        Fetch the URL provided and return response object.

        Args:
            url (str): URL provided
            params (Dict[str, str]): query parameters in dictinary format.

        Returns:
            requests.Response: HTML page fetched with response code.
        """
        try:
            r = self.session.get(url, params = params)
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            logging.error(Helper._message(f"Failed to get the URL {url}", e))
            raise SystemExit(e)
        logging.info(Helper._message(f"Success retrieving URL {url}"))
        return r

    def extract_links(self, response: requests.Response) -> List[str]:
        """
        Retrieving links given the response object.

        Args:
            body (requests.Response): response object containing links to articles.

        Returns:
            List[str]: list of extractred article links give the reponse.
        """
        soup = bs(response.content, "html.parser")
        link_divs = soup.find_all("div", class_ = "lenta_news_block")
        try:
            links = [d.li.a["href"].strip() for d in link_divs]
        except AttributeError as e:
            logging.error(Helper._message("Failed to extract links to articles at {response.url}.", e))
            raise SystemExit(e)
        logging.info(Helper._message("Retrieved article links from {response.url} successfully"))
        return links
    
    def extract_pages(Helper, response: requests.Response) -> List[str]:
        """
        Retrieving article page links from first page for the given date.

        Args:
            response (requests.Response): response object of the first page.

        Returns:
            List[str]: links for the article pages.
        """
        soup = bs(response.content, "html.parser")
        try:
            pages = soup.find("p", class_ = "pagination")
            pages = pages.find_all("a")
            pi = pages[0].getText().strip()
            pl = pages[-1].getText().strip()
            parsed_url = urlparse.urlparse(response.url)
            pages = [parsed_url._replace(path=f"/ru/archive/{str(i)}").geturl() for i in range(int(pi), int(pl) + 1)]
        except (AttributeError, IndexError, ValueError, TypeError) as e:
            logging.error(Helper._message(f"Failed to fetch articles page links at URL {response.url}", e))
            raise SystemExit(e)
        logging.info(Helper._message(f"Retrieved article page links from {response.url} successfully"))
        return pages    
        
    
    def extract_article(self, response: requests.Response) -> Dict[str, str]:
        """[summary]

        Args:
            body (requests.Response): [description]

        Returns:
            Dict[str, str]: [description]
        """
        raise NotImplementedError("Function not implemented yet.")