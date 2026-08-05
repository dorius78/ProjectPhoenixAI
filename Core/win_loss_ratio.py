"""
========================================
PROJECT PHOENIX AI
Win Loss Ratio
Versione 1.0
========================================
"""

from Logs.logger import Logger


class WinLossRatio:

    def __init__(self):

        Logger.success(

            "Win Loss Ratio V1 inizializzato."

        )

    def calculate(

        self,

        database

    ):

        trades = database.load_trades()

        if len(trades) == 0:

            return 0.0

        wins = 0

        losses = 0

        for trade in trades:

            pnl = float(

                trade[7]

            )

            if pnl > 0:

                wins += 1

            elif pnl < 0:

                losses += 1

        if losses == 0:

            return 0.0

        return round(

            wins / losses,

            3

        )