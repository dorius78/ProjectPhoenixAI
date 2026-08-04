"""
========================================
PROJECT PHOENIX AI
Sortino Ratio
Versione 1.0
========================================
"""

import math

from Logs.logger import Logger


class SortinoRatio:

    def __init__(self):

        Logger.success(

            "Sortino Ratio V1 inizializzato."

        )

    def calculate(

        self,

        database

    ):

        trades = database.load_trades()

        if len(trades) < 2:

            return 0.0

        returns = []

        negative = []

        for trade in trades:

            pnl = float(

                trade[7]

            )

            returns.append(

                pnl

            )

            if pnl < 0:

                negative.append(

                    pnl

                )

        if len(negative) == 0:

            return 0.0

        average = sum(

            returns

        ) / len(returns)

        downside = math.sqrt(

            sum(

                x ** 2

                for x in negative

            )

            /

            len(negative)

        )

        if downside == 0:

            return 0.0

        return round(

            average / downside,

            3

        )