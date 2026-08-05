"""
========================================
PROJECT PHOENIX AI
Smart Money Liquidity
Versione 1.0
========================================
"""

from Logs.logger import Logger


class SmartMoneyLiquidity:

    def __init__(self):

        Logger.success(
            "Smart Money Liquidity V1 inizializzato."
        )

    def detect(self, data):

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