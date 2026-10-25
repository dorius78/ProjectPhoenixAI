"""
PROJECT PHOENIX AI
Market Research Engine
Versione 1.1
"""

from collections import defaultdict
from datetime import datetime

from Logs.logger import Logger


class MarketResearch:

    def __init__(self):
        Logger.success("Market Research Engine V1.1 inizializzato.")

    @staticmethod
    def _to_float(value):
        try:
            if value is None:
                return None
            return float(value)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def _new_group():
        return {
            "trades": 0,
            "profit": 0.0,
            "wins": 0,
            "losses": 0
        }

    def analyze(self, database):
        # Ricava i nomi reali delle colonne senza modificare i dati.
        database.cursor.execute("SELECT * FROM trades LIMIT 0")
        description = database.cursor.description or ()
        columns = [item[0] for item in description]

        raw_trades = database.load_trades()
        trades = []

        for trade in raw_trades or []:
            if isinstance(trade, dict):
                trades.append(trade)
            elif isinstance(trade, (tuple, list)) and len(trade) == len(columns):
                trades.append(dict(zip(columns, trade)))

        overview = {"trades": 0, "profit": 0.0}
        symbols = defaultdict(self._new_group)
        sides = defaultdict(self._new_group)
        reasons = defaultdict(self._new_group)
        regimes = defaultdict(self._new_group)
        hours = defaultdict(self._new_group)
        durations = []
        risk_rewards = []

        for trade in trades:
            pnl = self._to_float(trade.get("pnl"))
            if pnl is None:
                continue

            overview["trades"] += 1
            overview["profit"] += pnl

            symbol = trade.get("symbol")
            side = trade.get("side")
            reason = trade.get("reason")
            regime = trade.get("regime")

            if isinstance(regime, dict):
                regime = regime.get("regime")

            if isinstance(regime, str):
                regime = regime.strip().upper()
                if not regime:
                    regime = None
            else:
                regime = None

            groups = [
                (symbols, symbol),
                (sides, side),
                (reasons, reason),
                (regimes, regime)
            ]

            for collection, key in groups:
                if key is None:
                    continue
                if isinstance(key, str):
                    key = key.strip()
                    if not key:
                        continue
                    if collection is sides:
                        key = key.upper()
                collection[key]["trades"] += 1
                collection[key]["profit"] += pnl

                if pnl > 0:
                    collection[key]["wins"] += 1
                elif pnl < 0:
                    collection[key]["losses"] += 1

            duration = self._to_float(trade.get("duration"))
            if duration is not None:
                durations.append(duration)

            risk_reward = self._to_float(trade.get("risk_reward"))
            if risk_reward is not None:
                risk_rewards.append(risk_reward)

            open_time = trade.get("open_time")
            if open_time:
                try:
                    parsed_time = datetime.fromisoformat(
                        str(open_time).replace("Z", "+00:00")
                    )
                    hour = parsed_time.strftime("%H")
                except (ValueError, TypeError):
                    hour = None

                if hour is not None:
                    hours[hour]["trades"] += 1
                    hours[hour]["profit"] += pnl
                    if pnl > 0:
                        hours[hour]["wins"] += 1
                    elif pnl < 0:
                        hours[hour]["losses"] += 1

        overview["profit"] = round(overview["profit"], 2)

        duration_stats = {
            "trades": len(durations),
            "average": round(sum(durations) / len(durations), 2) if durations else 0,
            "minimum": min(durations) if durations else 0,
            "maximum": max(durations) if durations else 0
        }

        risk_reward_stats = {
            "trades": len(risk_rewards),
            "average": round(sum(risk_rewards) / len(risk_rewards), 2) if risk_rewards else 0,
            "minimum": min(risk_rewards) if risk_rewards else 0,
            "maximum": max(risk_rewards) if risk_rewards else 0
        }

        def serialize_groups(collection):
            return {
                key: {
                    "trades": value["trades"],
                    "profit": round(value["profit"], 2),
                    "wins": value["wins"],
                    "losses": value["losses"]
                }
                for key, value in collection.items()
            }

        return {
            "overview": overview,
            "duration": duration_stats,
            "risk_reward": risk_reward_stats,
            "hours": serialize_groups(hours),
            "symbols": serialize_groups(symbols),
            "sides": serialize_groups(sides),
            "reasons": serialize_groups(reasons),
            "regimes": serialize_groups(regimes)
        }
