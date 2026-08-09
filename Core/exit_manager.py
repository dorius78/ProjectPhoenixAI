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

        Logger.success(
            "Exit Manager V1 inizializzato."
        )

    # =====================================
    # VALUTA USCITA
    # =====================================

    def evaluate(
        self,
        position,
        current_price
    ):

        if position is None:

            return None

        current_price = float(
            current_price
        )

        side = str(
            position["side"]
        ).upper()

        stop_loss = float(
            position["stop_loss"]
        )

        take_profit = float(
            position["take_profit"]
        )

        # =================================
        # BUY
        # =================================

        if side in ("BUY", "STRONG BUY"):

            if current_price <= stop_loss:

                return "STOP LOSS"

            if current_price >= take_profit:

                return "TAKE PROFIT"

        # =================================
        # SELL
        # =================================

        elif side in ("SELL", "STRONG SELL"):

            if current_price >= stop_loss:

                return "STOP LOSS"

            if current_price <= take_profit:

                return "TAKE PROFIT"

        return None