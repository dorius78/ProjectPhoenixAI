"""
========================================
PROJECT PHOENIX AI
Decision Engine
Versione 1.0
========================================
"""

from Logs.logger import Logger


class DecisionEngine:

    def __init__(self):

        Logger.success("Decision Engine inizializzato.")

    def analyze(self, signal):

        Logger.section("DECISION ENGINE")

        # ==========================
        # VALIDAZIONE SEGNALE
        # ==========================

        valid_signals = [

            "BUY",
            "SELL",
            "HOLD"

        ]

        if signal not in valid_signals:

            Logger.warning(
                f"Segnale non valido: {signal}"
            )

            return "HOLD"

        Logger.success(
            f"Decisione finale: {signal}"
        )

        return signal