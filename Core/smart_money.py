"""
========================================
PROJECT PHOENIX AI
Smart Money
Versione 9.0
========================================
"""

from Logs.logger import Logger


class SmartMoney:

    def __init__(self):

        Logger.success("Smart Money V9 inizializzato.")

    # =====================================
    # BREAK OF STRUCTURE
    # =====================================

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

    # =====================================
    # CHANGE OF CHARACTER
    # =====================================

    def detect_choch(self, data):

        if len(data) < 5:

            return False

        last = float(data["Close"].iloc[-1])
        prev = float(data["Close"].iloc[-2])
        prev2 = float(data["Close"].iloc[-3])

        bullish = prev < prev2 and last > prev
        bearish = prev > prev2 and last < prev

        return bullish or bearish

    # =====================================
    # FAIR VALUE GAP
    # =====================================

    def detect_fvg(self, data):

        if len(data) < 3:

            return False

        high_1 = float(data["High"].iloc[-3])
        low_3 = float(data["Low"].iloc[-1])

        low_1 = float(data["Low"].iloc[-3])
        high_3 = float(data["High"].iloc[-1])

        bullish_gap = low_3 > high_1
        bearish_gap = high_3 < low_1

        return bullish_gap or bearish_gap

    # =====================================
    # ORDER BLOCK
    # =====================================

    def detect_order_block(self, data):

        if len(data) < 5:

            return False

        candle = data.iloc[-2]

        body = abs(

            float(candle["Close"])

            -

            float(candle["Open"])

        )

        range_size = (

            float(candle["High"])

            -

            float(candle["Low"])

        )

        if range_size == 0:

            return False

        return body < (range_size * 0.30)

    # =====================================
    # LIQUIDITY SWEEP
    # =====================================

    def detect_liquidity(self, data):

        if len(data) < 10:

            return False

        last_high = float(data["High"].iloc[-1])

        previous_high = float(

            data["High"].iloc[-10:-1].max()

        )

        last_close = float(data["Close"].iloc[-1])

        return (

            last_high > previous_high

            and

            last_close < previous_high

        )