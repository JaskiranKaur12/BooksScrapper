import re

from locators.book_locator import BookLocators

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
        self.parent = parent

    def __repr__(self):
        return f"Quote: {self.name} by {self.price}"

    @property
    def name(self):
        locator = BookLocators.TEXT
        return self.parent.select_one(locator).attrs['title']

    @property
    def link(self):
        locator = BookLocators.LINK
        return self.parent.select_one(locator).attrs['href']

    @property
    def rating(self):
        locator = BookLocators.RATING
        star_tag = self.parent.select_one(locator)
        classes = [classes for classes in star_tag.attrs['class'] if classes != 'star-rating']
        rating_number=BookParser.RATINGS.get(classes[0], default=9) #none, if not found

    @property
    def price(self):
        locator = BookLocators.PRICE
        price=self.parent.select_one(locator).string
        matches = re.search('£([0-9]+/.[0-9]+)', price)
        return float(matches.group(1))
