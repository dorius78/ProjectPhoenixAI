"""
========================================
PROJECT PHOENIX AI
Execution Validator
Versione 1.0
========================================
"""

from Logs.logger import Logger


class ExecutionValidator:

    def __init__(self):

        Logger.success(
            "Execution Validator V1 inizializzato."
        )

    def validate(self, trade):

        if trade is None:

            return False, "Nessun trade"

        signal = str(

            trade.get(

                "signal",

                "HOLD"

            )

        ).upper()

        if signal == "HOLD":

            return False, "Segnale HOLD"

        if signal not in (

            "BUY",

            "SELL",

            "STRONG BUY",

            "STRONG SELL"

        ):

            return False, "Segnale non valido"

        return True, ""