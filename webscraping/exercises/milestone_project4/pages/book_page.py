import logging
from bs4 import BeautifulSoup

from parsers.book_parser import BookParser
from locators.book_page_locator import BookPageLocator

logger = logging.getLogger('scraping.book_page')

class BookPage:
    def __init__(self, page_content):
        logger.debug('Parsing page content w/ BS4')
        self.soup = BeautifulSoup(page_content, 'html.parser')

    def __len__(self):
        return len(self.get_books)
    
    def __getitems__(self, i):
        return self.get_books[i]

    @property
    def get_books(self) -> list:
        logger.debug(f'Finding all books using: {BookPageLocator.BOOK}')
        book_tags = self.soup.select(BookPageLocator.BOOK)
        return [BookParser(book) for book in book_tags]
    
    @property
    def page_count(self) -> int:
        logger.debug(f'Finding # of pages: {BookPageLocator.PAGE}')
        pages_string = self.soup.select_one(BookPageLocator.PAGE).string
        logger.debug(f'Pages found: {pages_string}')
        list_of_page_strings = pages_string.split()
        total_pgs = int(list_of_page_strings[len(list_of_page_strings) - 1])
        logger.debug(f'Extracted number of pages: {total_pgs}')
        return total_pgs