from bs4 import BeautifulSoup

from locators.books_locator import All_Books_Locators

class AllBooks:
    def __init__(self,pagecontent):
        self.soup = BeautifulSoup(pagecontent,'html.parser')

    @property
    def __bool__(self):
         return self.soup.select(All_Books_Locators.BOOKS)