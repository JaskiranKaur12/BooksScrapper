from bs4 import BeautifulSoup

from locators.books_locator import All_Books_Locators
from parsers.Books import BookParser

class AllBooks:
    def __init__(self,pagecontent):
        self.soup = BeautifulSoup(pagecontent,'html.parser')

    @property
    def books(self):
         return [BookParser(e) for e in self.soup.select(All_Books_Locators.BOOKS)]