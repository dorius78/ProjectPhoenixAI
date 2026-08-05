"""
========================================
PROJECT PHOENIX AI
Smart Money FVG
Versione 1.0
========================================
"""

from Logs.logger import Logger


class SmartMoneyFVG:

    def __init__(self):

        Logger.success(
            "Smart Money FVG V1 inizializzato."
        )

    def detect(self, data):

        if len(data) < 3:

            return False

        high_1 = float(data["High"].iloc[-3])
        low_3 = float(data["Low"].iloc[-1])

        low_1 = float(data["Low"].iloc[-3])
        high_3 = float(data["High"].iloc[-1])

        bullish_gap = low_3 > high_1
        bearish_gap = high_3 < low_1

        return bullish_gap or bearish_gap