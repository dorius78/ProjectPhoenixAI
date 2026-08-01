"""
========================================
PROJECT PHOENIX AI
Position Controller
Versione 7.0
========================================
"""

from datetime import datetime

from Logs.logger import Logger


class PositionController:

    def __init__(self):

        Logger.success("Position Controller V7 inizializzato.")

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

            Logger.warning("Esiste già una posizione aperta.")

            return False

        self.position = {

            "side": side,

            "entry": entry,

            "stop_loss": stop_loss,

            "take_profit": take_profit,

            "status": "OPEN",

            "open_time": datetime.now()

        }

        Logger.success(f"Posizione {side} aperta.")

        return True

    # =====================================
    # CHIUSURA POSIZIONE
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

        Logger.success(
            f"Posizione chiusa ({reason})"
        )

        closed = self.position

        self.position = None

        return closed

    # =====================================
    # POSIZIONE ATTUALE
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