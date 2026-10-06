"""
========================================
PROJECT PHOENIX AI
Pattern Analysis Engine
Versione 1.0
========================================
"""

from collections import defaultdict

from Logs.logger import Logger


class PatternAnalysis:

    def __init__(self):

        Logger.success(
            "Pattern Analysis Engine V1 inizializzato."
        )

    def analyze(self, trades):

        if trades is None:
            trades = []

        patterns = defaultdict(
            lambda: {
                "trades": 0,
                "profit": 0.0,
                "wins": 0,
                "losses": 0
            }
        )

        for trade in trades:

            if not isinstance(trade, dict):
                continue

            side = str(
                trade.get("side", "UNKNOWN")
            ).upper()

            reason = str(
                trade.get("reason", "UNKNOWN")
            ).upper()

            regime = trade.get(
                "regime",
                "UNKNOWN"
            )

            if isinstance(regime, dict):
                regime = regime.get(
                    "regime",
                    "UNKNOWN"
                )

            regime = str(regime).upper()

            key = (
                side,
                reason,
                regime
            )

            pnl = float(
                trade.get("pnl", 0.0)
            )

            patterns[key]["trades"] += 1
            patterns[key]["profit"] += pnl

            if pnl > 0:
                patterns[key]["wins"] += 1

            elif pnl < 0:
                patterns[key]["losses"] += 1

        return {
            "patterns": {
                str(key): {
                    "trades": value["trades"],
                    "profit": round(
                        value["profit"],
                        2
                    ),
                    "wins": value["wins"],
                    "losses": value["losses"]
                }
                for key, value in patterns.items()
            }
        }
