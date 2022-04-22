import datetime as dt
from typing import Optional, Union

import requests

from .models import (ChartBarsResponseModel,
                     TradeHistoryResponseModel, TokenPair)
from .ratelimit import RateLimiter

HISTORY_URL = "https://io6.dexscreener.io/u/trading-history/recent/{network}/{address}"
CHART_BAR_URL = "https://io5.dexscreener.io/u/chart/bars/{network}/{address}?{daterange}&res=15&cb=2"


class BaseClient:
    base_url = "https://api.dexscreener.io/latest"

    def __init__(self):
        self._limiter = RateLimiter(100, 60)  # 100 requests per 60 seconds

    def request(self, method, url, **kwargs) -> Union[list, dict]:
        with self._limiter:
            r = requests.request(method, url, **kwargs)

            return r.json()

    @staticmethod
    def _create_daterange_string(from_: dt.datetime, to: dt.datetime):
        return f"from={int(from_.timestamp() * 1_000)}&to={int(to.timestamp() * 1_000)}"


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

    def chart_bars(
        self,
        network: str,
        address: str,
        from_: dt.datetime,
        to: dt.datetime
    ) -> Optional[ChartBarsResponseModel]:
        """
        Fetch data from the 'chart/bars/' endpoint

        :param network: Network name as it appears in the URL
        :param address: Pair address
        :param from_: Start date for the chart bars
        :param to: End date for the chart bars

        :return:
            Return the response model
        """
        url = CHART_BAR_URL.format(
            network=network,
            address=address,
            daterange=self._create_daterange_string(from_, to)
        )

        resp = self.request("GET", url)

        return ChartBarsResponseModel.parse_obj(resp)

    def recent_trade_history(self, network: str, address: str) -> Optional[TradeHistoryResponseModel]:
        """
        Fetch data from the 'trading-history/recent/' endpoint

        :param network: Network name as it appears in the URL
        :param address: Pair address

        :return:
            Return the response model
        """
        url = HISTORY_URL.format(
            network=network,
            address=address
        )

        resp = self.request("GET", url)

        return TradeHistoryResponseModel.parse_obj(resp)
