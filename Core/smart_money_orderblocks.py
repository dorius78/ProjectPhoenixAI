"""
========================================
PROJECT PHOENIX AI
Smart Money Order Blocks
Versione 1.0
========================================
"""

from Logs.logger import Logger


class SmartMoneyOrderBlocks:

    def __init__(self):

        Logger.success(
            "Smart Money Order Blocks V1 inizializzato."
        )

    def detect(self, data):

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