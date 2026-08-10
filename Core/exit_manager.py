"""
========================================
PROJECT PHOENIX AI
Exit Manager
Versione 3.0
========================================
"""

from Logs.logger import Logger


class ExitManager:

    def __init__(self):

        Logger.success(
            "Exit Manager V3 inizializzato."
        )

    # =====================================
    # BREAK EVEN
    # =====================================

    def apply_break_even(
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

        break_even = bool(
            position.get("break_even", False)
        )

        # =================================
        # GIA' ATTIVO
        # =================================

        if break_even:

            return position

        # =================================
        # CALCOLO PROFITTO
        # =================================

        if side in ("BUY", "STRONG BUY"):

            profit = (
                current_price - entry
            ) * size

        else:

            profit = (
                entry - current_price
            ) * size

        # =================================
        # ATTIVAZIONE BREAK EVEN
        # =================================

        if profit > 0:

            position["stop_loss"] = entry

            position["break_even"] = True

            Logger.info(
                "Break Even attivato."
            )

        return position

    # =====================================
    # TRAILING STOP
    # =====================================

    def apply_trailing_stop(
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

        take_profit = float(
            position["take_profit"]
        )

        stop_loss = float(
            position["stop_loss"]
        )

        side = str(
            position["side"]
        ).upper()

        break_even = bool(
            position.get("break_even", False)
        )

        # =================================
        # TRAILING SOLO DOPO BREAK EVEN
        # =================================

        if not break_even:

            return position

        # =================================
        # DISTANZA TRAILING
        # =================================

        distance = abs(
            take_profit - entry
        ) * 0.25

        # =================================
        # BUY
        # =================================

        if side in ("BUY", "STRONG BUY"):

            new_stop = (
                current_price - distance
            )

            if new_stop > stop_loss:

                position["stop_loss"] = round(
                    new_stop,
                    6
                )

                Logger.info(
                    f"Trailing Stop -> "
                    f"{position['stop_loss']}"
                )

        # =================================
        # SELL
        # =================================

        elif side in ("SELL", "STRONG SELL"):

            new_stop = (
                current_price + distance
            )

            if new_stop < stop_loss:

                position["stop_loss"] = round(
                    new_stop,
                    6
                )

                Logger.info(
                    f"Trailing Stop -> "
                    f"{position['stop_loss']}"
                )

        return position

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

        # =================================
        # BREAK EVEN
        # =================================

        self.apply_break_even(
            position,
            current_price
        )

        # =================================
        # TRAILING STOP
        # =================================

        self.apply_trailing_stop(
            position,
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