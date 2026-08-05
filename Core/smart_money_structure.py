"""
========================================
PROJECT PHOENIX AI
Smart Money Structure
Versione 1.0
========================================
"""

from Logs.logger import Logger


class SmartMoneyStructure:

    def __init__(self):

        Logger.success(
            "Smart Money Structure V1 inizializzato."
        )

    def detect_bos(self, data, lookback=20):

        highs = data["High"].tail(lookback)
        lows = data["Low"].tail(lookback)

        last_close = float(data["Close"].iloc[-1])

        highest = float(highs.max())
        lowest = float(lows.min())

        return {

            "bos_bullish": last_close > highest,

            "bos_bearish": last_close < lowest

        }

    def detect_choch(self, data):

        if len(data) < 5:

            return False

        last = float(data["Close"].iloc[-1])
        prev = float(data["Close"].iloc[-2])
        prev2 = float(data["Close"].iloc[-3])

        bullish = prev < prev2 and last > prev
        bearish = prev > prev2 and last < prev

        return bullish or bearish