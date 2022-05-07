import datetime as dt
from typing import Union

import requests

from .models import TokenPair
from .ratelimit import RateLimiter


class BaseClient:
    base_url = "https://api.dexscreener.io/latest"

    def __init__(self):
        self._limiter = RateLimiter(100, 60)  # 100 requests per 60 seconds

    def request(self, method, url, **kwargs) -> Union[list, dict]:
        with self._limiter:
            r = requests.request(method, url, **kwargs)

            return r.json()


class DexscreenerClient(BaseClient):
    def get_token_pair(self, chain: str, address: str) -> TokenPair:
        """
        Fetch a pair on the provided chain id

        https://api.dexscreener.io/latest/dex/pairs/bsc/0x7213a321F1855CF1779f42c0CD85d3D95291D34C

        :param chain: Chain id
        :param address: Token address
        :return:
            Response as TokenPair model
        """
        url = f"{self.base_url}/dex/pairs/{chain}/{address}"

        resp = self.request("GET", url)

        return TokenPair.parse_obj(resp["pair"])

    def get_token_pairs(self, address: str) -> list[TokenPair]:
        """
        Get pairs matching base token address

        https://api.dexscreener.io/latest/dex/tokens/0x2170Ed0880ac9A755fd29B2688956BD959F933F8

        :param address: Token address
        :return:
            Response as list of TokenPair model
        """
        url = f"{self.base_url}/dex/tokens/{address}"

        resp = self.request("GET", url)

        return [TokenPair.parse_obj(pair) for pair in resp["pairs"]]

    def search_pairs(self, search_query: str) -> list[TokenPair]:
        """
        Search for pairs matching query

        https://api.dexscreener.io/latest/dex/tokens/0x2170Ed0880ac9A755fd29B2688956BD959F933F8

        :param search_query: query (e.g.: WBTC or WBTC/USDC)
        :return:
            Response as list of TokenPair model
        """
        url = f"{self.base_url}/dex/search/?q={search_query}"

        resp = self.request("GET", url)

        return [TokenPair.parse_obj(pair) for pair in resp["pairs"]]
