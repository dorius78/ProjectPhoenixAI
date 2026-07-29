"""
PROJECT PHOENIX AI
Risk Manager
Versione 0.1
"""

from Logs.logger import Logger


class RiskManager:

    def __init__(self):

        Logger.success("Risk Manager inizializzato.")

    def evaluate(self, analysis):

        trend = analysis["trend"]
        rsi = analysis["rsi"]
        momentum = analysis["momentum"]

        risk_score = 0

        # ==========================
        # Trend
        # ==========================

        if trend == "RIALZISTA":
            risk_score += 1

        elif trend == "RIBASSISTA":
            risk_score += 1

        # ==========================
        # RSI
        # ==========================

        if rsi == "NORMALE":
            risk_score += 2

        elif rsi in ["IPERCOMPRATO", "IPERVENDUTO"]:
            risk_score += 1

        # ==========================
        # Momentum
        # ==========================

        if momentum in ["RIALZISTA", "RIBASSISTA"]:
            risk_score += 2

        # ==========================
        # Livello di rischio
        # ==========================

        if risk_score >= 5:

            level = "BASSO"
            allow_trade = True

        elif risk_score >= 3:

            level = "MEDIO"
            allow_trade = True

        else:

            level = "ALTO"
            allow_trade = False

        return {
            "risk_level": level,
            "risk_score": risk_score,
            "allow_trade": allow_trade
        }