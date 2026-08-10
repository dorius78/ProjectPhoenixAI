"""
========================================
PROJECT PHOENIX AI
Exit Manager
Versione 3.2
========================================
"""

from Logs.logger import Logger


class ExitManager:

    def __init__(self):

        Logger.success(
            "Exit Manager V3.2 inizializzato."
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

        side = str(
            position["side"]
        ).upper()

        break_even = bool(
            position.get(
                "break_even",
                False
            )
        )

        # =================================
        # GIA' ATTIVO
        # =================================

        if break_even:

            return position

        # =================================
        # VERIFICA PROFITTO
        # =================================

        in_profit = False

        if side in (
            "BUY",
            "STRONG BUY"
        ):

            if current_price > entry:

                in_profit = True

        elif side in (
            "SELL",
            "STRONG SELL"
        ):

            if current_price < entry:

                in_profit = True

        # =================================
        # ATTIVAZIONE BREAK EVEN
        # =================================

        if in_profit:

            position["stop_loss"] = entry

            position["break_even"] = True

            # Nessun trailing ancora attivo.
            position["trailing_stop"] = None

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
            position.get(
                "break_even",
                False
            )
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

        if side in (
            "BUY",
            "STRONG BUY"
        ):

            new_stop = (

                current_price
                - distance

            )

            if new_stop > stop_loss:

                new_stop = round(
                    new_stop,
                    6
                )

                position["stop_loss"] = (
                    new_stop
                )

                position["trailing_stop"] = (
                    new_stop
                )

                Logger.info(

                    f"Trailing Stop -> "
                    f"{new_stop}"

                )

        # =================================
        # SELL
        # =================================

        elif side in (
            "SELL",
            "STRONG SELL"
        ):

            new_stop = (

                current_price
                + distance

            )

            if new_stop < stop_loss:

                new_stop = round(
                    new_stop,
                    6
                )

                position["stop_loss"] = (
                    new_stop
                )

                position["trailing_stop"] = (
                    new_stop
                )

                Logger.info(

                    f"Trailing Stop -> "
                    f"{new_stop}"

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

        position = self.apply_break_even(

            position,

            current_price

        )

        # =================================
        # TRAILING STOP
        # =================================

        position = self.apply_trailing_stop(

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

        trailing_stop = position.get(
            "trailing_stop"
        )

        break_even = bool(
            position.get(
                "break_even",
                False
            )
        )

        # =================================
        # BUY
        # =================================

        if side in (
            "BUY",
            "STRONG BUY"
        ):

            # -----------------------------
            # STOP / TRAILING
            # -----------------------------

            if current_price <= stop_loss:

                if trailing_stop is not None:

                    return "TRAILING STOP"

                if break_even:

                    return "BREAK EVEN"

                return "STOP LOSS"

            # -----------------------------
            # TAKE PROFIT
            # -----------------------------

            if current_price >= take_profit:

                return "TAKE PROFIT"

        # =================================
        # SELL
        # =================================

        elif side in (
            "SELL",
            "STRONG SELL"
        ):

            # -----------------------------
            # STOP / TRAILING
            # -----------------------------

            if current_price >= stop_loss:

                if trailing_stop is not None:

                    return "TRAILING STOP"

                if break_even:

                    return "BREAK EVEN"

                return "STOP LOSS"

            # -----------------------------
            # TAKE PROFIT
            # -----------------------------

            if current_price <= take_profit:

                return "TAKE PROFIT"

        return None