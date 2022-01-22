import contextlib
import datetime as dt
import threading
from typing import Optional, Tuple, Type

import pydantic
import requests

from .errors import DexscreenerException
from .models import (BaseModel, ChartBarsResponseModel,
                     TradeHistoryResponseModel)

HISTORY_URL = "https://io6.dexscreener.io/u/trading-history/recent/{network}/{address}"
CHART_BAR_URL = "https://io5.dexscreener.io/u/chart/bars/{network}/{address}?{daterange}&res=15&cb=2"


class BaseClient:

    @staticmethod
    def _try_parse_response(model: Type[BaseModel], data: dict) -> Optional[BaseModel]:
        """
        Try parse a Pydantic model from a dict, otherwise throw an exception

        :param model: Model class (subclass of Pydantic.BaseModel)
        :param data: Dict used to create the instance

        :return:
            Return the newly parsed model instance
        """
        with contextlib.suppress(pydantic.ValidationError):
            return model.parse_obj(data)

        raise DexscreenerException("Failed to parse response")

    @staticmethod
    def _create_daterange_string(from_: dt.datetime, to: dt.datetime):
        return f"from={int(from_.timestamp() * 1_000)}&to={int(to.timestamp() * 1_000)}"


class DexscreenerClient(BaseClient):
    def __init__(self):
        self._lock = threading.Lock()

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

        code, data = self._try_get(url)

        return self._try_parse_response(ChartBarsResponseModel, data)

    def recent_trade_history(self, network: str, address: str) -> Optional[TradeHistoryResponseModel]:
        """
        Fetch data from the 'trading-history/recent/' endpoint

        :param network: Network name as it appears in the URL
        :param address: Pair address

        :return:
            Return the response model
        """
        code, data = self._try_get(HISTORY_URL.format(network=network, address=address))

        return self._try_parse_response(TradeHistoryResponseModel, data)

    def _try_get(self, url: str) -> Tuple[int, dict]:
        """
        Attempt sending a GET request, otherwise throw an exception

        :param url: URL to send the request to

        :return:
            Return the status code and JSON as a dict
        """
        with self._lock, contextlib.suppress(requests.RequestException):
            r = requests.get(url)
            return r.status_code, r.json()

        raise DexscreenerException("Failed to send request")

