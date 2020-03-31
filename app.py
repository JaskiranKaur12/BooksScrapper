import requests
import logging

from pages.books_pages import AllBooks

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')

logger=logging.getLogger('scraping') #Example of singleton pattern

logger.info('Loading all the books...')


page_content=requests.get("http://books.toscrape.com").content
page=AllBooks(page_content)
books=page.books

# By default, requests library add debug logs u=in the logs.txt file for each http request

for x in range(1, page.page_count):
    url = f"http://books.toscrape.com/catalogue/page-{x+1}.html"
    page_content = requests.get(url).content
    logger.debug('Creating AllBooks Page from page content')
    page = AllBooks(page_content)
    books.extend(page.books)

