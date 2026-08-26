"""
PROJECT PHOENIX AI
Market Provider

Routing:
- DEMO / PAPER -> Yahoo Finance
- MT5 -> MetaTrader 5

Il provider MT5 viene usato quando richiesto
esplicitamente dal percorso MT5.
"""

from Config.settings import MODE

from Data.yfinance_provider import YFinanceProvider


class MarketProvider:

    def __init__(self, use_mt5=None):

        self.use_mt5 = (
            str(MODE).upper() == "LIVE"
            if use_mt5 is None
            else bool(use_mt5)
        )

        if self.use_mt5:

            from Data.mt5_provider import MT5Provider

            self.provider = MT5Provider()

            print(
                "Market Provider -> MT5"
            )

        else:

            self.provider = YFinanceProvider()

            print(
                "Market Provider -> Yahoo Finance"
            )

    def connect(self):

        if hasattr(
            self.provider,
            "connect"
        ):

            return self.provider.connect()

        return True

    def get_price(
        self,
        symbol
    ):

        return self.provider.get_price(
            symbol
        )

    def get_historical_data(
        self,
        symbol,
        period="5d",
        interval="1h"
    ):

        if self.use_mt5:

            if hasattr(
                self.provider,
                "get_historical_data"
            ):

                return self.provider.get_historical_data(
                    symbol,
                    period=period,
                    interval=interval
                )

            if hasattr(
                self.provider,
                "get_candles"
            ):

                return self.provider.get_candles(
                    symbol,
                    period=period,
                    interval=interval
                )

            raise RuntimeError(
                "MT5Provider non espone "
                "get_historical_data/get_candles."
            )

        return self.provider.get_historical_data(
            symbol,
            period=period,
            interval=interval
        )

    def disconnect(self):

        if hasattr(
            self.provider,
            "disconnect"
        ):

            return self.provider.disconnect()

        return True
