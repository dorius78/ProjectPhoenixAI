"""
========================================
PROJECT PHOENIX AI
Smart Money
Versione 8.0
========================================
"""

from Logs.logger import Logger


class SmartMoney:

    def __init__(self):

        Logger.success("Smart Money V8 inizializzato.")

    # =====================================
    # BREAK OF STRUCTURE
    # =====================================

    def detect_bos(self, data, lookback=20):

        highs = data["High"].tail(lookback)
        lows = data["Low"].tail(lookback)

        last_close = float(data["Close"].iloc[-1])

        highest = float(highs.max())
        lowest = float(lows.min())

        bullish = last_close > highest
        bearish = last_close < lowest

        return {

            "bos_bullish": bullish,

            "bos_bearish": bearish

        }

    # =====================================
    # CHANGE OF CHARACTER
    # =====================================

    def detect_choch(self, data):

        if len(data) < 3:

            return False

        last = float(data["Close"].iloc[-1])
        prev = float(data["Close"].iloc[-2])

        return abs(last - prev) > 0

    # =====================================
    # FAIR VALUE GAP
    # =====================================

    def detect_fvg(self, data):

        return False

    # =====================================
    # ORDER BLOCK
    # =====================================

    def detect_order_block(self, data):

        return False

    # =====================================
    # LIQUIDITY
    # =====================================

    def detect_liquidity(self, data):

        return False