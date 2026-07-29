"""
========================================
PROJECT PHOENIX AI
MACD Indicator
Versione 1.0
========================================
"""

from Config.settings import (
    MACD_FAST,
    MACD_SLOW,
    MACD_SIGNAL
)


class MACD:

    def __init__(self):

        print("MACD Indicator inizializzato.")

    def calculate(
        self,
        data,
        fast=MACD_FAST,
        slow=MACD_SLOW,
        signal=MACD_SIGNAL
    ):

        ema_fast = data["Close"].ewm(
            span=fast,
            adjust=False
        ).mean()

        ema_slow = data["Close"].ewm(
            span=slow,
            adjust=False
        ).mean()

        macd = ema_fast - ema_slow

        signal_line = macd.ewm(
            span=signal,
            adjust=False
        ).mean()

        histogram = macd - signal_line

        return macd, signal_line, histogram