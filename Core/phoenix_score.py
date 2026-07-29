"""
========================================
PROJECT PHOENIX AI
Phoenix Score
Versione 1.0
========================================
"""

from Logs.logger import Logger


class PhoenixScore:

    def __init__(self):

        Logger.success("Phoenix Score inizializzato.")

    def calculate(self, analysis):

        score = 50

        # ==========================
        # TREND
        # ==========================

        if analysis["trend"] == "RIALZISTA":
            score += 20

        elif analysis["trend"] == "RIBASSISTA":
            score -= 20

        # ==========================
        # RSI
        # ==========================

        if analysis["rsi"] == "IPERVENDUTO":
            score += 15

        elif analysis["rsi"] == "IPERCOMPRATO":
            score -= 15

        # ==========================
        # MOMENTUM
        # ==========================

        if analysis["momentum"] == "RIALZISTA":
            score += 15

        elif analysis["momentum"] == "RIBASSISTA":
            score -= 15

        # ==========================
        # LIMITI
        # ==========================

        score = max(0, min(score, 100))

        # ==========================
        # AFFIDABILITA'
        # ==========================

        confidence = score

        # ==========================
        # OPERAZIONE
        # ==========================

        if score >= 70:
            action = "BUY"

        elif score <= 30:
            action = "SELL"

        else:
            action = "HOLD"

        return {

            "score": score,
            "confidence": confidence,
            "action": action

        }