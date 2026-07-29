"""
========================================
PROJECT PHOENIX AI
SMA Indicator
Versione 1.0
========================================
"""

from Config.settings import SMA_PERIOD


class SMA:

    def __init__(self):

        print("SMA Indicator inizializzato.")

    def calculate(self, data, period=SMA_PERIOD):

        sma = data["Close"].rolling(
            window=period
        ).mean()

        return sma