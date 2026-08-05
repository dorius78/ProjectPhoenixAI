"""
========================================
PROJECT PHOENIX AI
Risk Position Size
Versione 1.0
========================================
"""

from Logs.logger import Logger


class RiskPositionSize:

    def __init__(self):

        Logger.success(
            "Risk Position Size V1 inizializzato."
        )

    def calculate(

        self,

        account_balance,

        risk_percent,

        entry,

        stop_loss

    ):

        account_balance = float(account_balance)
        risk_percent = float(risk_percent)

        entry = float(entry)
        stop_loss = float(stop_loss)

        risk_amount = account_balance * (

            risk_percent / 100

        )

        stop_distance = abs(

            entry - stop_loss

        )

        if stop_distance == 0:

            return 0

        position_size = (

            risk_amount /

            stop_distance

        )

        return round(

            position_size,

            6

        )