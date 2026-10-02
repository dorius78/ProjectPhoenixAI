"""
========================================
PROJECT PHOENIX AI
Phoenix Brain Logic
Versione 4.0
========================================
"""

from Logs.logger import Logger
from Config import settings


class PhoenixBrainLogic:

    def __init__(self):

        Logger.success(
            "Phoenix Brain Logic V4 inizializzato."
        )

    # =====================================
    # CALCOLO DECISIONALE
    # =====================================

    def calculate(self, analysis, risk, regime=None):

        bullish_score = 0
        bearish_score = 0

        bullish_reasons = []
        bearish_reasons = []

        # =====================================
        # TREND
        # =====================================

        if analysis.get("trend_bullish"):

            bullish_score += settings.PHOENIX_WEIGHT_TREND

            bullish_reasons.append(
                "Trend rialzista"
            )

        if analysis.get("trend_bearish"):

            bearish_score += settings.PHOENIX_WEIGHT_TREND

            bearish_reasons.append(
                "Trend ribassista"
            )

        # =====================================
        # EMA
        # =====================================

        if analysis.get("ema_alignment_bullish"):

            bullish_score += settings.PHOENIX_WEIGHT_EMA

            bullish_reasons.append(
                "EMA allineate al rialzo"
            )

        if analysis.get("ema_alignment_bearish"):

            bearish_score += settings.PHOENIX_WEIGHT_EMA

            bearish_reasons.append(
                "EMA allineate al ribasso"
            )

        # =====================================
        # MACD
        # =====================================

        if analysis.get("macd_buy"):

            bullish_score += settings.PHOENIX_WEIGHT_MACD

            bullish_reasons.append(
                "MACD BUY"
            )

        if analysis.get("macd_sell"):

            bearish_score += settings.PHOENIX_WEIGHT_MACD

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

            bullish_score += settings.PHOENIX_WEIGHT_RSI

            bullish_reasons.append(
                "RSI ipervenduto"
            )

        elif rsi > 70:

            bearish_score += settings.PHOENIX_WEIGHT_RSI

            bearish_reasons.append(
                "RSI ipercomprato"
            )

        # =====================================
        # ADX
        # =====================================

        if analysis.get("adx_strong"):

            if analysis.get("trend_bullish"):

                bullish_score += settings.PHOENIX_WEIGHT_ADX

                bullish_reasons.append(
                    "Trend forte (rialzista)"
                )

            elif analysis.get("trend_bearish"):

                bearish_score += settings.PHOENIX_WEIGHT_ADX

                bearish_reasons.append(
                    "Trend forte (ribassista)"
                )

        # =====================================
        # VOLUME
        # =====================================

        if analysis.get("volume_high"):

            if analysis.get("trend_bullish"):

                bullish_score += settings.PHOENIX_WEIGHT_VOLUME

                bullish_reasons.append(
                    "Volume elevato (conferma rialzo)"
                )

            elif analysis.get("trend_bearish"):

                bearish_score += settings.PHOENIX_WEIGHT_VOLUME

                bearish_reasons.append(
                    "Volume elevato (conferma ribasso)"
                )

        # =====================================
        # SMART MONEY - BOS
        # =====================================

        if analysis.get("bos_bullish"):

            bullish_score += settings.PHOENIX_WEIGHT_BOS

            bullish_reasons.append(
                "BOS Rialzista"
            )

        if analysis.get("bos_bearish"):

            bearish_score += settings.PHOENIX_WEIGHT_BOS

            bearish_reasons.append(
                "BOS Ribassista"
            )

        # =====================================
        # SMART MONEY - CHoCH
        # =====================================

        if analysis.get("choch_bullish"):

            bullish_score += settings.PHOENIX_WEIGHT_CHOCH

            bullish_reasons.append(
                "CHoCH Rialzista"
            )

        if analysis.get("choch_bearish"):

            bearish_score += settings.PHOENIX_WEIGHT_CHOCH

            bearish_reasons.append(
                "CHoCH Ribassista"
            )

        # =====================================
        # SMART MONEY - FVG
        # =====================================

        if analysis.get("fvg_bullish"):

            bullish_score += settings.PHOENIX_WEIGHT_FVG

            bullish_reasons.append(
                "Fair Value Gap Rialzista"
            )

        if analysis.get("fvg_bearish"):

            bearish_score += settings.PHOENIX_WEIGHT_FVG

            bearish_reasons.append(
                "Fair Value Gap Ribassista"
            )

        # =====================================
        # SMART MONEY - ORDER BLOCK
        # =====================================

        if analysis.get("order_block_bullish"):

            bullish_score += settings.PHOENIX_WEIGHT_ORDER_BLOCK

            bullish_reasons.append(
                "Order Block Rialzista"
            )

        if analysis.get("order_block_bearish"):

            bearish_score += settings.PHOENIX_WEIGHT_ORDER_BLOCK

            bearish_reasons.append(
                "Order Block Ribassista"
            )

        # =====================================
        # SMART MONEY - LIQUIDITY
        # =====================================

        if analysis.get("liquidity_bullish"):

            bullish_score += settings.PHOENIX_WEIGHT_LIQUIDITY

            bullish_reasons.append(
                "Liquidity Sweep Rialzista"
            )

        if analysis.get("liquidity_bearish"):

            bearish_score += settings.PHOENIX_WEIGHT_LIQUIDITY

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
            abs(bullish_score - bearish_score) < settings.PHOENIX_CONFLICT_THRESHOLD
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

        net_advantage = abs(
            bullish_score - bearish_score
        )

        total_score = (
            bullish_score
            + bearish_score
        )

        if total_score <= 0:
            confidence = 0
        else:
            dominance = (
                net_advantage
                / total_score
            ) * 100

            confidence = (
                50
                + (dominance * 0.75)
            )

        if not conflict:
            confidence += settings.PHOENIX_CONFIDENCE_NO_CONFLICT_BONUS

        if conflict:
            confidence -= settings.PHOENIX_CONFIDENCE_CONFLICT_PENALTY

        # =====================================
        # PENALITÀ CONFLITTO
        # =====================================

        if conflict:

            confidence -= settings.PHOENIX_CONFIDENCE_CONFLICT_PENALTY

        # =====================================
        # PENALITÀ RISCHIO
        # =====================================

        risk_level = risk.get(
            "risk_level",
            "BASSO"
        )

        if risk_level == "MEDIO":

            confidence -= settings.PHOENIX_CONFIDENCE_RISK_MEDIUM_PENALTY

        elif risk_level == "ALTO":

            confidence -= settings.PHOENIX_CONFIDENCE_RISK_HIGH_PENALTY

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
