"""
========================================
PROJECT PHOENIX AI
Trade Statistics
Versione 1.0
========================================
"""

from Logs.logger import Logger


class TradeStatistics:

    def __init__(self):

        Logger.success(

            "Trade Statistics V1 inizializzato."

        )

    def calculate(

        self,

        database

    ):

        total = database.count()

        if total == 0:

            return {

                "average_win": 0,

                "average_loss": 0,

                "expectancy": 0

            }

        trades = database.load_trades()

        wins = []

        losses = []

        for trade in trades:

            pnl = float(trade[7])

            if pnl > 0:

                wins.append(pnl)

            elif pnl < 0:

                losses.append(abs(pnl))

        average_win = 0

        average_loss = 0

        if len(wins) > 0:

            average_win = round(

                sum(wins) / len(wins),

                2

            )

        if len(losses) > 0:

            average_loss = round(

                sum(losses) / len(losses),

                2

            )

        expectancy = round(

            database.total_profit() / total,

            2

        )

        return {

            "average_win": average_win,

            "average_loss": average_loss,

            "expectancy": expectancy

        }