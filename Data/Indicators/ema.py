"""
========================================
PROJECT PHOENIX AI
EMA Indicator
Versione 1.0
========================================
"""

from Config.settings import EMA_PERIOD


class EMA:

    def __init__(self):

        print("EMA Indicator inizializzato.")

    def calculate(self, data, period=EMA_PERIOD):

        ema = data["Close"].ewm(
            span=period,
            adjust=False
        ).mean()

        return ema