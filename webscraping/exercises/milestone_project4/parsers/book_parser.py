import logging
from locators.book_locator import BookLocator

logger = logging.getLogger('scraping.book_parser')

class BookParser:

    STAR_RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
    }

    def __init__(self, parent):
        logger.info(f'Book created from parent: {parent}')
        self.parent = parent

    def __repr__(self) -> str:
        return f'{self.title} has {self.rating} stars'

    @property
    def link(self):
        locator = BookLocator.LINK
        link_item = self.parent.select_one(locator)
        link = link_item.attrs['href']
        return link
        
    @property
    def title(self):
        locator = BookLocator.TITLE
        title_items = self.parent.select_one(locator)
        title = title_items.attrs['title']
        return title
        
    @property
    def price(self):
        locator = BookLocator.PRICE
        price_item = self.parent.select_one(locator)
        price = price_item.string
        price_float = float(price.strip('£'))
        return price_float
        
    @property
    def rating(self):
        locator = BookLocator.RATING
        rating_item = self.parent.select_one(locator)
        rating_item_classes = rating_item.attrs['class']
        rating_text = [class_name for class_name in rating_item_classes if class_name != 'star-rating']
        # assigns rating number as the value associated with its respective key in STAR_RATING dictionary. 
        # The key the value is gotten from it rating_text[0]
        # If there is no key = to rating_text[0], rating_number = -1
        rating_number = BookParser.STAR_RATINGS.get(rating_text[0], -1)
        return rating_number