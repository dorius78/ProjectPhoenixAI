from pathlib import Path

path = Path(
    "Execution/execution_validator.py"
)

text = path.read_text(
    encoding="utf-8-sig"
)

old = '''    def validate(self, trade):

        if trade is None:

            return False, "Nessun trade"

        signal = str(

            trade.get(

                "signal",

                "HOLD"

            )

        ).upper()

        if signal == "HOLD":

            return False, "Segnale HOLD"

        if signal not in (

            "BUY",

            "SELL",

            "STRONG BUY",

            "STRONG SELL"

        ):

            return False, "Segnale non valido"

        return True, ""
'''

new = '''    def validate(self, trade):

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
'''

count = text.count(old)

print("=" * 100)
print("E.27.57 EXECUTION VALIDATOR CONTRACT PATCH")
print("=" * 100)
print(
    f"TARGET OCCURRENCES = {count}"
)

if count != 1:

    raise RuntimeError(
        "STOP: blocco validate non trovato "
        "in modo univoco."
    )

text = text.replace(
    old,
    new,
    1
)

path.write_text(
    text,
    encoding="utf-8"
)

print()
print("PATCH APPLICATA: OK")
print()
print("TRADE PRESENCE: FIX")
print("REQUIRED FIELDS: FIX")
print("SIGNAL/SIDE CONSISTENCY: FIX")
print("NUMERIC VALUES: FIX")
print("POSITIVE VALUES: FIX")
print("BUY SL/ENTRY/TP: FIX")
print("SELL TP/ENTRY/SL: FIX")
print()
print("RISK AI: INVARIATO")
print("TRADE BUILDER: INVARIATO")
print("EXECUTION ENGINE: INVARIATO")
print("MT5: INVARIATO")
print()
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

