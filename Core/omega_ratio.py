"""
========================================
PROJECT PHOENIX AI
Omega Ratio
Versione 1.1
========================================
"""

from Logs.logger import Logger


class OmegaRatio:

    def __init__(self):

        Logger.success(

            "Omega Ratio V1 inizializzato."

        )

    def calculate(self, database):

        trades = database.load_trades()

        if len(trades) == 0:

            return 0

        gross_profit = 0
        gross_loss = 0

        for trade in trades:

            pnl = float(trade[7])

            if pnl > 0:

                gross_profit += pnl

            elif pnl < 0:

                gross_loss += abs(pnl)

        if gross_loss == 0:

            return round(

                gross_profit,

                3

            )

        return round(

            gross_profit / gross_loss,

            3

        )