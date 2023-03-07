from selenium.webdriver.common.by import By # self.browser.find_elements(By.CSS_SELECTOR, locator)
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from typing import List

from parsers.quote import QuoteParser
from locators.quotes_page_locators import QuotePageLocator


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def all_quotes(self) -> List[QuoteParser]:
        '''
        Find all quotes
        Create a list of QuoteParser objects.
        QuoteParser objects are created by looping through each quote 
        and passing the quote as the parent into the QuoteParser constructor
        '''
        locator = QuotePageLocator.QUOTE
        quotes = self.browser.find_elements(By.CSS_SELECTOR, locator)
        return [QuoteParser(quote) for quote in quotes]
    
    @property
    def author_dropdown(self) -> Select:
        locator = QuotePageLocator.AUTHOR_DROPDOWN
        element = self.browser.find_element(By.CSS_SELECTOR, locator)
        return Select(element)
    
    @property
    def tags_dropdown(self):
        locator = QuotePageLocator.TAG_DROPDOWN
        element = self.browser.find_element(By.CSS_SELECTOR, locator)
        return Select(element)
    
    @property
    def search_button(self): 
        return self.browser.find_element(By.CSS_SELECTOR, QuotePageLocator.SEARCH_BUTTON)

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)
    
    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tags_dropdown.options]
    
    def select_tag(self, tag_name: str):
        self.tags_dropdown.select_by_visible_text(tag_name)

    def search_for_quotes(self, author: str, tag: str) -> List[QuoteParser]:
        self.select_author(author)

        WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located(By.CSS_SELECTOR, QuotePageLocator.TAG_DROPDOWN_VALUE_OPTION)
        )

        try:
            self.select_tag(tag)
        except NoSuchElementException:
            raise InvalidTagForAuthorError(f'Author {author} does not have any quote tagged with {tag}')
        self.search_button.click()
        return self.all_quotes
    
class InvalidTagForAuthorError(ValueError):
    pass