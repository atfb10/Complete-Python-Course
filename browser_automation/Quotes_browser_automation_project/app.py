from selenium import webdriver
from selenium.webdriver.common.by import By # self.browser.find_elements(By.CSS_SELECTOR, locator)

from pages.quote_page import InvalidTagForAuthorError, QuotesPage

try:
    author = input("Enter Author: ")
    selected_tag = input("Enter Your Tag: ")

    # Chrome instance for quotes page
    chrome = webdriver.Chrome(executable_path="C:\\Users\\afore\\chromedriver_win32\\chromedriver.exe")
    chrome.get('http://quotes.toscrape.com/search.aspx')
    quotes_page = QuotesPage(chrome)

    print(quotes_page.search_for_quotes(author, selected_tag))

except InvalidTagForAuthorError as e:
    print(e)

except Exception as e:
    print(e)
    print("an unknown error occurred")