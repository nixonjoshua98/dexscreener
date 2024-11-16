from dexscreener import DexscreenerClient, DexscreenerClientV1
import asyncio

async def main():
    client = DexscreenerClient()

    pair = await client.get_token_pair_list_async("ethereum", (
    	"0xC2aDdA861F89bBB333c90c492cB837741916A225",
    	"0x7BeA39867e4169DBe237d55C8242a8f2fcDcc387") );
    
    
    pair = await client.get_token_pair_async("harmony", "0xcd818813f038a4d1a27c84d24d74bbc21551fa83")

    pairs = await client.get_token_pairs_async("0x2170Ed0880ac9A755fd29B2688956BD959F933F8")

    search = await client.search_pairs_async("WBTC")

    client_v1 = DexscreenerClientV1()

    token_profiles = client_v1.get_latest_token_profiles()

    boosted_tokens = client_v1.get_latest_boosted_tokens()

    most_active_tokens = client_v1.get_tokens_most_active()
    
    paid_of_orders = client_v1.get_orders_paid_of_token("solana", "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v")

    pair = await client_v1.get_token_pair_async("harmony", "0xcd818813f038a4d1a27c84d24d74bbc21551fa83")

    pairs = await client_v1.get_token_pairs_async("0x2170Ed0880ac9A755fd29B2688956BD959F933F8")

    pairs = await client_v1.get_token_pair_list_async("ethereum", (
    	"0xC2aDdA861F89bBB333c90c492cB837741916A225",
    	"0x7BeA39867e4169DBe237d55C8242a8f2fcDcc387"))

    search = await client_v1.search_pairs_async("WBTC")
    

asyncio.get_event_loop().run_until_complete(main())
