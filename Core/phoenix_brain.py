"""
========================================
PROJECT PHOENIX AI
Phoenix Brain
Versione 5.0
========================================
"""

from Logs.logger import Logger


class PhoenixBrain:

    def __init__(self):

        Logger.success("Phoenix Brain inizializzato.")

    def think(self, analysis, risk):

        trend = analysis["trend"]
        trend_strength = analysis["trend_strength"]

        ema_position = analysis["ema_position"]
        sma_position = analysis["sma_position"]

        macd_status = analysis["macd_status"]

        rsi = analysis["rsi"]
        momentum = analysis["momentum"]

        adx = analysis["adx"]

        score = 50

        reasons = []
        warnings = []

        # ==========================
        # TREND
        # ==========================

        if trend == "RIALZISTA":

            score += 20
            reasons.append("Trend rialzista")

        elif trend == "RIBASSISTA":

            score -= 20
            reasons.append("Trend ribassista")

        else:

            warnings.append("Trend neutro")

        # ==========================
        # ADX
        # ==========================

        if adx >= 40:

            score += 15
            reasons.append(f"ADX molto forte ({adx})")

        elif adx >= 25:

            score += 10
            reasons.append(f"ADX forte ({adx})")

        elif adx >= 20:

            score += 5
            reasons.append(f"ADX discreto ({adx})")

        else:

            score -= 5
            warnings.append(f"ADX debole ({adx})")

        # ==========================
        # TREND STRENGTH
        # ==========================

        if trend_strength == "MOLTO FORTE":

            score += 10

        elif trend_strength == "FORTE":

            score += 5

        elif trend_strength == "DEBOLE":

            score -= 5

        # ==========================
        # EMA
        # ==========================

        if ema_position == "SOPRA":

            score += 5
            reasons.append("Prezzo sopra EMA20")

        else:

            score -= 5
            warnings.append("Prezzo sotto EMA20")

        # ==========================
        # SMA
        # ==========================

        if sma_position == "SOPRA":

            score += 5
            reasons.append("Prezzo sopra SMA20")

        else:

            score -= 5
            warnings.append("Prezzo sotto SMA20")

        # ==========================
        # MACD
        # ==========================

        if macd_status == "POSITIVO":

            score += 10
            reasons.append("MACD positivo")

        else:

            score -= 10
            warnings.append("MACD negativo")

        # ==========================
        # RSI
        # ==========================

        if rsi == "IPERVENDUTO":

            score += 15
            reasons.append("RSI ipervenduto")

        elif rsi == "IPERCOMPRATO":

            score -= 15
            warnings.append("RSI ipercomprato")

        else:

            reasons.append("RSI neutrale")

        # ==========================
        # MOMENTUM
        # ==========================

        if momentum == "RIALZISTA":

            score += 10
            reasons.append("Momentum rialzista")

        else:

            score -= 10
            warnings.append("Momentum ribassista")

        # ==========================
        # LIMITI
        # ==========================

        score = max(0, min(score, 100))

        # ==========================
        # ACTION
        # ==========================

        if score >= 80:

            action = "BUY"

        elif score <= 20:

            action = "SELL"

        else:

            action = "HOLD"

        # ==========================
        # STRENGTH
        # ==========================

        if score >= 90:

            strength = "ECCELLENTE"

        elif score >= 80:

            strength = "MOLTO FORTE"

        elif score >= 70:

            strength = "FORTE"

        elif score >= 50:

            strength = "MEDIA"

        else:

            strength = "DEBOLE"

        # ==========================
        # RISK
        # ==========================

        if risk["risk_level"] == "LOW":

            risk_level = "BASSO"

        elif risk["risk_level"] == "MEDIUM":

            risk_level = "MEDIO"

        else:

            risk_level = "ALTO"

        # ==========================
        # CONFIDENCE
        # ==========================

        confidence = score

        if risk_level == "MEDIO":

            confidence -= 10

        elif risk_level == "ALTO":

            confidence -= 20

        confidence = max(0, min(confidence, 100))

        # ==========================
        # OUTPUT
        # ==========================

        return {

            "action": action,

            "score": score,

            "confidence": confidence,

            "strength": strength,

            "risk": risk_level,

            "adx": adx,

            "reasons": reasons,

            "warnings": warnings

        }