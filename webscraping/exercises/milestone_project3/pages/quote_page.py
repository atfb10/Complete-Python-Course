from bs4 import BeautifulSoup

from parsers.quote import QuoteParser
from locators.quotes_page_locators import QuotePageLocator

class QuotesPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def all_quotes(self):
        '''
        Find all quotes
        Create a list of QuoteParser objects.
        QuoteParser objects are created by looping through each quote 
        and passing the quote as the parent into the QuoteParser constructor
        '''
        locator = QuotePageLocator.QUOTE
        quotes = self.soup.select(locator)
        return [QuoteParser(quote) for quote in quotes]