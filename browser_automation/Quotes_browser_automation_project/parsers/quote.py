from selenium.webdriver.common.by import By # self.browser.find_elements(By.CSS_SELECTOR, locator)

from locators.quote_locators import QuoteLocators

class QuoteParser:
    '''
    given a specific quote div, find out data about the quote
    '''
    def __init__(self, parent):
        '''
        parent is parent tag that all other tags fall under
        '''
        self.parent = parent

    def __repr__(self) -> str:
        '''
        print of QuoteParser object returns a string of the quote with the author
        '''
        return f'\"{self.content}\" - {self.author}'

    @property
    def content(self) -> str:
        '''
        return quote content as a string
        '''
        return self.parent.find_element(By.CSS_SELECTOR, QuoteLocators.CONTENT).text
    
    @property
    def author(self) -> str:
        '''
        return quote's author as a string
        '''
        return self.parent.find_element(By.CSS_SELECTOR, QuoteLocators.AUTHOR).text
        '''
        return tags as a list of strings
        '''

    @property
    def tag(self):
        return [tag.string for tag in self.parent.find_element(By.CSS_SELECTOR, QuoteLocators.TAGS)]