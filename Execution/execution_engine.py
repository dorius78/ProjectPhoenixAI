"""
========================================
PROJECT PHOENIX AI
Execution Engine
Versione 6.0
========================================
"""

from datetime import datetime

from Logs.logger import Logger


class ExecutionEngine:

    def __init__(self):

        Logger.success("Execution Engine V6 inizializzato.")

        self.orders = []

    # =====================================
    # ESECUZIONE ORDINE
    # =====================================

    def execute(

        self,

        trade

    ):

        Logger.section("EXECUTION ENGINE")

        if trade is None:

            Logger.warning("Trade non valido.")

            return {

                "success": False,

                "message": "Nessun trade"

            }

        signal = str(

            trade.get(

                "signal",

                "HOLD"

            )

        ).upper()

        if signal == "HOLD":

            Logger.info(

                "Segnale HOLD."

            )

            return {

                "success": False,

                "message": "Segnale HOLD"

            }

        side = signal

        if signal == "STRONG BUY":

            side = "BUY"

        elif signal == "STRONG SELL":

            side = "SELL"

        order = {

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

            "status": "OPEN",

            "reason": "ENTRY",

            "pnl": 0.0,

            "open_time": datetime.now(),

            "close_time": None

        }

        self.orders.append(order)

        Logger.success(

            f"Ordine {side} aperto."

        )

        return order

    # =====================================
    # CHIUSURA ORDINE
    # =====================================

    def close(

        self,

        position

    ):

        if position is None:

            return None

        report = {

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

            "close_time": datetime.now()

        }

        Logger.success(

            f"Ordine {position['side']} chiuso."

        )

        return report

    # =====================================
    # ORDINI
    # =====================================

    def get_orders(self):

        return self.orders

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        self.orders.clear()

        Logger.info(

            "Execution Engine azzerato."

        )