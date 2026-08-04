"""
========================================
PROJECT PHOENIX AI
Symbol Statistics
Versione 1.0
========================================
"""

from collections import defaultdict

from Logs.logger import Logger


class SymbolStatistics:

    def __init__(self):

        Logger.success(

            "Symbol Statistics V1 inizializzato."

        )

    def calculate(

        self,

        database

    ):

        stats = defaultdict(

            lambda: {

                "trades": 0,

                "profit": 0.0,

                "wins": 0,

                "losses": 0

            }

        )

        trades = database.load_trades()

        for trade in trades:

            symbol = trade[1]

            pnl = float(trade[7])

            stats[symbol]["trades"] += 1

            stats[symbol]["profit"] += pnl

            if pnl > 0:

                stats[symbol]["wins"] += 1

            elif pnl < 0:

                stats[symbol]["losses"] += 1

        return dict(stats)