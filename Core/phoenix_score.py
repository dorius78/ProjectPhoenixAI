"""
========================================
PROJECT PHOENIX AI
Phoenix Score
Versione 7.0
========================================
"""

from Logs.logger import Logger


class PhoenixScore:

    def __init__(self):

        Logger.success("Phoenix Score V7 inizializzato.")

    # =====================================
    # CALCOLO SCORE
    # =====================================

    def calculate(self, analysis):

        score = 50

        reasons = []

        # ==========================
        # TREND
        # ==========================

        trend = analysis.get("trend", "NEUTRO")

        if trend == "RIALZISTA":

            score += 20
            reasons.append("Trend rialzista")

        elif trend == "RIBASSISTA":

            score -= 20
            reasons.append("Trend ribassista")

        # ==========================
        # RSI
        # ==========================

        rsi = analysis.get("rsi", "NEUTRALE")

        if rsi == "IPERVENDUTO":

            score += 15
            reasons.append("RSI ipervenduto")

        elif rsi == "IPERCOMPRATO":

            score -= 15
            reasons.append("RSI ipercomprato")

        # ==========================
        # MOMENTUM
        # ==========================

        momentum = analysis.get("momentum", "NEUTRO")

        if momentum == "RIALZISTA":

            score += 15
            reasons.append("Momentum rialzista")

        elif momentum == "RIBASSISTA":

            score -= 15
            reasons.append("Momentum ribassista")

        # ==========================
        # LIMITI
        # ==========================

        score = max(0, min(100, score))

        confidence = score

        # ==========================
        # SEGNALE
        # ==========================

        if score >= 85:

            signal = "STRONG BUY"

        elif score >= 70:

            signal = "BUY"

        elif score <= 15:

            signal = "STRONG SELL"

        elif score <= 30:

            signal = "SELL"

        else:

            signal = "HOLD"

        return {

            "signal": signal,

            "score": score,

            "confidence": confidence,

            "direction_score": score,

            "reasons": reasons

        }