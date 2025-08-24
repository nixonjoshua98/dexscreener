from .models import TokenPair, TokenInfo, OrderInfo
from .http_client import HttpClient
from typing import Optional, Iterable, List
import json


class DexscreenerClient:
    def __init__(self) -> None:
        self._client_60rpm: HttpClient = HttpClient(60, 60, base_url="https://api.dexscreener.com")
        self._client_300rpm: HttpClient = HttpClient(300, 60, base_url="https://api.dexscreener.com/latest")

    def get_latest_token_profiles(self) -> list[TokenInfo]:
        """
        Get the latest token profiles

        https://api.dexscreener.com/token-profiles/latest/v1

        :return:
            Response as list of TokenInfo model
        """
        resp = self._client_60rpm.request("GET", "token-profiles/latest/v1")
        return [TokenInfo(**token) for token in resp]

    async def get_latest_token_profiles_async(self) -> list[TokenInfo]:
        """
        Async version of `get_latest_token_profiles`
        """
        resp = await self._client_60rpm.request_async("GET", "token-profiles/latest/v1")
        return [TokenInfo(**token) for token in resp]

    def get_latest_boosted_tokens(self) -> list[TokenInfo]:
        """
        Get the latest boosted tokens

        https://api.dexscreener.com/token-boosts/latest/v1

        :return:
            Response as list of TokenInfo model
        """
        resp = self._client_60rpm.request("GET", "token-boosts/latest/v1")
        return [TokenInfo(**token) for token in resp]
        
    async def get_latest_boosted_tokens_async(self) -> list[TokenInfo]:
        """
        Async version of `get_latest_boosted_tokens`
        """
        resp = await self._client_60rpm.request_async("GET", "token-boosts/latest/v1")
        return [TokenInfo(**token) for token in resp]

    def get_tokens_most_active(self) -> list[TokenInfo]:
        """
        Get the tokens with most active boosts

        https://api.dexscreener.com/token-boosts/top/v1

        :return:
            Response as list of TokenInfo model
        """
        resp = self._client_60rpm.request("GET", "token-boosts/top/v1")
        return [TokenInfo(**token) for token in resp]

    async def get_tokens_most_active_async(self) -> list[TokenInfo]:
        """
        Async version of `get_tokens_most_active`
        """
        resp = await self._client_60rpm.request_async("GET", "token-boosts/top/v1")
        return [TokenInfo(**token) for token in resp]

    def get_orders_paid_of_token(self, chain_id: str, token_address: str) -> list[OrderInfo]:
        """
        Check orders paid for of token

        https://api.dexscreener.com/orders/v1/solana/A55XjvzRU4KtR3Lrys8PpLZQvPojPqvnv5bJVHMYy3Jv

        :return:
            Response as list of OrderInfo model
        """
        resp = self._client_60rpm.request("GET", f"orders/v1/{chain_id}/{token_address}")
        return [OrderInfo(**order) for order in resp]
    
    async def get_orders_paid_of_token_async(self, chain_id: str, token_address: str) -> list[OrderInfo]:
        """
        Async version of `get_orders_paid_of_token`
        """
        resp = await self._client_60rpm.request_async("GET", f"orders/v1/{chain_id}/{token_address}")
        return [OrderInfo(**order) for order in resp]

    def get_token_pair(self, chain: str, address: str) -> Optional[TokenPair]:
        """
        Fetch a pair on the provided chain id

        https://api.dexscreener.com/latest/dex/pairs/bsc/0x7213a321F1855CF1779f42c0CD85d3D95291D34C

        :param chain: Chain id
        :param address: Token address
        :return:
            Response as TokenPair model
        """
        resp = self._client_300rpm.request("GET", f"dex/pairs/{chain}/{address}")
        return TokenPair(**resp["pair"]) if resp["pair"] else None

    async def get_token_pair_async(self, chain: str, address: str) -> Optional[TokenPair]:
        """
        Async version of `get_token_pair`
        """
        resp = await self._client_300rpm.request_async("GET", f"dex/pairs/{chain}/{address}")        
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
        resp = self._client_300rpm.request("GET", f"dex/pairs/{chain}/{','.join(addresses_list)}")
        return [TokenPair(**pair) for pair in resp.get("pairs", [])]

    async def get_token_pair_list_async(self, chain: str, addresses: Iterable[str]) -> List[TokenPair]:
        """
        Async version of `get_token_pairs`
        """
        addresses_list = list(addresses)
        if len(addresses_list) > 30:
            raise ValueError("The maximum number of addresses allowed is 30.")
        resp = await self._client_300rpm.request_async("GET", f"dex/pairs/{chain}/{','.join(addresses_list)}")
        return [TokenPair(**pair) for pair in resp.get("pairs", [])]    
    
    def get_token_pairs(self, address: str) -> list[TokenPair]:
        """
        Get pairs matching base token address

        https://api.dexscreener.com/latest/dex/tokens/0x2170Ed0880ac9A755fd29B2688956BD959F933F8

        :param address: Token address
        :return:
            Response as list of TokenPair model
        """
        resp = self._client_300rpm.request("GET",  f"dex/tokens/{address}")        
        return [TokenPair(**pair) for pair in resp.get("pairs", [])]

    async def get_token_pairs_async(self, address: str) -> list[TokenPair]:
        """
        Async version of `get_token_pairs`
        """
        resp = await self._client_300rpm.request_async("GET", f"dex/tokens/{address}")        
        return [TokenPair(**pair) for pair in resp.get("pairs", [])]

    def search_pairs(self, search_query: str) -> list[TokenPair]:
        """
        Search for pairs matching query

        https://api.dexscreener.com/latest/dex/tokens/0x2170Ed0880ac9A755fd29B2688956BD959F933F8

        :param search_query: query (e.g.: WBTC or WBTC/USDC)
        :return:
            Response as list of TokenPair model
        """
        resp = self._client_300rpm.request("GET", f"dex/search/?q={search_query}")        
        return [TokenPair(**pair) for pair in resp.get("pairs", [])]

    async def search_pairs_async(self, search_query: str) -> list[TokenPair]:
        """
        Async version of `search_pairs`
        """
        resp = await self._client_300rpm.request_async("GET", f"dex/search/?q={search_query}")        
        return [TokenPair(**pair) for pair in resp.get("pairs", [])]

    def get_pairs_by_token_addresses(
        self, chain_id: str, token_list: Iterable[str]
    ) -> list[TokenPair]:
        """
        Get token information for multiple tokens by chain and addresses

        :param chain_id: Chain id eg: solana
        :param token_list: Iterable of token addresses (up to 30) eg: [0x2170Ed0880ac9A755fd29B2688956BD959F933F8, 0x7BeA39867e4169DBe237d55C8242a8f2fcDcc387]
        :return:
            Response as list of TokenPair model
        """
        token_list_list = list(token_list)
        if len(token_list_list) > 30:
            raise ValueError("The maximum number of addresses allowed is 30.")

        csv_addresses = ",".join(token_list_list)  # TODO: improve validation

        # NOTE: this endpoint supports 300rpm however this is is not implemented, see: https://docs.dexscreener.com/api/reference#get-tokens-v1-chainid-tokenaddresses
        # TODO: Implement 300rpm
        resp = self._client_60rpm.request(
            "GET", f"tokens/v1/{chain_id}/{csv_addresses}"
        )
        return [TokenPair(**pair) for pair in resp]

    async def get_pairs_by_token_addresses_async(
        self, chain_id: str, token_list: Iterable[str]
    ) -> list[TokenPair]:
        """
        Async version of `get_pairs_by_token_addresses`

        :param chain_id: Chain id eg: solana
        :param token_list: Iterable of token addresses (up to 30) eg: [0x2170Ed0880ac9A755fd29B2688956BD959F933F8, 0x7BeA39867e4169DBe237d55C8242a8f2fcDcc387]
        :return:
            Response as list of TokenPair model
        """
        token_list_list = list(token_list)
        if len(token_list_list) > 30:
            raise ValueError("The maximum number of addresses allowed is 30.")

        csv_addresses = ",".join(token_list_list)
        resp = await self._client_60rpm.request_async(
            "GET", f"tokens/v1/{chain_id}/{csv_addresses}"
        )
        return [TokenPair(**pair) for pair in resp]

    def get_token_pairs_v1(self, chain_id: str, token_address: str) -> list[TokenPair]:
        """
        Get token pairs by token address

        https://api.dexscreener.com/token-pairs/v1/{chainId}/{tokenAddress}

        :param chain_id: Chain id eg: solana
        :param token_address: Token address eg: JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN
        :return:
            Response as list of TokenPair model
        """
        resp = self._client_60rpm.request(
            "GET", f"token-pairs/v1/{chain_id}/{token_address}"
        )
        return [TokenPair(**pair) for pair in resp]

    async def get_token_pairs_v1_async(
        self, chain_id: str, token_address: str
    ) -> list[TokenPair]:
        """
        Async version of `get_token_pairs_v1`
        """
        resp = await self._client_60rpm.request_async(
            "GET", f"token-pairs/v1/{chain_id}/{token_address}"
        )
        return [TokenPair(**pair) for pair in resp]
