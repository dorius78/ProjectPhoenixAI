"""
========================================
PROJECT PHOENIX AI
Trade Journal
Versione E68.1
========================================

Registro strutturato del ciclo completo
di una posizione.

NESSUNA esecuzione MT5.
"""

from Logs.logger import Logger


class TradeJournal:

    def __init__(self, database=None):
        self.database = database

        Logger.success(
            "Trade Journal E68.1 inizializzato."
        )

    # =====================================
    # REGISTRA TRADE CHIUSO
    # =====================================

    def record_trade(self, trade):

        if not isinstance(trade, dict):
            return {
                "success": False,
                "reason": "Trade non valido"
            }

        required = [
            "symbol",
            "side",
            "entry",
            "exit",
            "size",
            "pnl"
        ]

        missing = [
            field
            for field in required
            if field not in trade
        ]

        if missing:
            return {
                "success": False,
                "reason": (
                    "Campi mancanti: "
                    + ", ".join(missing)
                )
            }

        record = {
            "symbol": trade["symbol"],
            "side": trade["side"],
            "entry": float(trade["entry"]),
            "exit": float(trade["exit"]),
            "size": float(trade["size"]),
            "pnl": float(trade["pnl"]),
            "reason": trade.get(
                "reason",
                "UNKNOWN"
            ),
            "stop_loss": trade.get(
                "stop_loss"
            ),
            "take_profit": trade.get(
                "take_profit"
            ),
            "risk_reward": trade.get(
                "risk_reward"
            ),
            "confidence": trade.get(
                "confidence"
            ),
            "regime": trade.get(
                "regime"
            )
        }

        Logger.success(
            f"Trade Journal registrato: "
            f"{record['symbol']} | "
            f"{record['side']} | "
            f"PnL: {record['pnl']}"
        )

        return {
            "success": True,
            "record": record
        }

    # =====================================
    # DATABASE
    # =====================================

    def save(self, trade):

        from datetime import datetime

        record = dict(trade)

        now = datetime.now()

        record.setdefault("status", "CLOSED")
        record.setdefault("open_time", now)
        record.setdefault("close_time", now)
        record.setdefault("duration", 0)
        record.setdefault("result", "WIN" if float(record.get("pnl", 0)) > 0 else "LOSS")
        record.setdefault("risk_reward", 0.0)

        try:

            self.database.save_trade(record)

            Logger.success(
                "Trade Journal salvato nel Database: "
                f"{record.get('symbol')} | "
                f"{record.get('side')} | "
                f"PnL: {record.get('pnl')}"
            )

            return {
                "success": True,
                "saved": True,
                "record": record
            }

        except Exception as error:

            Logger.warning(
                f"Salvataggio Journal fallito: {error}"
            )

            return {
                "success": False,
                "saved": False,
                "record": record,
                "reason": str(error)
            }
