import aiohttp
import async_timeout
import asyncio
import time

# Suspend execution while waiting. Resume execution when done waiting
async def fetch_page(session, url: str):
    page_start = time.time()
    async with async_timeout.timeout(30):
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start} seconds')
            return response.status
        
async def get_multiple_pages(loop, urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

loop = asyncio.get_event_loop()
urls = ['http://google.com' for i in range(50)]
start_time = time.time()
loop.run_until_complete(get_multiple_pages(loop, urls))
print(f'All took {time.time() - start_time} seconds')