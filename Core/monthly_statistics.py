"""
========================================
PROJECT PHOENIX AI
Monthly Statistics
Versione 1.0
========================================
"""

from collections import defaultdict

from Logs.logger import Logger


class MonthlyStatistics:

    def __init__(self):

        Logger.success(

            "Monthly Statistics V1 inizializzato."

        )

    def calculate(

        self,

        database

    ):

        months = defaultdict(float)

        trades = database.load_trades()

        for trade in trades:

            close_time = str(trade[11])

            if len(close_time) >= 7:

                month = close_time[:7]

            else:

                month = "N/A"

            pnl = float(trade[7])

            months[month] += pnl

        return dict(months)