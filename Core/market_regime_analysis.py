"""
========================================
PROJECT PHOENIX AI
Market Regime Analysis Engine
Versione 1.0
========================================
"""

from collections import defaultdict

from Logs.logger import Logger


class MarketRegimeAnalysis:

    def __init__(self):

        Logger.success(
            "Market Regime Analysis Engine V1 inizializzato."
        )

    def analyze(self, trades):

        if trades is None:
            trades = []

        regimes = defaultdict(
            lambda: {
                "trades": 0,
                "profit": 0.0,
                "wins": 0,
                "losses": 0,
                "durations": [],
                "risk_rewards": []
            }
        )

        for trade in trades:

            if not isinstance(trade, dict):
                continue

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

            pnl = float(
                trade.get("pnl", 0.0)
            )

            duration = float(
                trade.get("duration", 0.0)
            )

            risk_reward = float(
                trade.get("risk_reward", 0.0)
            )

            data = regimes[regime]

            data["trades"] += 1
            data["profit"] += pnl
            data["durations"].append(duration)
            data["risk_rewards"].append(risk_reward)

            if pnl > 0:
                data["wins"] += 1

            elif pnl < 0:
                data["losses"] += 1

        result = {}

        for regime, data in regimes.items():

            trades_count = data["trades"]

            result[regime] = {
                "trades": trades_count,
                "profit": round(
                    data["profit"],
                    2
                ),
                "wins": data["wins"],
                "losses": data["losses"],
                "win_rate": round(
                    data["wins"] / trades_count * 100,
                    2
                ) if trades_count else 0.0,
                "average_pnl": round(
                    data["profit"] / trades_count,
                    2
                ) if trades_count else 0.0,
                "average_duration": round(
                    sum(data["durations"]) / len(data["durations"]),
                    2
                ) if data["durations"] else 0.0,
                "average_risk_reward": round(
                    sum(data["risk_rewards"]) / len(data["risk_rewards"]),
                    2
                ) if data["risk_rewards"] else 0.0
            }

        best_regime = None
        worst_regime = None

        if result:

            best_regime = max(
                result,
                key=lambda regime: result[regime]["profit"]
            )

            worst_regime = min(
                result,
                key=lambda regime: result[regime]["profit"]
            )

        return {
            "regimes": result,
            "best_regime": best_regime,
            "worst_regime": worst_regime
        }
