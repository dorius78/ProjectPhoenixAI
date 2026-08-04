"""
========================================
PROJECT PHOENIX AI
Equity Curve
Versione 1.0
========================================
"""

from Logs.logger import Logger


class EquityCurve:

    def __init__(self):

        Logger.success(

            "Equity Curve V1 inizializzata."

        )

    def calculate(

        self,

        trades,

        initial_capital=10000

    ):

        equity = initial_capital

        curve = []

        for trade in trades:

            equity += float(trade[7])

            curve.append(

                round(equity,2)

            )

        return curve