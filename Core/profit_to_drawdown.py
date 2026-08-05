"""
========================================
PROJECT PHOENIX AI
Profit to Drawdown
Versione 1.0
========================================
"""

from Logs.logger import Logger


class ProfitToDrawdown:

    def __init__(self):

        Logger.success(

            "Profit to Drawdown V1 inizializzato."

        )

    def calculate(self, database):

        trades = database.load_trades()

        if len(trades) == 0:

            return 0

        equity = 10000.0
        peak = equity
        max_drawdown = 0

        for trade in reversed(trades):

            pnl = float(trade[7])

            equity += pnl

            if equity > peak:

                peak = equity

            drawdown = peak - equity

            if drawdown > max_drawdown:

                max_drawdown = drawdown

        profit = database.total_profit()

        if max_drawdown == 0:

            return round(

                profit,

                3

            )

        return round(

            profit / max_drawdown,

            3

        )