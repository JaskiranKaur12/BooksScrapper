import re
import  logging
from bs4 import BeautifulSoup

from locators.books_locator import All_Books_Locators
from parsers.Books import BookParser

logger= logging.getLogger('Scraping.all_books_page')
#this is a child logger related to parent(scraping) logger

class AllBooks:
    def __init__(self,pagecontent):
        logger.debug('Parsing page content using beautiful soup')
        self.soup = BeautifulSoup(pagecontent,'html.parser')

    @property
    def books(self):
        logger.debug(f'Getting all the books using `{All_Books_Locators.BOOKS}`')
        return [BookParser(e) for e in self.soup.select(All_Books_Locators.BOOKS)]

    @property
    def page_count(self):
        logger.debug('Finding total number of pages available')
        pager=self.soup.select_one(All_Books_Locators.PAGER).string
        logger.info(f'Found total number of pages available `{pager}`.')
        pattern='Page [0-9]+ of ([0-9]+)'
        matches=re.search(pattern,pager)
        pages=int(matches.group(1))
        logger.debug(f'found number of pages in int: `{pages}`')
        return pages
