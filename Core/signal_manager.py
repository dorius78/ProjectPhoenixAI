"""
========================================
PROJECT PHOENIX AI
Signal Manager
Versione 9.0
========================================
"""

from Config.settings import MIN_CONFIDENCE
from Logs.logger import Logger


class SignalManager:

    def __init__(self):

        Logger.success("Signal Manager V9 inizializzato.")

    # =====================================
    # VALIDAZIONE
    # =====================================

    def validate(self, decision):

        signal = str(

            decision.get("action", "HOLD")

        ).upper()

        confidence = float(

            decision.get("confidence", 0)

        )

        score = int(

            decision.get("score", 0)

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

            valid = confidence >= MIN_CONFIDENCE

        return {

            "valid": valid,

            "signal": signal,

            "score": score,

            "confidence": confidence,

            "reasons": decision.get(

                "reasons",

                []

            )

        }

    # =====================================
    # GENERAZIONE
    # =====================================

    def generate_signal(

        self,

        decision,

        brain,

        risk

    ):

        if not risk["allow_trade"]:

            return "HOLD"

        action = brain["action"].upper()

        if action in (

            "BUY",

            "SELL",

            "STRONG BUY",

            "STRONG SELL",

            "HOLD"

        ):

            return action

        return "HOLD"

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
    # RESET
    # =====================================

    def reset(self):

        Logger.info("Signal Manager resettato.")