"""
========================================
PROJECT PHOENIX AI
Signal Manager
Versione 7.0
========================================
"""

from Config.settings import MIN_CONFIDENCE
from Logs.logger import Logger


class SignalManager:

    def __init__(self):

        Logger.success("Signal Manager V7 inizializzato.")

    # =====================================
    # VALIDAZIONE
    # =====================================

    def validate(self, decision):

        signal = str(
            decision.get("signal", "HOLD")
        ).upper()

        score = abs(
            float(
                decision.get("score", 0)
            )
        )

        confidence = abs(
            float(
                decision.get(
                    "confidence",
                    score
                )
            )
        )

        reasons = decision.get(
            "reasons",
            []
        )

        valid = False

        if signal in (
            "STRONG BUY",
            "STRONG SELL"
        ):

            valid = True

        elif signal in (
            "BUY",
            "SELL"
        ):

            valid = (
                confidence >= MIN_CONFIDENCE
            )

        return {

            "valid": valid,

            "signal": signal,

            "score": score,

            "confidence": confidence,

            "reasons": reasons

        }

    # =====================================
    # BUY
    # =====================================

    def is_buy(self, signal):

        return str(signal).upper() in (

            "BUY",

            "STRONG BUY"

        )

    # =====================================
    # SELL
    # =====================================

    def is_sell(self, signal):

        return str(signal).upper() in (

            "SELL",

            "STRONG SELL"

        )

    # =====================================
    # HOLD
    # =====================================

    def is_hold(self, signal):

        return str(signal).upper() == "HOLD"

    # =====================================
    # ESECUZIONE
    # =====================================

    def should_execute(
        self,
        validation
    ):

        return validation["valid"]

    # =====================================
    # REPORT
    # =====================================

    def summary(self, validation):

        Logger.separator()

        Logger.title("SIGNAL MANAGER")

        Logger.info(
            f"Segnale      : {validation['signal']}"
        )

        Logger.info(
            f"Score        : {validation['score']}"
        )

        Logger.info(
            f"Confidence   : {validation['confidence']:.2f}"
        )

        Logger.info(
            f"Eseguibile   : {validation['valid']}"
        )

        for reason in validation["reasons"]:

            Logger.info(f"✔ {reason}")

        Logger.separator()

    # =====================================
    # EXPORT
    # =====================================

    def export(self, validation):

        return validation.copy()

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        Logger.info(
            "Signal Manager resettato."
        )