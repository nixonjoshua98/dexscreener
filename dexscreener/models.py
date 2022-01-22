from pydantic import BaseModel, Field


# Fields =

class NumberField(int):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        v = v.replace(",", "")

        return float(v)


# Trade History Models #

class TradeHistoryEntryModel(BaseModel):
    block: int = Field(..., alias="blockNumber")
    block_timestamp: int = Field(..., alias="blockTimestamp")
    txn_hash: str = Field(..., alias="txnHash")
    log_index: int = Field(..., alias="logIndex")
    type: str = Field(..., alias="type")
    price_usd: NumberField = Field(..., alias="priceUsd")
    volume_usd: NumberField = Field(..., alias="volumeUsd")
    token0_amount: NumberField = Field(..., alias="amount0")
    token1_amount: NumberField = Field(..., alias="amount1")


class TradeHistoryResponseModel(BaseModel):
    schema_verion: str = Field(..., alias="schemaVersion")

    base_token_symbol: str = Field([], alias="baseTokenSymbol")
    quote_token_symbol: str = Field([], alias="quoteTokenSymbol")
    trade_history: list[TradeHistoryEntryModel] = Field([], alias="tradingHistory")


# Chart Bars #

class ChartBarModel(BaseModel):
    timestamp: int = Field(..., alias="timestamp")
    open: NumberField = Field(..., alias="open")
    open_usd: NumberField = Field(..., alias="openUsd")
    high: NumberField = Field(..., alias="high")
    high_usd: NumberField = Field(..., alias="highUsd")
    low: NumberField = Field(..., alias="low")
    low_usd: NumberField = Field(..., alias="lowUsd")
    close: NumberField = Field(..., alias="close")
    close_usd: NumberField = Field(..., alias="closeUsd")
    volume_usd: NumberField = Field(..., alias="volumeUsd")


class ChartBarsResponseModel(BaseModel):
    schema_verion: str = Field(..., alias="schemaVersion")
    bars: list[ChartBarModel] = Field([], alias="bars")