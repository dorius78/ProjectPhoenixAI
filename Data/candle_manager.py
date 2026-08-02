"""
========================================
PROJECT PHOENIX AI
Candle Manager
Versione 8.0
========================================
"""

import yfinance as yf

from Logs.logger import Logger


class CandleManager:

    def __init__(self):

        Logger.success("Candle Manager V8 inizializzato.")

    # =====================================
    # DOWNLOAD
    # =====================================

    def _download(self, symbol, period, interval):

        try:

            Logger.info(
                f"Download dati {symbol} ({period} - {interval})"
            )

            ticker = yf.Ticker(symbol)

            data = ticker.history(

                period=period,

                interval=interval

            )

            if data is None or data.empty:

                Logger.warning("Nessun dato ricevuto.")

                return None

            Logger.success(
                f"Candele ricevute: {len(data)}"
            )

            return data

        except Exception as e:

            Logger.error(f"Errore download dati: {e}")

            return None

    # =====================================
    # LIVE
    # =====================================

    def get_candles(
        self,
        symbol,
        period="5d",
        interval="1h"
    ):

        return self._download(
            symbol,
            period,
            interval
        )

    # =====================================
    # BACKTEST
    # =====================================

    def get_backtest_data(
        self,
        symbol,
        period="1y",
        interval="1h"
    ):

        return self._download(
            symbol,
            period,
            interval
        )

    # =====================================
    # CUSTOM
    # =====================================

    def get_custom_data(
        self,
        symbol,
        period,
        interval
    ):

        return self._download(
            symbol,
            period,
            interval
        )

    # =====================================
    # ULTIMA CANDELA
    # =====================================

    def last_candle(self, data):

        return data.iloc[-1]

    # =====================================
    # MASSIMO RECENTE
    # =====================================

    def recent_high(self, data, bars=20):

        return float(
            data["High"].tail(bars).max()
        )

    # =====================================
    # MINIMO RECENTE
    # =====================================

    def recent_low(self, data, bars=20):

        return float(
            data["Low"].tail(bars).min()
        )

    # =====================================
    # RANGE MEDIO
    # =====================================

    def average_range(self, data, bars=20):

        rng = data["High"] - data["Low"]

        return float(
            rng.tail(bars).mean()
        )

    # =====================================
    # TREND PREZZO
    # =====================================

    def price_direction(self, data):

        first = float(data["Close"].iloc[0])

        last = float(data["Close"].iloc[-1])

        if last > first:

            return "UP"

        if last < first:

            return "DOWN"

        return "SIDEWAYS"