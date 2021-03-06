import re
from locators.book_locators import BookLocators

class BookParser:
    RATINGS={
        'One':1,
        'Two':2,
        'Three':3,
        'Four':4,
        'Five':5
    }
    def __init__(self,parent):
        self.parent=parent

    @property
    def name(self):
        locators=BookLocators.NAME_LOCATOR
        item_name=self.parent.select_one(locators).attrs['title']
        return item_name

    @property
    def link(self):
        locator=BookLocators.LINK_LOCATOR
        item_link=self.parent.select_one(locator).attrs['href']
        return item_link

    @property
    def price(self):
        locator=BookLocators.PRICE_LOCATOR
        item_price=self.parent.select_one(locator).string
        pattern="£([0-9]+\.[0-9]+)"
        matcher=re.search(pattern,item_price)
        return float(matcher.group(1))

    @property
    def rating(self):
        locator=BookLocators.RATING_LOCATOR
        star_rating=self.parent.select_one(locator)
        classes=star_rating.attrs['class']
        rating_classes=[r for r in classes if r!='star-rating']
        rating_num=BookParser.RATINGS.get(rating_classes[0])
        return  rating_num

    def __repr__(self):
        return f"<Book {self.name} price:{self.price} Rating: {self.rating} star>"