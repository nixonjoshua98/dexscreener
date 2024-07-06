from .models import TokenPair
from .http_client import HttpClient
from typing import Optional, Iterable, List

class DexscreenerClient:
    def __init__(self):
        self._client: HttpClient = HttpClient(100, 60)

    def get_token_pair(self, chain: str, address: str) -> Optional[TokenPair]:
        """
        Fetch a pair on the provided chain id

        https://api.dexscreener.io/latest/dex/pairs/bsc/0x7213a321F1855CF1779f42c0CD85d3D95291D34C

        :param chain: Chain id
        :param address: Token address
        :return:
            Response as TokenPair model
        """
        resp = self._client.request("GET", f"dex/pairs/{chain}/{address}")
        return TokenPair(**resp["pair"]) if resp["pair"] else None

    async def get_token_pair_async(self, chain: str, address: str) -> Optional[TokenPair]:
        """
        Async version of `get_token_pair`
        """
        resp = await self._client.request_async("GET", f"dex/pairs/{chain}/{address}")        
        return TokenPair(**resp["pair"]) if resp["pair"] else None

    def get_token_pair_list(self, chain: str, addresses: Iterable[str]) -> List[TokenPair]:
        """
        Fetch multiple pairs on the provided chain id

        https://api.dexscreener.com/latest/dex/pairs/ethereum/0xC2aDdA861F89bBB333c90c492cB837741916A225,0x7BeA39867e4169DBe237d55C8242a8f2fcDcc387
        
        :param chain: Chain id
        :param addresses: Iterable of token addresses (up to 30)
        :return:
            Response as list of TokenPair models
        """
        addresses_list = list(addresses)
        if len(addresses_list) > 30:
            raise ValueError("The maximum number of addresses allowed is 30.")
        resp = self._client.request("GET", f"dex/pairs/{chain}/{','.join(addresses_list)}")
        return [TokenPair(**pair) for pair in resp.get("pairs", [])]

    async def get_token_pair_list_async(self, chain: str, addresses: Iterable[str]) -> List[TokenPair]:
        """
        Async version of `get_token_pairs`
        """
        addresses_list = list(addresses)
        if len(addresses_list) > 30:
            raise ValueError("The maximum number of addresses allowed is 30.")
        resp = await self._client.request_async("GET", f"dex/pairs/{chain}/{','.join(addresses_list)}")
        return [TokenPair(**pair) for pair in resp.get("pairs", [])]    
    
    def get_token_pairs(self, address: str) -> list[TokenPair]:
        """
        Get pairs matching base token address

        https://api.dexscreener.io/latest/dex/tokens/0x2170Ed0880ac9A755fd29B2688956BD959F933F8

        :param address: Token address
        :return:
            Response as list of TokenPair model
        """
        resp = self._client.request("GET",  f"dex/tokens/{address}")        
        return [TokenPair(**pair) for pair in resp.get("pairs", [])]

    async def get_token_pairs_async(self, address: str) -> list[TokenPair]:
        """
        Async version of `get_token_pairs`
        """
        resp = await self._client.request_async("GET", f"dex/tokens/{address}")        
        return [TokenPair(**pair) for pair in resp.get("pairs", [])]

    def search_pairs(self, search_query: str) -> list[TokenPair]:
        """
        Search for pairs matching query

        https://api.dexscreener.io/latest/dex/tokens/0x2170Ed0880ac9A755fd29B2688956BD959F933F8

        :param search_query: query (e.g.: WBTC or WBTC/USDC)
        :return:
            Response as list of TokenPair model
        """
        resp = self._client.request("GET", f"dex/search/?q={search_query}")        
        return [TokenPair(**pair) for pair in resp.get("pairs", [])]

    async def search_pairs_async(self, search_query: str) -> list[TokenPair]:
        """
        Async version of `search_pairs`
        """
        resp = await self._client.request_async("GET", f"dex/search/?q={search_query}")        
        return [TokenPair(**pair) for pair in resp.get("pairs", [])]
