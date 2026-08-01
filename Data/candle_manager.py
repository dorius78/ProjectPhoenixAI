"""
========================================
PROJECT PHOENIX AI
Candle Manager
Versione 7.0
========================================
"""

import yfinance as yf

from Logs.logger import Logger


class CandleManager:

    def __init__(self):

        Logger.success("Candle Manager V7 inizializzato.")

    # =====================================
    # DOWNLOAD DATI
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

            Logger.error(
                f"Errore download dati: {e}"
            )

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
    # PERSONALIZZATI
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