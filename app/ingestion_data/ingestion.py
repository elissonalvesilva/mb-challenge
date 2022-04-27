from typing import List
from config.settings import MB_FAKE_URL
from shared.async_request import async_requests

def make_urls(pairs) -> List[str]:
    url = MB_FAKE_URL
    return [url.replace('<PAIR>', pair) + '?from=4564&to=244&precision=2d' for pair in pairs]

def request_data():
    response = {}
    pairs = ['BRLBTC', 'BRLETH']
    urls = make_urls(pairs)
    async_requests(urls, response)

