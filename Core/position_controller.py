"""
========================================
PROJECT PHOENIX AI
Position Controller
Versione 8.0
========================================
"""

from datetime import datetime

from Logs.logger import Logger


class PositionController:

    def __init__(self):

        Logger.success("Position Controller V8 inizializzato.")

        self.position = None

    # =====================================
    # APERTURA POSIZIONE
    # =====================================

    def open_position(
        self,
        side,
        entry,
        stop_loss,
        take_profit
    ):

        if self.position is not None:

            Logger.warning("Posizione già aperta.")
            return False

        self.position = {

            "side": side,

            "entry": float(entry),

            "stop_loss": float(stop_loss),

            "take_profit": float(take_profit),

            "status": "OPEN",

            "open_time": datetime.now(),

            "current_price": float(entry),

            "current_profit": 0.0,

            "max_profit": 0.0,

            "break_even": False,

            "trailing_stop": None

        }

        Logger.success(f"Aperta posizione {side}")

        return True

    # =====================================
    # AGGIORNA POSIZIONE
    # =====================================

    def update(self, current_price):

        if self.position is None:

            return

        self.position["current_price"] = float(current_price)

        entry = self.position["entry"]

        if self.position["side"] == "BUY":

            profit = current_price - entry

        else:

            profit = entry - current_price

        self.position["current_profit"] = round(profit, 6)

        if profit > self.position["max_profit"]:

            self.position["max_profit"] = round(profit, 6)

        if (

            not self.position["break_even"]

            and profit > 0

        ):

            self.position["stop_loss"] = entry

            self.position["break_even"] = True

    # =====================================
    # CHIUSURA
    # =====================================

    def close_position(
        self,
        reason="MANUALE"
    ):

        if self.position is None:

            Logger.warning("Nessuna posizione aperta.")
            return None

        self.position["status"] = "CLOSED"

        self.position["close_reason"] = reason

        self.position["close_time"] = datetime.now()

        Logger.success(f"Posizione chiusa ({reason})")

        closed = self.position

        self.position = None

        return closed

    # =====================================
    # GET
    # =====================================

    def get_position(self):

        return self.position

    # =====================================
    # CONTROLLO
    # =====================================

    def has_position(self):

        return self.position is not None

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        self.position = None

        Logger.info("Position Controller azzerato.")