import aiohttp
import asyncio
import time


async def fetch_page(session, url):
    start = time.time()
    async with session.get(url) as response:
        print(f"page took {time.time() - start}")
        return response.status


async def get_multiple_pages(loop,*urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


loop = asyncio.get_event_loop()
urls = ['http://google.com' for i in range(50)]

loop.run_until_complete(get_multiple_pages(loop,*urls))
