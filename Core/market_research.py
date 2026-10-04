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

        durations = []
        risk_rewards = []

        for trade in trades:

            symbol = trade[1]
            side = trade[2]
            pnl = float(trade[9])
            reason = trade[11]
            regime = trade[17]
            duration = float(trade[14])
            risk_reward = float(trade[16])

            durations.append(duration)
            risk_rewards.append(risk_reward)

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

        duration_stats = {
            "trades": len(durations),
            "average": round(
                sum(durations) / len(durations),
                2
            ) if durations else 0,
            "minimum": min(durations) if durations else 0,
            "maximum": max(durations) if durations else 0
        }

        risk_reward_stats = {
            "trades": len(risk_rewards),
            "average": round(
                sum(risk_rewards) / len(risk_rewards),
                2
            ) if risk_rewards else 0,
            "minimum": min(risk_rewards) if risk_rewards else 0,
            "maximum": max(risk_rewards) if risk_rewards else 0
        }

        return {
            "overview": overview,
            "duration": duration_stats,
            "risk_reward": risk_reward_stats,
            "symbols": dict(symbols),
            "sides": dict(sides),
            "reasons": dict(reasons),
            "regimes": dict(regimes)
        }
