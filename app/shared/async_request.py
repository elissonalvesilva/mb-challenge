import asyncio
import aiohttp
import re


async def gather_with_concurrency(n, *tasks):
    semaphore = asyncio.Semaphore(n)

    async def sem_task(task):
        async with semaphore:
            return await task

    return await asyncio.gather(*(sem_task(task) for task in tasks))


async def get_async(url, session, results):

    try:
        pair = re.search('v4/(.+?)/candle', url).group(1)
    except AttributeError:
        pair = 'BRLBTC'
    async with session.get(url) as response:
        obj = await response.text()
        results[pair] = obj


async def process_requests(urls, response):
    conn = aiohttp.TCPConnector(limit=None, ttl_dns_cache=300)
    session = aiohttp.ClientSession(connector=conn)

    conc_req = len(urls)
    await gather_with_concurrency(conc_req, *[get_async(i, session, response) for i in urls])

    await session.close()



def async_requests(urls, response):
    asyncio.run(process_requests(urls, response))
