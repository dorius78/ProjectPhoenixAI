"""
========================================
PROJECT PHOENIX AI
Phoenix Brain
Versione 8.0
========================================
"""

from Logs.logger import Logger


class PhoenixBrain:

    def __init__(self):

        Logger.success("Phoenix Brain V8 inizializzato.")

    # =====================================
    # AI DECISION
    # =====================================

    def think(self, analysis, risk):

        score = 50

        reasons = []
        warnings = []

        # =====================================
        # TREND
        # =====================================

        if analysis.get("trend_bullish"):

            score += 20
            reasons.append("Trend rialzista")

        elif analysis.get("trend_bearish"):

            score -= 20
            warnings.append("Trend ribassista")

        # =====================================
        # EMA
        # =====================================

        if analysis.get("ema_alignment"):

            score += 10
            reasons.append("EMA allineate")

        # =====================================
        # MACD
        # =====================================

        if analysis.get("macd_buy"):

            score += 10
            reasons.append("MACD BUY")

        elif analysis.get("macd_sell"):

            score -= 10
            warnings.append("MACD SELL")

        # =====================================
        # RSI
        # =====================================

        rsi = float(analysis.get("rsi", 50))

        if rsi < 30:

            score += 15
            reasons.append("RSI ipervenduto")

        elif rsi > 70:

            score -= 15
            warnings.append("RSI ipercomprato")

        elif 45 <= rsi <= 60:

            score += 5
            reasons.append("RSI equilibrato")

        # =====================================
        # ADX
        # =====================================

        if analysis.get("adx_strong"):

            score += 10
            reasons.append("Trend forte")

        # =====================================
        # VOLUME
        # =====================================

        if analysis.get("volume_high"):

            score += 10
            reasons.append("Volume elevato")

        # =====================================
        # SMART MONEY
        # =====================================

        if analysis.get("bos_bullish"):

            score += 15
            reasons.append("BOS Rialzista")

        if analysis.get("bos_bearish"):

            score -= 15
            warnings.append("BOS Ribassista")

        if analysis.get("choch"):

            score += 10
            reasons.append("CHoCH")

        if analysis.get("fvg"):

            score += 8
            reasons.append("Fair Value Gap")

        if analysis.get("order_block"):

            score += 10
            reasons.append("Order Block")

        if analysis.get("liquidity"):

            score += 8
            reasons.append("Liquidity Sweep")

        # =====================================
        # LIMITI
        # =====================================

        score = max(0, min(score, 100))

        confidence = score

        if risk["risk_level"] == "MEDIO":

            confidence -= 10

        elif risk["risk_level"] == "ALTO":

            confidence -= 20

        confidence = max(0, min(confidence, 100))

        # =====================================
        # DECISIONE
        # =====================================

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

            "confidence": confidence,

            "strength": score,

            "risk": risk["risk_level"],

            "reasons": reasons,

            "warnings": warnings

        }