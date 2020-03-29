import requests

from pages.books_pages import AllBooks

page_content=requests.get("http://books.toscrape.com").content
page=AllBooks(page_content)

for b in page.books:
    print(b)