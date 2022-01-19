from pydantic import BaseModel, Field


class _NumberField(int):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        v = v.replace(",", "")

        return float(v)


class TradeHistoryEntryModel(BaseModel):
    block: int = Field(..., alias="blockNumber")
    block_timestamp: int = Field(..., alias="blockTimestamp")
    txn_hash: str = Field(..., alias="txnHash")
    log_index: int = Field(..., alias="logIndex")
    type: str = Field(..., alias="type")
    price_usd: float = Field(..., alias="priceUsd")
    volume_usd: float = Field(..., alias="volumeUsd")
    token0_amount: _NumberField = Field(..., alias="amount0")
    token1_amount: _NumberField = Field(..., alias="amount1")


class TradeHistoryResponseModel(BaseModel):
    schema_verion: str = Field(..., alias="schemaVersion")

    base_token_symbol: str = Field([], alias="baseTokenSymbol")
    quote_token_symbol: str = Field([], alias="quoteTokenSymbol")
    trade_history: list[TradeHistoryEntryModel] = Field([], alias="tradingHistory")
