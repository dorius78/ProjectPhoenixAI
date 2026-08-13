"""
========================================
PROJECT PHOENIX AI
Phoenix Brain Logic
Versione 4.0
========================================
"""

from Logs.logger import Logger


class PhoenixBrainLogic:

    def __init__(self):

        Logger.success(
            "Phoenix Brain Logic V4 inizializzato."
        )

    # =====================================
    # CALCOLO DECISIONALE
    # =====================================

    def calculate(self, analysis, risk):

        bullish_score = 0
        bearish_score = 0

        bullish_reasons = []
        bearish_reasons = []

        # =====================================
        # TREND
        # =====================================

        if analysis.get("trend_bullish"):

            bullish_score += 20

            bullish_reasons.append(
                "Trend rialzista"
            )

        elif analysis.get("trend_bearish"):

            bearish_score += 20

            bearish_reasons.append(
                "Trend ribassista"
            )

        # =====================================
        # EMA
        # =====================================

        if analysis.get("ema_alignment_bullish"):

            bullish_score += 10

            bullish_reasons.append(
                "EMA allineate al rialzo"
            )

        elif analysis.get("ema_alignment_bearish"):

            bearish_score += 10

            bearish_reasons.append(
                "EMA allineate al ribasso"
            )

        # =====================================
        # MACD
        # =====================================

        if analysis.get("macd_buy"):

            bullish_score += 10

            bullish_reasons.append(
                "MACD BUY"
            )

        elif analysis.get("macd_sell"):

            bearish_score += 10

            bearish_reasons.append(
                "MACD SELL"
            )

        # =====================================
        # RSI
        # =====================================

        rsi = float(
            analysis.get("rsi", 50)
        )

        if rsi < 30:

            bullish_score += 15

            bullish_reasons.append(
                "RSI ipervenduto"
            )

        elif rsi > 70:

            bearish_score += 15

            bearish_reasons.append(
                "RSI ipercomprato"
            )

        # =====================================
        # ADX
        # =====================================

        if analysis.get("adx_strong"):

            if analysis.get("trend_bullish"):

                bullish_score += 10

                bullish_reasons.append(
                    "Trend forte (rialzista)"
                )

            elif analysis.get("trend_bearish"):

                bearish_score += 10

                bearish_reasons.append(
                    "Trend forte (ribassista)"
                )

        # =====================================
        # VOLUME
        # =====================================

        if analysis.get("volume_high"):

            if analysis.get("trend_bullish"):

                bullish_score += 10

                bullish_reasons.append(
                    "Volume elevato (conferma rialzo)"
                )

            elif analysis.get("trend_bearish"):

                bearish_score += 10

                bearish_reasons.append(
                    "Volume elevato (conferma ribasso)"
                )

        # =====================================
        # SMART MONEY - BOS
        # =====================================

        if analysis.get("bos_bullish"):

            bullish_score += 15

            bullish_reasons.append(
                "BOS Rialzista"
            )

        if analysis.get("bos_bearish"):

            bearish_score += 15

            bearish_reasons.append(
                "BOS Ribassista"
            )

        # =====================================
        # SMART MONEY - CHoCH
        # =====================================

        if analysis.get("choch_bullish"):

            bullish_score += 10

            bullish_reasons.append(
                "CHoCH Rialzista"
            )

        elif analysis.get("choch_bearish"):

            bearish_score += 10

            bearish_reasons.append(
                "CHoCH Ribassista"
            )

        # =====================================
        # SMART MONEY - FVG
        # =====================================

        if analysis.get("fvg_bullish"):

            bullish_score += 8

            bullish_reasons.append(
                "Fair Value Gap Rialzista"
            )

        elif analysis.get("fvg_bearish"):

            bearish_score += 8

            bearish_reasons.append(
                "Fair Value Gap Ribassista"
            )

        # =====================================
        # SMART MONEY - ORDER BLOCK
        # =====================================

        if analysis.get("order_block_bullish"):

            bullish_score += 10

            bullish_reasons.append(
                "Order Block Rialzista"
            )

        elif analysis.get("order_block_bearish"):

            bearish_score += 10

            bearish_reasons.append(
                "Order Block Ribassista"
            )

        # =====================================
        # SMART MONEY - LIQUIDITY
        # =====================================

        if analysis.get("liquidity_bullish"):

            bullish_score += 8

            bullish_reasons.append(
                "Liquidity Sweep Rialzista"
            )

        elif analysis.get("liquidity_bearish"):

            bearish_score += 8

            bearish_reasons.append(
                "Liquidity Sweep Ribassista"
            )

        # =====================================
        # SCORE NETTO
        # =====================================

        score = 50 + (
            bullish_score - bearish_score
        )

        score = max(
            0,
            min(score, 100)
        )

        # =====================================
        # CONFLITTO
        # =====================================

        conflict = (
            bullish_score > 0
            and bearish_score > 0
        )

        # =====================================
        # DIREZIONE DOMINANTE
        # =====================================

        if bullish_score > bearish_score:

            dominant_direction = "BULLISH"

            reasons = bullish_reasons
            warnings = bearish_reasons

        elif bearish_score > bullish_score:

            dominant_direction = "BEARISH"

            reasons = bearish_reasons
            warnings = bullish_reasons

        else:

            dominant_direction = "NEUTRAL"

            reasons = []
            warnings = (
                bullish_reasons
                + bearish_reasons
            )

        # =====================================
        # CONFIDENCE
        # =====================================

        confidence = abs(
            score - 50
        ) * 2

        confidence = max(
            0,
            min(confidence, 100)
        )

        # =====================================
        # PENALITÀ CONFLITTO
        # =====================================

        if conflict:

            confidence -= 10

        # =====================================
        # PENALITÀ RISCHIO
        # =====================================

        risk_level = risk.get(
            "risk_level",
            "BASSO"
        )

        if risk_level == "MEDIO":

            confidence -= 10

        elif risk_level == "ALTO":

            confidence -= 20

        confidence = max(
            0,
            min(confidence, 100)
        )

        # =====================================
        # OUTPUT
        # =====================================

        return {

            "score": score,

            "confidence": confidence,

            "bullish_score": bullish_score,

            "bearish_score": bearish_score,

            "conflict": conflict,

            "dominant_direction": dominant_direction,

            "reasons": reasons,

            "warnings": warnings,

            "bullish_reasons": bullish_reasons,

            "bearish_reasons": bearish_reasons

        }