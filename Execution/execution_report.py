"""
========================================
PROJECT PHOENIX AI
Execution Report
Versione 1.1
========================================
"""

from datetime import datetime

from Logs.logger import Logger


class ExecutionReport:

    def __init__(self):

        Logger.success(
            "Execution Report V1.1 inizializzato."
        )

    def build(self, position):

        if position is None:

            return None

        required_fields = [
            "symbol",
            "side",
            "entry",
            "current_price",
            "stop_loss",
            "take_profit",
            "current_profit",
            "status",
            "close_reason",
            "open_time"
        ]

        missing_fields = [
            field
            for field in required_fields
            if field not in position
        ]

        if missing_fields:

            Logger.error(
                "Execution Report: posizione incompleta. "
                f"Campi mancanti: {missing_fields}"
            )

            return None

        return {

            "success": True,

            "symbol": position["symbol"],

            "side": position["side"],

            "entry": position["entry"],

            "exit": position["current_price"],

            "stop_loss": position["stop_loss"],

            "take_profit": position["take_profit"],

            "pnl": position["current_profit"],

            "status": "CLOSED",

            "reason": position["close_reason"],

            "open_time": position["open_time"],

            "close_time": (
                position["close_time"]
                if position.get("close_time") is not None
                else datetime.now()
            )

        }
