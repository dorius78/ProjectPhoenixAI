"""
========================================
PROJECT PHOENIX AI
Signal Manager
Versione 2.1
========================================
"""

from Logs.logger import Logger


class SignalManager:

    def __init__(self):

        Logger.success("Signal Manager inizializzato.")

    def generate_signal(

        self,

        decision,

        brain,

        risk

    ):

        Logger.section("SIGNAL MANAGER")

        # ==========================
        # CONTROLLO RISCHIO
        # ==========================

        if not risk["allow_trade"]:

            Logger.warning("Trade bloccato dal Risk Manager.")

            return "HOLD"

        # ==========================
        # CONTROLLO CONFIDENCE
        # ==========================

        confidence = brain["confidence"]

        if confidence < 60:

            Logger.info(
                f"Confidence troppo bassa ({confidence}%)."
            )

            return "HOLD"

        # ==========================
        # CONFERMA BUY
        # ==========================

        if (
            decision == "BUY"
            and brain["action"] == "BUY"
        ):

            Logger.success("Segnale BUY confermato.")

            return "BUY"

        # ==========================
        # CONFERMA SELL
        # ==========================

        if (
            decision == "SELL"
            and brain["action"] == "SELL"
        ):

            Logger.success("Segnale SELL confermato.")

            return "SELL"

        # ==========================
        # NESSUN SEGNALE
        # ==========================

        Logger.info("Nessun segnale valido.")

        return "HOLD"