import requests

from pages.quote_page import QuotesPage

url = 'https://quotes.toscrape.com/'
page_content = requests.get(url).content
quotes = QuotesPage(page_content)

for quote in quotes.all_quotes:
    print(quote.content)