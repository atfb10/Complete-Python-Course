from parsers.quote import QuoteParser
from locators.quotes_page_locators import QuotePageLocator
from selenium.webdriver.common.by import By # self.browser.find_elements(By.CSS_SELECTOR, locator)


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def all_quotes(self):
        '''
        Find all quotes
        Create a list of QuoteParser objects.
        QuoteParser objects are created by looping through each quote 
        and passing the quote as the parent into the QuoteParser constructor
        '''
        locator = QuotePageLocator.QUOTE
        quotes = self.browser.find_elements(By.CSS_SELECTOR, locator)
        return [QuoteParser(quote) for quote in quotes]