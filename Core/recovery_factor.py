"""
========================================
PROJECT PHOENIX AI
Recovery Factor
Versione 1.0
========================================
"""

from Logs.logger import Logger


class RecoveryFactor:

    def __init__(self):

        Logger.success(

            "Recovery Factor V1 inizializzato."

        )

    def calculate(

        self,

        database

    ):

        trades = database.load_trades()

        if len(trades) == 0:

            return 0.0

        total_profit = 0.0

        equity = 10000.0

        peak = equity

        max_drawdown = 0.0

        for trade in trades:

            pnl = float(

                trade[7]

            )

            total_profit += pnl

            equity += pnl

            if equity > peak:

                peak = equity

            drawdown = peak - equity

            if drawdown > max_drawdown:

                max_drawdown = drawdown

        if max_drawdown == 0:

            return 0.0

        return round(

            total_profit / max_drawdown,

            3

        )