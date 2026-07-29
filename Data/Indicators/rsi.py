"""
========================================
PROJECT PHOENIX AI
RSI Indicator
Versione 1.0
========================================
"""

from Config.settings import RSI_PERIOD


class RSI:

    def __init__(self):

        print("RSI Indicator inizializzato.")

    def calculate(self, data, period=RSI_PERIOD):

        delta = data["Close"].diff()

        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(window=period).mean()
        avg_loss = loss.rolling(window=period).mean()

        rs = avg_gain / avg_loss

        rsi = 100 - (100 / (1 + rs))

        return rsi