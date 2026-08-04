"""
========================================
PROJECT PHOENIX AI
Timeframe Statistics
Versione 1.0
========================================
"""

from collections import defaultdict

from Logs.logger import Logger


class TimeframeStatistics:

    def __init__(self):

        Logger.success(

            "Timeframe Statistics V1 inizializzato."

        )

    def calculate(

        self,

        database

    ):

        stats = defaultdict(

            lambda: {

                "trades": 0,

                "profit": 0.0

            }

        )

        trades = database.load_trades()

        for trade in trades:

            timeframe = "1H"

            pnl = float(trade[7])

            stats[timeframe]["trades"] += 1

            stats[timeframe]["profit"] += pnl

        return dict(stats)