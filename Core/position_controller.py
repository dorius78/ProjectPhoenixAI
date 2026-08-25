"""
========================================
PROJECT PHOENIX AI
Position Controller
Versione 12.0
========================================
"""

from datetime import datetime

from Logs.logger import Logger
from Config.settings import BREAK_EVEN_BUFFER_PERCENT


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

        size=1.0,

        timestamp=None

    ):

        if self.position is not None:

            Logger.warning("Posizione già aperta.")

            return False

        # Nel Live Trading non passiamo "timestamp": qui si usa l'ora
        # reale del PC, corretto per operazioni dal vivo. Nel Backtest
        # invece si passa la data della candela storica, altrimenti
        # ogni trade risulterebbe aperto e chiuso nello stesso istante
        # reale (il backtest gira in pochi secondi).
        open_time = timestamp if timestamp is not None else datetime.now()

        self.position = {

            "symbol": symbol,

            "side": side,

            "entry": float(entry),

            "stop_loss": float(stop_loss),

            "initial_stop_loss": float(stop_loss),

            "take_profit": float(take_profit),

            "size": float(size),

            "status": "OPEN",

            "open_time": open_time,

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

        current_price,

        timestamp=None,

        high=None,

        low=None

    ):

        if self.position is None:

            return None

        current_price = float(current_price)

        entry = self.position["entry"]

        side = self.position["side"]

        size = self.position.get("size", 1.0)

        # =====================================
        # PREZZO CORRENTE
        # =====================================

        self.position["current_price"] = current_price

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
        # OHLC INTRABAR
        # =====================================

        candle_high = (

            float(high)

            if high is not None

            else current_price

        )

        candle_low = (

            float(low)

            if low is not None

            else current_price

        )

        # =====================================
        # SL / TP PRIMA DI BE / TRAILING
        # =====================================

        if side == "BUY":

            if candle_low <= self.position["stop_loss"]:

                return self.close_position(

                    "STOP LOSS",

                    timestamp,

                    exit_price=self.position["stop_loss"]

                )

            if candle_high >= self.position["take_profit"]:

                return self.close_position(

                    "TAKE PROFIT",

                    timestamp,

                    exit_price=self.position["take_profit"]

                )

        else:

            if candle_high >= self.position["stop_loss"]:

                return self.close_position(

                    "STOP LOSS",

                    timestamp,

                    exit_price=self.position["stop_loss"]

                )

            if candle_low <= self.position["take_profit"]:

                return self.close_position(

                    "TAKE PROFIT",

                    timestamp,

                    exit_price=self.position["take_profit"]

                )

        # =====================================
        # BREAK EVEN
        # =====================================

        break_even_buffer = (
            float(BREAK_EVEN_BUFFER_PERCENT) / 100.0
        )

        if (

            not self.position["break_even"]

            and (
                (
                    side == "BUY"
                    and current_price >= (
                        entry * (1 + break_even_buffer)
                    )
                )
                or
                (
                    side == "SELL"
                    and current_price <= (
                        entry * (1 - break_even_buffer)
                    )
                )
            )

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

        return self.position

    # =====================================
    # CHIUSURA POSIZIONE
    # =====================================

    def close_position(

        self,

        reason="MANUALE",

        timestamp=None,

        exit_price=None,

        current_price=None

    ):

        if self.position is None:

            return None

        if current_price is not None:

            if exit_price is not None:
                print(
                    "ERRORE: usare exit_price oppure current_price, non entrambi."
                )
                raise ValueError(
                    "exit_price e current_price non possono essere usati insieme."
                )

            exit_price = current_price

        if exit_price is not None:

            exit_price = float(exit_price)

            self.position["current_price"] = exit_price

            entry = self.position["entry"]
            size = self.position.get("size", 1.0)
            side = self.position["side"]

            if side == "BUY":

                profit = (exit_price - entry) * size

            else:

                profit = (entry - exit_price) * size

            self.position["current_profit"] = round(
                profit,
                6
            )

        self.position["status"] = "CLOSED"

        self.position["close_reason"] = reason

        self.position["close_time"] = (
            timestamp if timestamp is not None else datetime.now()
        )

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