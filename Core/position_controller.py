"""
========================================
PROJECT PHOENIX AI
Position Controller
Versione 12.0
========================================
"""

from datetime import datetime

from Logs.logger import Logger


class PositionController:

    def __init__(self):

        Logger.success("Position Controller V12 inizializzato.")

        self.position = None

    # =====================================
    # APERTURA POSIZIONE
    # =====================================

    def open_position(

        self,

        side,

        entry,

        stop_loss,

        take_profit,

        symbol="BTC-USD",

        size=1.0

    ):

        if self.position is not None:

            Logger.warning("Posizione già aperta.")

            return False

        self.position = {

            "symbol": symbol,

            "side": side,

            "entry": float(entry),

            "stop_loss": float(stop_loss),

            "take_profit": float(take_profit),

            "size": float(size),

            "status": "OPEN",

            "open_time": datetime.now(),

            "close_time": None,

            "close_reason": None,

            "current_price": float(entry),

            "current_profit": 0.0,

            "max_profit": 0.0,

            "break_even": False,

            "trailing_stop": None

        }

        Logger.success(

            f"Aperta posizione {side} su {symbol} (size: {size})"

        )

        return True

    # =====================================
    # AGGIORNA POSIZIONE
    # =====================================

    def update(

        self,

        current_price

    ):

        if self.position is None:

            return None

        current_price = float(current_price)

        self.position["current_price"] = current_price

        entry = self.position["entry"]

        side = self.position["side"]

        size = self.position.get("size", 1.0)

        if side == "BUY":

            profit = (current_price - entry) * size

        else:

            profit = (entry - current_price) * size

        self.position["current_profit"] = round(

            profit,

            6

        )

        if profit > self.position["max_profit"]:

            self.position["max_profit"] = round(

                profit,

                6

            )

        # =====================================
        # BREAK EVEN
        # =====================================

        if (

            not self.position["break_even"]

            and profit > 0

        ):

            self.position["stop_loss"] = entry

            self.position["break_even"] = True

            Logger.info(

                "Break Even attivato."

            )

        # =====================================
        # TRAILING STOP
        # =====================================

        if self.position["break_even"]:

            distance = abs(

                self.position["take_profit"]

                - entry

            ) * 0.25

            if side == "BUY":

                new_stop = current_price - distance

                if new_stop > self.position["stop_loss"]:

                    self.position["stop_loss"] = round(

                        new_stop,

                        6

                    )

                    Logger.info(

                        f"Trailing Stop -> {self.position['stop_loss']}"

                    )

            else:

                new_stop = current_price + distance

                if new_stop < self.position["stop_loss"]:

                    self.position["stop_loss"] = round(

                        new_stop,

                        6

                    )

                    Logger.info(

                        f"Trailing Stop -> {self.position['stop_loss']}"

                    )

        # =====================================
        # STOP LOSS / TAKE PROFIT
        # =====================================

        if side == "BUY":

            if current_price <= self.position["stop_loss"]:

                return self.close_position(

                    "STOP LOSS"

                )

            if current_price >= self.position["take_profit"]:

                return self.close_position(

                    "TAKE PROFIT"

                )

        else:

            if current_price >= self.position["stop_loss"]:

                return self.close_position(

                    "STOP LOSS"

                )

            if current_price <= self.position["take_profit"]:

                return self.close_position(

                    "TAKE PROFIT"

                )

        return self.position

    # =====================================
    # CHIUSURA POSIZIONE
    # =====================================

    def close_position(

        self,

        reason="MANUALE"

    ):

        if self.position is None:

            return None

        self.position["status"] = "CLOSED"

        self.position["close_reason"] = reason

        self.position["close_time"] = datetime.now()

        Logger.success(

            f"Posizione chiusa ({reason})"

        )

        closed = self.position.copy()

        self.position = None

        return closed

    # =====================================
    # POSIZIONE
    # =====================================

    def get_position(self):

        return self.position

    # =====================================
    # ESISTE
    # =====================================

    def has_position(self):

        return self.position is not None

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        self.position = None

        Logger.info(

            "Position Controller azzerato."

        )