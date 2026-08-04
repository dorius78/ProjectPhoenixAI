"""
========================================
PROJECT PHOENIX AI
Execution Engine
Versione 5.0
========================================
"""

from datetime import datetime

from Logs.logger import Logger


class ExecutionEngine:

    def __init__(self):

        Logger.success("Execution Engine V5 inizializzato.")

        self.orders = []

    # =====================================
    # ESECUZIONE ORDINE
    # =====================================

    def execute(self, trade):

        Logger.section("EXECUTION ENGINE")

        if trade is None:

            Logger.warning("Trade non valido.")

            return {

                "success": False,

                "message": "Nessun trade"

            }

        signal = str(

            trade.get("signal", "HOLD")

        ).upper()

        if signal == "HOLD":

            Logger.info("Segnale HOLD.")

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

            "entry": float(trade["entry"]),

            "stop_loss": float(trade["stop_loss"]),

            "take_profit": float(trade["take_profit"]),

            "risk_reward": float(

                trade["risk_reward"]

            ),

            "status": "OPEN",

            "open_time": datetime.now()

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

        Logger.success(

            f"Ordine {position['side']} chiuso."

        )

        return {

            "success": True,

            "symbol": position["symbol"],

            "side": position["side"],

            "entry": position["entry"],

            "exit": position["current_price"],

            "pnl": position["current_profit"],

            "reason": position["close_reason"],

            "status": "CLOSED",

            "close_time": datetime.now()

        }

    # =====================================
    # ORDINI APERTI
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