from selenium import webdriver
from selenium.webdriver.common.by import By # self.browser.find_elements(By.CSS_SELECTOR, locator)

from pages.quote_page import QuotesPage

# Chrome instance for quotes page
chrome = webdriver.Chrome(executable_path="C:\\Users\\afore\\chromedriver_win32\\chromedriver.exe")

# I do not know why it says that the code is unreachable. It works fine! Just as intended
chrome.get('http://quotes.toscrape.com/search.aspx')
quotes = QuotesPage(chrome)

for quote in quotes.all_quotes:
    print(quote)