import requests
from typing import Optional
from .models import TradeHistoryResponseModel

HISTORY_URL = "https://io6.dexscreener.io/u/trading-history/recent/{network}/{address}"


class DexscreenerClient:

    def get_recent_trade_history(self, network, address) -> Optional[TradeHistoryResponseModel]:
        url = HISTORY_URL.format(network=network, address=address)

        r = requests.get(url)

        return self._create_trade_history_model(r.json())

    def _create_trade_history_model(self, data: dict):
        cls = {
            "1.2.2": TradeHistoryResponseModel
        }.get(data.get("schemaVersion"))

        return cls.parse_obj(data) if cls is not None else None
