"""
========================================
PROJECT PHOENIX AI
Execution Builder
Versione 1.0
========================================
"""

from datetime import datetime

from Logs.logger import Logger


class ExecutionBuilder:

    def __init__(self):

        Logger.success(
            "Execution Builder V1 inizializzato."
        )

    def build(self, trade):

        signal = str(

            trade.get(

                "signal",

                "HOLD"

            )

        ).upper()

        side = signal

        if signal == "STRONG BUY":

            side = "BUY"

        elif signal == "STRONG SELL":

            side = "SELL"

        return {

            "success": True,

            "symbol": trade["symbol"],

            "side": side,

            "signal": signal,

            "entry": float(

                trade["entry"]

            ),

            "stop_loss": float(

                trade["stop_loss"]

            ),

            "take_profit": float(

                trade["take_profit"]

            ),

            "risk_reward": float(

                trade["risk_reward"]

            ),

            "size": float(

                trade.get("size", 1.0)

            ),

            "status": "OPEN",

            "reason": "ENTRY",

            "pnl": 0.0,

            "open_time": datetime.now(),

            "close_time": None

        }