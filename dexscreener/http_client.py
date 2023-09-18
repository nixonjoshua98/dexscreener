import requests
from typing import Union
import aiohttp

from .ratelimit import RateLimiter


class HttpClient:
    base_url = "https://api.dexscreener.io/latest"

    def __init__(self, calls: int, period: int):
        self._limiter = RateLimiter(calls, period)

    def _create_absolute_url(self, relative: str) -> str:
        return f"{self.base_url}/{relative}"

    def request(self, method, url, **kwargs) -> Union[list, dict]:
        url = self._create_absolute_url(url)

        with self._limiter:
            r = requests.request(method, url, **kwargs)

            return r.json()

    async def request_async(self, method, url, **kwargs):
        url = self._create_absolute_url(url)

        async with self._limiter:
            async with aiohttp.ClientSession() as session:
                async with session.request(method, url, **kwargs) as response:
                    return await response.json()

