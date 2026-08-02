"""
========================================
PROJECT PHOENIX AI
Signal Manager
Versione 7.1
========================================
"""

from Logs.logger import Logger


class SignalManager:

    def __init__(self):

        Logger.success("Signal Manager V7 inizializzato.")

    # =====================================
    # GENERAZIONE SEGNALE
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

        return signal.upper() in (

            "BUY",

            "STRONG BUY"

        )

    # =====================================
    # SELL
    # =====================================

    def is_sell(self, signal):

        return signal.upper() in (

            "SELL",

            "STRONG SELL"

        )

    # =====================================
    # HOLD
    # =====================================

    def is_hold(self, signal):

        return signal.upper() == "HOLD"

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        Logger.info("Signal Manager resettato.")