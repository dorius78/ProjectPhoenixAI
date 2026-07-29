"""
========================================
PROJECT PHOENIX AI
Candle Manager
Versione 1.0
========================================
"""

import yfinance as yf

from Logs.logger import Logger


class CandleManager:

    def __init__(self):

        Logger.success("Candle Manager inizializzato.")

    # ==========================
    # DATI LIVE
    # ==========================

    def get_candles(
        self,
        symbol,
        period="5d",
        interval="1h"
    ):

        Logger.info(f"Scarico candele LIVE: {symbol}")

        ticker = yf.Ticker(symbol)

        data = ticker.history(
            period=period,
            interval=interval
        )

        Logger.value(
            "Candele scaricate",
            len(data)
        )

        return data

    # ==========================
    # DATI BACKTEST
    # ==========================

    def get_backtest_data(
        self,
        symbol,
        period="1y",
        interval="1h"
    ):

        Logger.info(f"Scarico dati BACKTEST: {symbol}")

        ticker = yf.Ticker(symbol)

        data = ticker.history(
            period=period,
            interval=interval
        )

        Logger.value(
            "Candele Backtest",
            len(data)
        )

        return data

    # ==========================
    # DATI PERSONALIZZATI
    # ==========================

    def get_custom_data(
        self,
        symbol,
        period,
        interval
    ):

        Logger.info(
            f"Scarico dati personalizzati: {symbol}"
        )

        ticker = yf.Ticker(symbol)

        data = ticker.history(
            period=period,
            interval=interval
        )

        Logger.value(
            "Candele",
            len(data)
        )

        return data