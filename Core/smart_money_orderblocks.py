"""
========================================
PROJECT PHOENIX AI
Smart Money Order Blocks
Versione 2.0
========================================
"""

from Logs.logger import Logger


class SmartMoneyOrderBlocks:

    def __init__(self):

        Logger.success(
            "Smart Money Order Blocks V2 inizializzato."
        )

    def detect(self, data):

        # Un Order Block rialzista e' l'ultima candela ribassista
        # prima di una rottura decisa al rialzo (il prezzo chiude
        # sopra il massimo di quella candela). Quello ribassista e'
        # l'equivalente speculare.

        if len(data) < 3:

            return {"detected": False, "direction": None}

        ob_candle = data.iloc[-2]
        confirm_candle = data.iloc[-1]

        ob_open = float(ob_candle["Open"])
        ob_close = float(ob_candle["Close"])
        ob_high = float(ob_candle["High"])
        ob_low = float(ob_candle["Low"])

        confirm_close = float(confirm_candle["Close"])

        bullish_ob = (
            ob_close < ob_open
            and confirm_close > ob_high
        )

        bearish_ob = (
            ob_close > ob_open
            and confirm_close < ob_low
        )

        if bullish_ob:
            return {"detected": True, "direction": "BULLISH"}

        if bearish_ob:
            return {"detected": True, "direction": "BEARISH"}

        return {"detected": False, "direction": None}