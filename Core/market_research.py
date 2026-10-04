"""
========================================
PROJECT PHOENIX AI
Market Research Engine
Versione 1.0
========================================
"""

from collections import defaultdict

from Logs.logger import Logger


class MarketResearch:

    def __init__(self):

        Logger.success(
            "Market Research Engine V1 inizializzato."
        )

    def analyze(self, database):

        trades = database.load_trades()

        overview = {
            "trades": 0,
            "profit": 0.0
        }

        symbols = defaultdict(
            lambda: {
                "trades": 0,
                "profit": 0.0,
                "wins": 0,
                "losses": 0
            }
        )

        sides = defaultdict(
            lambda: {
                "trades": 0,
                "profit": 0.0,
                "wins": 0,
                "losses": 0
            }
        )

        reasons = defaultdict(
            lambda: {
                "trades": 0,
                "profit": 0.0,
                "wins": 0,
                "losses": 0
            }
        )

        regimes = defaultdict(
            lambda: {
                "trades": 0,
                "profit": 0.0,
                "wins": 0,
                "losses": 0
            }
        )

        for trade in trades:

            symbol = trade[1]
            side = trade[2]
            pnl = float(trade[9])
            reason = trade[11]
            regime = trade[17]

            overview["trades"] += 1
            overview["profit"] += pnl

            groups = [
                (symbols, symbol),
                (sides, side),
                (reasons, reason),
                (regimes, regime)
            ]

            for collection, key in groups:

                if key is None:
                    continue

                collection[key]["trades"] += 1
                collection[key]["profit"] += pnl

                if pnl > 0:
                    collection[key]["wins"] += 1

                elif pnl < 0:
                    collection[key]["losses"] += 1

        overview["profit"] = round(
            overview["profit"],
            2
        )

        return {
            "overview": overview,
            "symbols": dict(symbols),
            "sides": dict(sides),
            "reasons": dict(reasons),
            "regimes": dict(regimes)
        }
