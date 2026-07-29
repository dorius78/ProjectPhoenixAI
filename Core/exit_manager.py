"""
========================================
PROJECT PHOENIX AI
Exit Manager
Versione 1.0
========================================
"""

from Logs.logger import Logger


class ExitManager:

    def __init__(self):

        Logger.success("Exit Manager inizializzato.")

    # ==========================
    # VALUTAZIONE USCITA
    # ==========================

    def evaluate(self, position, current_price):

        Logger.section("EXIT MANAGER")

        if position is None:

            Logger.info("Nessuna posizione aperta.")

            return {

                "exit": False,
                "reason": "NO_POSITION"

            }

        direction = position["side"]

        stop_loss = position["stop_loss"]

        take_profit = position["take_profit"]

        # ==========================
        # BUY
        # ==========================

        if direction == "BUY":

            if current_price <= stop_loss:

                Logger.warning("Stop Loss raggiunto.")

                return {

                    "exit": True,
                    "reason": "STOP_LOSS"

                }

            if current_price >= take_profit:

                Logger.success("Take Profit raggiunto.")

                return {

                    "exit": True,
                    "reason": "TAKE_PROFIT"

                }

        # ==========================
        # SELL
        # ==========================

        elif direction == "SELL":

            if current_price >= stop_loss:

                Logger.warning("Stop Loss raggiunto.")

                return {

                    "exit": True,
                    "reason": "STOP_LOSS"

                }

            if current_price <= take_profit:

                Logger.success("Take Profit raggiunto.")

                return {

                    "exit": True,
                    "reason": "TAKE_PROFIT"

                }

        Logger.info("Posizione ancora aperta.")

        return {

            "exit": False,
            "reason": "POSITION_OPEN"

        }