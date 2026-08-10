"""
========================================
PROJECT PHOENIX AI
Position Controller
Versione 12.4
========================================
"""

from datetime import datetime

from Logs.logger import Logger
from Core.position_monitor import PositionMonitor
from Core.exit_manager import ExitManager


class PositionController:

    def __init__(self):

        Logger.success(
            "Position Controller V12.4 inizializzato."
        )

        self.position = None

        # =================================
        # POSITION MONITOR
        # =================================
        #
        # Responsabile di:
        # - prezzo corrente
        # - profitto corrente
        # - massimo profitto

        self.monitor = PositionMonitor()

        # =================================
        # EXIT MANAGER
        # =================================
        #
        # Responsabile di:
        # - Break Even
        # - Trailing Stop
        # - Stop Loss
        # - Take Profit

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
        #
        # Live Trading:
        # viene utilizzata l'ora reale.
        #
        # Backtest:
        # viene utilizzato il timestamp
        # della candela storica.

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
            # Questo valore NON viene mai modificato
            # da Break Even o Trailing Stop.

            "initial_stop_loss": stop_loss,

            # Stop Loss corrente.
            # Questo valore può essere modificato
            # durante la gestione della posizione.

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
        #
        # Aggiorna:
        # - current_price
        # - current_profit
        # - max_profit

        self.position = self.monitor.update(

            self.position,

            current_price

        )

        # =================================
        # 2. EXIT MANAGER
        # =================================
        #
        # Gestisce:
        # - Break Even
        # - Trailing Stop
        # - Stop Loss
        # - Take Profit

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

                timestamp

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

        timestamp=None

    ):

        if self.position is None:

            return None

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