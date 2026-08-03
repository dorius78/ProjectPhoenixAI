"""
========================================
PROJECT PHOENIX AI
Execution Engine
Versione 4.0
========================================
"""

from Logs.logger import Logger


class ExecutionEngine:

    def __init__(self):

        Logger.success("Execution Engine V4 inizializzato.")

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

        signal = trade.get("signal", "").upper()

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

        Logger.success(

            f"Ordine {side} aperto."

        )

        return {

            "success": True,

            "symbol": trade["symbol"],

            "side": side,

            "signal": signal,

            "entry": trade["entry"],

            "stop_loss": trade["stop_loss"],

            "take_profit": trade["take_profit"],

            "risk_reward": trade["risk_reward"],

            "status": "SIMULATED"

        }

    # =====================================
    # CHIUSURA ORDINE
    # =====================================

    def close(self, position):

        if position is None:

            return None

        Logger.success(

            f"Ordine {position['side']} chiuso."

        )

        return {

            "success": True,

            "symbol": position["symbol"],

            "status": "CLOSED"

        }
}