import requests

from pages.books_pages import AllBooks


page_content=requests.get("http://books.toscrape.com").content
page=AllBooks(page_content)
books=page.books

for x in range(1, page.page_count):
    url = f"http://books.toscrape.com/catalogue/page-{x+1}.html"
    page_content = requests.get(url).content
    page = AllBooks(page_content)
    books.extend(page.books)

