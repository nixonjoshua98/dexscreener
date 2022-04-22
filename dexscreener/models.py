from pydantic import BaseModel, Field
from typing import Optional
import datetime as dt


class TimestampDatetime:

    @classmethod
    def __get_validators__(cls):
        yield lambda val: dt.datetime.utcfromtimestamp(val / 1000.0) if val is not None else val


class BaseToken(BaseModel):
    address: str
    name: str
    symbol: str


class QuoteToken(BaseModel):
    symbol: str


class TransactionCount(BaseModel):
    buys: int
    sells: int


class PairTransactionCounts(BaseModel):
    m5: TransactionCount
    h1: TransactionCount
    h6: TransactionCount
    h24: TransactionCount


class _TimePeriodsFloat(BaseModel):
    m5: Optional[float] = 0.0
    h1: Optional[float] = 0.0
    h6: Optional[float] = 0.0
    h24: Optional[float] = 0.0


class VolumePeriods(_TimePeriodsFloat):
    ...


class PriceChangePeriods(_TimePeriodsFloat):
    ...


class Liquidity(BaseModel):
    usd: Optional[float] = None
    base: float
    quote: float


class TokenPair(BaseModel):
    chain_id: str = Field(..., alias="chainId")
    dex_id: str = Field(..., alias="dexId")
    url: str
    pair_address: str = Field(..., alias="pairAddress")
    base_token: BaseToken = Field(..., alias="baseToken")
    quote_token: QuoteToken = Field(..., alias="quoteToken")
    price_native: float = Field(..., alias="priceNative")
    price_usd: Optional[float] = Field(None, alias="priceUsd")
    transactions: PairTransactionCounts = Field(..., alias="txns")
    volume: VolumePeriods
    price_change: PriceChangePeriods = Field(..., alias="priceChange")
    liquidity: Optional[Liquidity] = None
    fdv: Optional[float] = 0.0
    pair_created_at: Optional[TimestampDatetime] = Field(None, alias="pairCreatedAt")


# = Unofficial endpoint models

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