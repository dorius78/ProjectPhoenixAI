"""
========================================
PROJECT PHOENIX AI
Execution Validator
Versione 1.0
========================================
"""

from Logs.logger import Logger


class ExecutionValidator:

    def __init__(self):

        Logger.success(
            "Execution Validator V1 inizializzato."
        )

    def validate(self, trade):

        # =====================================
        # TRADE PRESENTE
        # =====================================

        if trade is None:

            return False, "Nessun trade"

        if not isinstance(trade, dict):

            return False, "Trade non valido"

        # =====================================
        # SIGNAL
        # =====================================

        signal = str(
            trade.get(
                "signal",
                "HOLD"
            )
        ).upper().strip()

        if signal == "HOLD":

            return False, "Segnale HOLD"

        if signal not in (
            "BUY",
            "SELL",
            "STRONG BUY",
            "STRONG SELL"
        ):

            return False, "Segnale non valido"

        # =====================================
        # CAMPI OBBLIGATORI
        # =====================================

        required_fields = (
            "symbol",
            "side",
            "entry",
            "stop_loss",
            "take_profit",
            "atr",
            "size"
        )

        for field in required_fields:

            if field not in trade:

                return False, (
                    f"Campo trade mancante: {field}"
                )

        # =====================================
        # SIDE
        # =====================================

        side = str(
            trade.get(
                "side"
            )
        ).upper().strip()

        if side not in (
            "BUY",
            "SELL"
        ):

            return False, "Side non valido"

        expected_side = (
            "BUY"
            if "BUY" in signal
            else "SELL"
        )

        if side != expected_side:

            return False, (
                "Signal e side non coerenti"
            )

        # =====================================
        # VALORI NUMERICI
        # =====================================

        try:

            entry = float(
                trade["entry"]
            )

            stop_loss = float(
                trade["stop_loss"]
            )

            take_profit = float(
                trade["take_profit"]
            )

            atr = float(
                trade["atr"]
            )

            size = float(
                trade["size"]
            )

        except (
            TypeError,
            ValueError
        ):

            return False, (
                "Valori numerici non validi"
            )

        # =====================================
        # VALORI POSITIVI
        # =====================================

        if entry <= 0:

            return False, "Entry non valida"

        if atr <= 0:

            return False, "ATR non valido"

        if size <= 0:

            return False, "Size non valida"

        if stop_loss <= 0:

            return False, "Stop Loss non valido"

        if take_profit <= 0:

            return False, "Take Profit non valido"

        # =====================================
        # COERENZA BUY
        # =====================================

        if side == "BUY":

            if not (
                stop_loss < entry < take_profit
            ):

                return False, (
                    "Livelli BUY non coerenti"
                )

        # =====================================
        # COERENZA SELL
        # =====================================

        elif side == "SELL":

            if not (
                take_profit < entry < stop_loss
            ):

                return False, (
                    "Livelli SELL non coerenti"
                )

        # =====================================
        # VALID
        # =====================================

        return True, ""

