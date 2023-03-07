import logging
from requests import get

from pages.book_page import BookPage

awesome_logging_format = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
logging.basicConfig(format=awesome_logging_format, level=logging.INFO, filename='logs.txt')    
logger = logging.getLogger('scraper')
logger.info('Loading books list...')

url = 'https://books.toscrape.com'
page_content = get(url).content
page = BookPage(page_content)
books = []

# Get all pages of books (there are 50. 1 - 50). Then get all books
for page_num in range(1, page.page_count + 1):
    url = f'https://books.toscrape.com/catalogue/page-{page_num}.html'
    page_content = get(url).content
    book_page_obj = BookPage(page_content)
    books.extend(book_page_obj.get_books)

logger.info('Books list scraped')