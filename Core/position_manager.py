"""
========================================
PROJECT PHOENIX AI
Position Manager
Versione 1.0
========================================
"""

from Logs.logger import Logger


class PositionManager:

    def __init__(self):

        Logger.success(
            "Position Manager V1 inizializzato."
        )

        self.position = None

    # =====================================
    # APERTURA POSIZIONE
    # =====================================

    def open_position(
        self,
        symbol,
        side,
        entry,
        size=1.0,
        timestamp=None
    ):

        if self.position is not None:

            Logger.warning(
                "Posizione già presente."
            )

            return False

        self.position = {

            "symbol": symbol,

            "side": side,

            "entry": float(entry),

            "size": float(size),

            "status": "OPEN",

            "open_time": timestamp,

            "close_time": None

        }

        Logger.success(
            f"Position Manager -> posizione aperta "
            f"{side} {symbol}"
        )

        return True

    # =====================================
    # AGGIORNA POSIZIONE
    # =====================================

    def update_position(self, **updates):

        if self.position is None:

            return None

        self.position.update(
            updates
        )

        return self.position

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
    # CHIUSURA
    # =====================================

    def close_position(
        self,
        timestamp=None
    ):

        if self.position is None:

            return None

        self.position["status"] = "CLOSED"

        self.position["close_time"] = timestamp

        closed = self.position.copy()

        self.position = None

        Logger.success(
            "Position Manager -> posizione chiusa."
        )

        return closed

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        self.position = None

        Logger.info(
            "Position Manager azzerato."
        )