"""
========================================
PROJECT PHOENIX AI
Risk Limits
Versione 1.0
========================================
"""

from Logs.logger import Logger


class RiskLimits:

    def __init__(self):

        Logger.success(
            "Risk Limits V1 inizializzato."
        )

    def evaluate(self, analysis):

        trend = analysis.get("trend", "NEUTRO")
        momentum = analysis.get("momentum", "NEUTRO")
        rsi = analysis.get("rsi", "NEUTRALE")

        score = 50

        if trend == "RIALZISTA":

            score += 20

        elif trend == "RIBASSISTA":

            score += 20

        if momentum in (

            "RIALZISTA",

            "RIBASSISTA"

        ):

            score += 20

        if rsi == "NEUTRALE":

            score += 10

        if score >= 70:

            level = "BASSO"
            allow_trade = True

        elif score >= 50:

            level = "MEDIO"
            allow_trade = True

        else:

            level = "ALTO"
            allow_trade = False

        return {

            "risk_level": level,

            "risk_score": score,

            "allow_trade": allow_trade

        }