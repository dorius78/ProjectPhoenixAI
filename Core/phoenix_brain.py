"""
========================================
PROJECT PHOENIX AI
Phoenix Brain
Versione 9.0
========================================
"""

from Logs.logger import Logger

from Core.phoenix_brain_logic import PhoenixBrainLogic


class PhoenixBrain:

    def __init__(self):

        Logger.success(
            "Phoenix Brain V9 inizializzato."
        )

        self.logic = PhoenixBrainLogic()

    def think(

        self,

        analysis,

        risk

    ):

        data = self.logic.calculate(

            analysis,

            risk

        )

        score = data["score"]

        if score >= 90:

            action = "STRONG BUY"

        elif score >= 70:

            action = "BUY"

        elif score <= 10:

            action = "STRONG SELL"

        elif score <= 30:

            action = "SELL"

        else:

            action = "HOLD"

        return {

            "action": action,

            "score": score,

            "confidence": data["confidence"],

            "strength": score,

            "risk": risk["risk_level"],

            "reasons": data["reasons"],

            "warnings": data["warnings"]

        }