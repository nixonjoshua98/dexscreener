from dexscreener import DexscreenerClient

import asyncio


async def main():
    client = DexscreenerClient()

    pair = await client.get_token_pair_async("harmony", "0xcd818813f038a4d1a27c84d24d74bbc21551fa83")

    pairs = await client.get_token_pairs_async("0x2170Ed0880ac9A755fd29B2688956BD959F933F8")

    search = await client.search_pairs_async("WBTC")


asyncio.get_event_loop().run_until_complete(main())