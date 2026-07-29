"""
========================================
PROJECT PHOENIX AI
ATR Indicator
Versione 1.1
========================================
"""

from Config.settings import ATR_PERIOD
from Logs.logger import Logger


class ATR:

    def __init__(self):

        Logger.success("ATR Indicator inizializzato.")

    def calculate(self, data, period=ATR_PERIOD):

        high = data["High"]
        low = data["Low"]
        close = data["Close"]

        previous_close = close.shift(1)

        tr1 = high - low
        tr2 = (high - previous_close).abs()
        tr3 = (low - previous_close).abs()

        true_range = tr1.combine(tr2, max).combine(tr3, max)

        atr = true_range.rolling(
            window=period
        ).mean()

        return atr