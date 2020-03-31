import re
import logging

from locators.book_locator import BookLocators

logger= logging.getLogger('Scraping.book_parser')
class BookParser:
    """Given one quote div at a time,
    it will find out quote content, author and tags"""

    RATINGS={
        'One':1,
        'Two':2,
        'Three':3,
        'Four':4,
        'Five':5
    }

    def __init__(self, parent):
        logger.debug(f'New book parsed created from `{parent}` ')
        self.parent = parent

    def __repr__(self):
        return f"Book {self.name}, £{self.price} has {self.rating} stars"

    @property
    def name(self):
        logger.debug('Finding book name..')
        locator = BookLocators.TEXT
        item_name=self.parent.select_one(locator).attrs['title']
        logger.debug(f'found book name, `{item_name}`')
        return item_name

    @property
    def link(self):
        logger.debug('Finding book link..')
        locator = BookLocators.LINK
        item_link=self.parent.select_one(locator).attrs['href']
        logger.debug(f'found book link, `{item_link}`')
        return item_link

    @property
    def rating(self):
        logger.debug('Finding book rating..')
        locator = BookLocators.RATING
        star_tag = self.parent.select_one(locator)
        classes = [classes for classes in star_tag.attrs['class'] if classes != 'star-rating']
        rating_number=BookParser.RATINGS.get(classes[0], "Not Found") #none, if not found
        logger.debug(f'Found book rating, `{rating_number}`')
        return rating_number

    @property
    def price(self):
        logger.debug('Finding book price..')
        locator = BookLocators.PRICE
        price = self.parent.select_one(locator).string
        matches = re.search( '£([0-9]+\.[0-9]+)', price)
        logger.debug(f'found book price, `{matches.group(1)}`')
        return matches.group(1)
