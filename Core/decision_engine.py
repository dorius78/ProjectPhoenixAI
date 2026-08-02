"""
========================================
PROJECT PHOENIX AI
Decision Engine
Versione 7.1
========================================
"""

from Logs.logger import Logger


class DecisionEngine:

    def __init__(self):

        Logger.success("Decision Engine V7 inizializzato.")

    # =====================================
    # ANALISI
    # =====================================

    def analyze(self, action):

        valid = [

            "BUY",
            "SELL",
            "HOLD",
            "STRONG BUY",
            "STRONG SELL"

        ]

        if action not in valid:

            Logger.warning(
                f"Azione non valida: {action}"
            )

            action = "HOLD"

        return action