"""
========================================
PROJECT PHOENIX AI
Position Controller
Versione 12.5
========================================
"""

from datetime import datetime

from Logs.logger import Logger
from Core.position_monitor import PositionMonitor
from Core.exit_manager import ExitManager


class PositionController:

    def __init__(self):

        Logger.success(
            "Position Controller V12.5 inizializzato."
        )

        self.position = None

        # =================================
        # POSITION MONITOR
        # =================================

        self.monitor = PositionMonitor()

        # =================================
        # EXIT MANAGER
        # =================================

        self.exit_manager = ExitManager()

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

        size=1.0,

        timestamp=None

    ):

        if self.position is not None:

            Logger.warning(
                "Posizione già aperta."
            )

            return False

        # =================================
        # ORARIO APERTURA
        # =================================

        open_time = (

            timestamp
            if timestamp is not None
            else datetime.now()

        )

        # =================================
        # VALORI NUMERICI
        # =================================

        entry = float(entry)

        stop_loss = float(stop_loss)

        take_profit = float(take_profit)

        size = float(size)

        # =================================
        # CREAZIONE POSIZIONE
        # =================================

        self.position = {

            "symbol": symbol,

            "side": side,

            "entry": entry,

            # Stop Loss iniziale.
            # NON viene modificato da
            # Break Even o Trailing Stop.

            "initial_stop_loss": stop_loss,

            # Stop Loss corrente.
            # Può essere modificato durante
            # la gestione della posizione.

            "stop_loss": stop_loss,

            "take_profit": take_profit,

            "size": size,

            "status": "OPEN",

            "open_time": open_time,

            "close_time": None,

            "close_reason": None,

            "current_price": entry,

            "current_profit": 0.0,

            "max_profit": 0.0,

            "break_even": False,

            "trailing_stop": None

        }

        Logger.success(

            f"Aperta posizione {side} su {symbol} "
            f"(size: {size})"

        )

        return True

    # =====================================
    # AGGIORNA POSIZIONE
    # =====================================

    def update(

        self,

        current_price,

        timestamp=None

    ):

        if self.position is None:

            return None

        current_price = float(
            current_price
        )

        # =================================
        # 1. POSITION MONITOR
        # =================================

        self.position = self.monitor.update(

            self.position,

            current_price

        )

        # =================================
        # 2. EXIT MANAGER
        # =================================

        exit_reason = self.exit_manager.evaluate(

            self.position,

            current_price

        )

        # =================================
        # 3. CHIUSURA
        # =================================

        if exit_reason is not None:

            return self.close_position(

                exit_reason,

                timestamp,

                current_price

            )

        # =================================
        # POSIZIONE ANCORA APERTA
        # =================================

        return self.position

    # =====================================
    # CHIUSURA POSIZIONE
    # =====================================

    def close_position(

        self,

        reason="MANUALE",

        timestamp=None,

        current_price=None

    ):

        if self.position is None:

            return None

        # =================================
        # PREZZO CORRENTE
        # =================================

        if current_price is None:

            current_price = self.position[
                "current_price"
            ]

        current_price = float(
            current_price
        )

        # =================================
        # DETERMINAZIONE PREZZO USCITA
        # =================================

        reason_upper = str(
            reason
        ).upper()

        # ---------------------------------
        # TAKE PROFIT
        # ---------------------------------

        if reason_upper == "TAKE PROFIT":

            exit_price = float(
                self.position["take_profit"]
            )

        # ---------------------------------
        # BREAK EVEN
        # ---------------------------------

        elif reason_upper == "BREAK EVEN":

            exit_price = float(
                self.position["entry"]
            )

        # ---------------------------------
        # TRAILING STOP
        # ---------------------------------

        elif reason_upper == "TRAILING STOP":

            trailing_stop = self.position.get(
                "trailing_stop"
            )

            if trailing_stop is not None:

                exit_price = float(
                    trailing_stop
                )

            else:

                exit_price = float(
                    self.position["stop_loss"]
                )

        # ---------------------------------
        # STOP LOSS
        # ---------------------------------

        elif reason_upper == "STOP LOSS":

            exit_price = float(
                self.position["stop_loss"]
            )

        # ---------------------------------
        # USCITA MANUALE / ALTRO
        # ---------------------------------

        else:

            exit_price = current_price

        # =================================
        # PREZZO DI USCITA FINALE
        # =================================

        self.position["current_price"] = (
            exit_price
        )

        # =================================
        # CALCOLO PNL FINALE
        # =================================

        side = str(
            self.position["side"]
        ).upper()

        entry = float(
            self.position["entry"]
        )

        size = float(
            self.position.get(
                "size",
                1.0
            )
        )

        if side in (
            "BUY",
            "STRONG BUY"
        ):

            self.position["current_profit"] = round(

                (exit_price - entry) * size,

                6

            )

        elif side in (
            "SELL",
            "STRONG SELL"
        ):

            self.position["current_profit"] = round(

                (entry - exit_price) * size,

                6

            )

        # =================================
        # STATO
        # =================================

        self.position["status"] = "CLOSED"

        self.position["close_reason"] = reason

        self.position["close_time"] = (

            timestamp
            if timestamp is not None
            else datetime.now()

        )

        Logger.success(

            f"Posizione chiusa ({reason})"

        )

        # =================================
        # COPIA POSIZIONE CHIUSA
        # =================================

        closed = self.position.copy()

        # =================================
        # RESET POSIZIONE ATTIVA
        # =================================

        self.position = None

        return closed

    # =====================================
    # POSIZIONE CORRENTE
    # =====================================

    def get_position(self):

        return self.position

    # =====================================
    # VERIFICA POSIZIONE
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