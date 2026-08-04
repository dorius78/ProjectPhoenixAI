"""
========================================
PROJECT PHOENIX AI
Sharpe Ratio
Versione 1.0
========================================
"""

import math

from Logs.logger import Logger


class SharpeRatio:

    def __init__(self):

        Logger.success(

            "Sharpe Ratio V1 inizializzato."

        )

    def calculate(

        self,

        database

    ):

        trades = database.load_trades()

        if len(trades) < 2:

            return 0.0

        returns = []

        for trade in trades:

            returns.append(

                float(trade[7])

            )

        media = sum(returns) / len(returns)

        varianza = sum(

            (

                x - media

            ) ** 2

            for x in returns

        ) / len(returns)

        deviazione = math.sqrt(

            varianza

        )

        if deviazione == 0:

            return 0.0

        return round(

            media / deviazione,

            3

        )