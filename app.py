import requests

from pages.books_pages import AllBooks

page_content=requests.get("http://books.toscrape.com").content
page=AllBooks(page_content)

books=page.books
for b in books:
    print(b)