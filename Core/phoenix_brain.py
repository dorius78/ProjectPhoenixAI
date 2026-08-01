"""
========================================
PROJECT PHOENIX AI
Phoenix Brain
Versione 7.0
========================================
"""

from Logs.logger import Logger


class PhoenixBrain:

    def __init__(self):

        Logger.success("Phoenix Brain V7 inizializzato.")

    def think(self, analysis, risk):

        score = 50

        reasons = []
        warnings = []

        # ==========================
        # TREND
        # ==========================

        if analysis["trend_bullish"]:

            score += 20
            reasons.append("Trend rialzista")

        elif analysis["trend_bearish"]:

            score -= 20
            warnings.append("Trend ribassista")

        # ==========================
        # EMA
        # ==========================

        if analysis["ema_alignment"]:

            score += 10
            reasons.append("EMA allineate")

        # ==========================
        # MACD
        # ==========================

        if analysis["macd_buy"]:

            score += 10
            reasons.append("MACD BUY")

        elif analysis["macd_sell"]:

            score -= 10
            warnings.append("MACD SELL")

        # ==========================
        # RSI
        # ==========================

        rsi = analysis["rsi"]

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

        if analysis["adx_strong"]:

            score += 10
            reasons.append("Trend forte")

        # ==========================
        # VOLUME
        # ==========================

        if analysis["volume_high"]:

            score += 5
            reasons.append("Volume elevato")

        # ==========================
        # SMART MONEY
        # ==========================

        if analysis["breakout"]:

            score += 5
            reasons.append("Breakout")

        if analysis["order_block"]:

            score += 5
            reasons.append("Order Block")

        if analysis["liquidity"]:

            score += 5
            reasons.append("Liquidity")

        if analysis["smart_money"]:

            score += 10
            reasons.append("Smart Money")

        # ==========================
        # LIMITI
        # ==========================

        score = max(0, min(score, 100))

        # ==========================
        # AZIONE
        # ==========================

        if score >= 80:

            action = "BUY"

        elif score <= 20:

            action = "SELL"

        else:

            action = "HOLD"

        # ==========================
        # CONFIDENCE
        # ==========================

        confidence = score

        if risk["risk_level"] == "MEDIO":

            confidence -= 10

        elif risk["risk_level"] == "ALTO":

            confidence -= 20

        confidence = max(0, min(confidence, 100))

        return {

            "action": action,

            "score": score,

            "confidence": confidence,

            "reasons": reasons,

            "warnings": warnings

        }