import asyncio
import aiohttp
import async_timeout
import logging
import requests

from pages.book_page import BookPage

awesome_logging_format = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
logging.basicConfig(format=awesome_logging_format, level=logging.INFO, filename='logs.txt')    
logger = logging.getLogger('scraper')
logger.info('Loading books list...')

url = 'https://books.toscrape.com'
page_content = requests.get(url).content
page = BookPage(page_content)
loop = asyncio.get_event_loop()
books = []

async def fetch_page(session, url: str):
    async with async_timeout.timeout(30):
        async with session.get(url) as response:
            return await response.text()
        
async def get_multiple_pages(loop, urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks
    
urls = [f'https://books.toscrape.com/catalogue/page-{page_num}.html' for page_num in range(1, page.page_count + 1)]
pages = loop.run_until_complete(get_multiple_pages(loop, urls))

for page_content in pages:
    logger.debug('Creating AllBooksPage from page content')
    page = BookPage(page_content)
    books.extend(page_content)    

logger.info('Books list scraped')