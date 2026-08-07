"""
========================================
PROJECT PHOENIX AI
Smart Money Liquidity
Versione 2.0
========================================
"""

from Logs.logger import Logger


class SmartMoneyLiquidity:

    def __init__(self):

        Logger.success(
            "Smart Money Liquidity V2 inizializzato."
        )

    def detect(self, data):

        if len(data) < 10:

            return {"detected": False, "direction": None}

        last_high = float(data["High"].iloc[-1])
        last_low = float(data["Low"].iloc[-1])
        last_close = float(data["Close"].iloc[-1])

        previous_high = float(
            data["High"].iloc[-10:-1].max()
        )

        previous_low = float(
            data["Low"].iloc[-10:-1].min()
        )

        # Sweep sopra un massimo recente poi richiusura sotto:
        # liquidita' buy-side bruciata, tipicamente segnale RIBASSISTA.
        bearish_sweep = (
            last_high > previous_high
            and last_close < previous_high
        )

        # Sweep sotto un minimo recente poi richiusura sopra:
        # liquidita' sell-side bruciata, tipicamente segnale RIALZISTA.
        bullish_sweep = (
            last_low < previous_low
            and last_close > previous_low
        )

        if bullish_sweep:
            return {"detected": True, "direction": "BULLISH"}

        if bearish_sweep:
            return {"detected": True, "direction": "BEARISH"}

        return {"detected": False, "direction": None}