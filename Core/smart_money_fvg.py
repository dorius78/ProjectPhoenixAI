"""
========================================
PROJECT PHOENIX AI
Smart Money FVG
Versione 2.0
========================================
"""

from Logs.logger import Logger


class SmartMoneyFVG:

    def __init__(self):

        Logger.success(
            "Smart Money FVG V2 inizializzato."
        )

    def detect(self, data):

        if len(data) < 3:

            return {"detected": False, "direction": None}

        high_1 = float(data["High"].iloc[-3])
        low_3 = float(data["Low"].iloc[-1])

        low_1 = float(data["Low"].iloc[-3])
        high_3 = float(data["High"].iloc[-1])

        bullish_gap = low_3 > high_1
        bearish_gap = high_3 < low_1

        if bullish_gap:
            return {"detected": True, "direction": "BULLISH"}

        if bearish_gap:
            return {"detected": True, "direction": "BEARISH"}

        return {"detected": False, "direction": None}