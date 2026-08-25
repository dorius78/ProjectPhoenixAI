"""
========================================
PROJECT PHOENIX AI
Execution Builder
Versione 1.2
========================================
"""

from datetime import datetime

from Logs.logger import Logger


class ExecutionBuilder:

    def __init__(self):

        Logger.success(
            "Execution Builder V1.2 inizializzato."
        )

    # =====================================
    # BUILD ORDER
    # =====================================

    def build(self, trade):

        if not trade:

            return {
                "success": False,
                "reason": "Trade vuoto"
            }

        signal = str(
            trade.get(
                "signal",
                "HOLD"
            )
        ).upper()

        # =====================================
        # DETERMINAZIONE SIDE
        # =====================================

        if signal in (
            "BUY",
            "STRONG BUY"
        ):

            side = "BUY"

        elif signal in (
            "SELL",
            "STRONG SELL"
        ):

            side = "SELL"

        else:

            side = signal

        # =====================================
        # SIZE
        # =====================================

        size = float(
            trade.get(
                "size",
                0.0
            )
        )

        # =====================================
        # PREZZI
        # =====================================

        entry = float(
            trade.get(
                "entry",
                0.0
            )
        )

        stop_loss = float(
            trade.get(
                "stop_loss",
                0.0
            )
        )

        take_profit = float(
            trade.get(
                "take_profit",
                0.0
            )
        )

        risk_reward = float(
            trade.get(
                "risk_reward",
                0.0
            )
        )

        # =====================================
        # VALIDAZIONE BASE
        # =====================================

        if not trade.get("symbol"):

            return {
                "success": False,
                "reason": "Simbolo mancante"
            }

        if side not in (
            "BUY",
            "SELL"
        ):

            return {
                "success": False,
                "reason": "Direzione non valida"
            }

        if size <= 0:

            return {
                "success": False,
                "reason": "Size non valida"
            }

        if entry <= 0:

            return {
                "success": False,
                "reason": "Entry non valida"
            }

        if stop_loss <= 0:

            return {
                "success": False,
                "reason": "Stop Loss non valido"
            }

        if take_profit <= 0:

            return {
                "success": False,
                "reason": "Take Profit non valido"
            }

        # =====================================
        # COSTRUZIONE ORDINE
        # =====================================

        return {

            "success": True,

            "symbol":
                trade["symbol"],

            "side":
                side,

            "signal":
                signal,

            "entry":
                entry,

            "stop_loss":
                stop_loss,

            "take_profit":
                take_profit,

            "risk_reward":
                risk_reward,

            "size":
                size,

            "status":
                "OPEN",

            "reason":
                "ENTRY",

            "pnl":
                0.0,

            "open_time":
                datetime.now(),

            "close_time":
                None

        }