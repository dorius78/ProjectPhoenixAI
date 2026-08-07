"""
========================================
PROJECT PHOENIX AI
Execution Report
Versione 1.0
========================================
"""

from datetime import datetime

from Logs.logger import Logger


class ExecutionReport:

    def __init__(self):

        Logger.success(
            "Execution Report V1 inizializzato."
        )

    def build(self, position):

        if position is None:

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