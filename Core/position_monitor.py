"""
========================================
PROJECT PHOENIX AI
Position Monitor
Versione 1.0
========================================
"""

from Logs.logger import Logger


class PositionMonitor:

    def __init__(self):

        Logger.success(
            "Position Monitor V1 inizializzato."
        )

    # =====================================
    # AGGIORNA POSIZIONE
    # =====================================

    def update(
        self,
        position,
        current_price
    ):

        if position is None:

            return None

        current_price = float(
            current_price
        )

        entry = float(
            position["entry"]
        )

        size = float(
            position.get("size", 1.0)
        )

        side = str(
            position["side"]
        ).upper()

        # =================================
        # PREZZO CORRENTE
        # =================================

        position["current_price"] = current_price

        # =================================
        # PROFITTO
        # =================================

        if side in ("BUY", "STRONG BUY"):

            profit = (
                current_price - entry
            ) * size

        else:

            profit = (
                entry - current_price
            ) * size

        position["current_profit"] = round(
            profit,
            6
        )

        # =================================
        # MASSIMO PROFITTO
        # =================================

        previous_max = float(
            position.get("max_profit", 0.0)
        )

        if profit > previous_max:

            position["max_profit"] = round(
                profit,
                6
            )

        else:

            position["max_profit"] = round(
                previous_max,
                6
            )

        return position