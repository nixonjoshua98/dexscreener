# Python Wrapper for 'dexscreener.com'
###### Pull requests GREATLY encouraged!

```python
import datetime as dt

from dexscreener import DexscreenerClient

client = DexscreenerClient()

history = client.recent_trade_history("harmony", "0xcd818813f038a4d1a27c84d24d74bbc21551fa83")

"""
schema_verion='1.2.2' 
base_token_symbol='WAIFU' 
quote_token_symbol='WONE' 
trade_history=[
    TradeHistoryEntryModel(
        block=21906751, 
        block_timestamp=1642611592000, 
        txn_hash='0xf5bae798e7bebb3692816e0baed6756cf2444c53200e9879d6f37ed39a0926a4', 
        log_index=92, 
        type='sell', 
        price_usd=0.0001172, 
        volume_usd=11.72,
        token0_amount=100000.0, 
        token1_amount=40.25
    ), ...
]     
"""

bars = client.chart_bars(
    "harmony",
    "0xcd818813f038a4d1a27c84d24d74bbc21551fa83",
    dt.datetime.utcnow() - dt.timedelta(seconds=30),
    dt.datetime.utcnow()
)

"""
schema_verion='1.2.2' 
bars=[
    ChartBarModel(
        timestamp=1642860000000,
        open=21.697709, 
        open_usd=4.164694, 
        high=23.567648, 
        high_usd=4.496434, 
        low=21.477209, 
        low_usd=4.085605, 
        close=23.567265, 
        close_usd=4.496434, 
        volume_usd=16105.27
    ), ...
]
"""
```