# Python Wrapper for 'dexscreener.com'
###### Pull requests GREATLY encouraged!

[![Downloads](https://pepy.tech/badge/dexscreener)](https://pepy.tech/project/dexscreener)

```python
import datetime as dt

from dexscreener import DexscreenerClient

client = DexscreenerClient()

pair = client.get_token_pair("harmony", "0xcd818813f038a4d1a27c84d24d74bbc21551fa83")

pairs = client.get_token_pairs("0x2170Ed0880ac9A755fd29B2688956BD959F933F8")

search = client.search_pairs("WBTC")

history = client.recent_trade_history("harmony", "0xcd818813f038a4d1a27c84d24d74bbc21551fa83")

bars = client.chart_bars(
    "harmony",
    "0xcd818813f038a4d1a27c84d24d74bbc21551fa83",
    dt.datetime.utcnow() - dt.timedelta(seconds=30),
    dt.datetime.utcnow()
)
```
