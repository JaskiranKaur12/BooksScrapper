import re
from bs4 import BeautifulSoup

from locators.books_locator import All_Books_Locators
from parsers.Books import BookParser

class AllBooks:
    def __init__(self,pagecontent):
        self.soup = BeautifulSoup(pagecontent,'html.parser')

    @property
    def books(self):
         return [BookParser(e) for e in self.soup.select(All_Books_Locators.BOOKS)]

    @property
    def page_count(self):
        pager=self.soup.select_one(All_Books_Locators.PAGER).string
        pattern='Page [0-9]+ of ([0-9]+)'
        matches=re.search(pattern,pager)
        pages=int(matches.group(1))
        return pages
