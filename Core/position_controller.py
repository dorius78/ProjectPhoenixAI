"""
PROJECT PHOENIX AI
Position Controller
Versione 2.0
"""

from datetime import datetime


class PositionController:

    def __init__(self):
        self.position = None

    def open_position(self, side, entry, stop_loss, take_profit):

        if self.position is not None:
            return False

        self.position = {
            "side": side,
            "entry": entry,
            "stop_loss": stop_loss,
            "take_profit": take_profit,
            "open_time": datetime.now(),
            "status": "OPEN"
        }

        return True

    def get_position(self):
        return self.position

    def has_position(self):
        return self.position is not None

    def close_position(self, reason="MANUALE"):

        if self.position is None:
            return None

        self.position["status"] = "CLOSED"
        self.position["close_time"] = datetime.now()
        self.position["close_reason"] = reason

        closed = self.position
        self.position = None

        return closed