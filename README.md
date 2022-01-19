# Python Wrapper for 'dexscreener.com'
###### Pull requests GREATLY encouraged!

```python
from dexscreener import DexscreenerClient

client = DexscreenerClient()

history = client.get_recent_trade_history("harmony", "0xfb305344b1b9c8b57b1fa80ebb8a6548490a15ea")

print(history)

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
    ), 
    ...         
"""
```