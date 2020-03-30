import aiohttp
import asyncio
import time

async def fetch_page(url):
    start=time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"Page took {time.time()-start} sec")
            return response.status

loop=asyncio.get_event_loop()
tasks=[fetch_page("http://google.com") for i in range(50)]
start=time.time()
loop.run_until_complete(asyncio.gather(*tasks))
print(f"All took {time.time()-start} sec..")