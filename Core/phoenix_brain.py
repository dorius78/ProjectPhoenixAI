"""
========================================
PROJECT PHOENIX AI
Phoenix Brain
Versione 7.1
========================================
"""

from Logs.logger import Logger


class PhoenixBrain:

    def __init__(self):

        Logger.success("Phoenix Brain V7 inizializzato.")

    # =====================================
    # AI DECISION
    # =====================================

    def think(self, analysis, risk):

        score = 50

        reasons = []
        warnings = []

        # ==========================
        # TREND
        # ==========================

        if analysis.get("trend_bullish", False):

            score += 20
            reasons.append("Trend rialzista")

        elif analysis.get("trend_bearish", False):

            score -= 20
            warnings.append("Trend ribassista")

        # ==========================
        # EMA
        # ==========================

        if analysis.get("ema_alignment", False):

            score += 10
            reasons.append("EMA allineate")

        # ==========================
        # MACD
        # ==========================

        if analysis.get("macd_buy", False):

            score += 10
            reasons.append("MACD BUY")

        elif analysis.get("macd_sell", False):

            score -= 10
            warnings.append("MACD SELL")

        # ==========================
        # RSI
        # ==========================

        rsi = float(analysis.get("rsi", 50))

        if 45 <= rsi <= 60:

            score += 10
            reasons.append("RSI equilibrato")

        elif rsi > 70:

            score -= 15
            warnings.append("RSI ipercomprato")

        elif rsi < 30:

            score += 15
            reasons.append("RSI ipervenduto")

        # ==========================
        # ADX
        # ==========================

        if analysis.get("adx_strong", False):

            score += 10
            reasons.append("Trend forte")

        # ==========================
        # VOLUME
        # ==========================

        if analysis.get("volume_high", False):

            score += 5
            reasons.append("Volume elevato")

        # ==========================
        # SMART MONEY
        # ==========================

        for key, text in [

            ("breakout", "Breakout"),
            ("order_block", "Order Block"),
            ("liquidity", "Liquidity"),
            ("smart_money", "Smart Money")

        ]:

            if analysis.get(key, False):

                score += 5
                reasons.append(text)

        # ==========================
        # LIMITI
        # ==========================

        score = max(0, min(score, 100))

        confidence = score

        if risk["risk_level"] == "MEDIO":

            confidence -= 10

        elif risk["risk_level"] == "ALTO":

            confidence -= 20

        confidence = max(0, min(confidence, 100))

        # ==========================
        # AZIONE
        # ==========================

        if score >= 85:

            action = "STRONG BUY"

        elif score >= 70:

            action = "BUY"

        elif score <= 15:

            action = "STRONG SELL"

        elif score <= 30:

            action = "SELL"

        else:

            action = "HOLD"

        return {

            "action": action,

            "score": score,

            "confidence": confidence,

            "strength": score,

            "risk": risk["risk_level"],

            "reasons": reasons,

            "warnings": warnings

        }