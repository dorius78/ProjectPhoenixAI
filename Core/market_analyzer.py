"""
========================================
PROJECT PHOENIX AI
Market Analyzer
Versione 3.0
========================================
"""

from Logs.logger import Logger


class MarketAnalyzer:

    def __init__(self):

        Logger.success("Market Analyzer inizializzato.")

    def analyze(
        self,
        data,
        ema20,
        sma20,
        rsi14,
        macd,
        signal,
        adx14
    ):

        last_close = data["Close"].iloc[-1]

        # ==========================
        # TREND
        # ==========================

        trend = "NEUTRO"

        if (
            last_close > ema20.iloc[-1]
            and last_close > sma20.iloc[-1]
        ):
            trend = "RIALZISTA"

        elif (
            last_close < ema20.iloc[-1]
            and last_close < sma20.iloc[-1]
        ):
            trend = "RIBASSISTA"

        # ==========================
        # ADX
        # ==========================

        adx_value = float(adx14.iloc[-1])

        if adx_value >= 40:
            trend_strength = "MOLTO FORTE"

        elif adx_value >= 25:
            trend_strength = "FORTE"

        elif adx_value >= 20:
            trend_strength = "MEDIA"

        else:
            trend_strength = "DEBOLE"

        # ==========================
        # EMA
        # ==========================

        ema_position = (
            "SOPRA"
            if last_close > ema20.iloc[-1]
            else "SOTTO"
        )

        # ==========================
        # SMA
        # ==========================

        sma_position = (
            "SOPRA"
            if last_close > sma20.iloc[-1]
            else "SOTTO"
        )

        # ==========================
        # RSI
        # ==========================

        if rsi14.iloc[-1] > 70:

            rsi_status = "IPERCOMPRATO"

        elif rsi14.iloc[-1] < 30:

            rsi_status = "IPERVENDUTO"

        else:

            rsi_status = "NEUTRALE"

        # ==========================
        # MACD
        # ==========================

        if macd.iloc[-1] > signal.iloc[-1]:

            momentum = "RIALZISTA"
            macd_status = "POSITIVO"

        else:

            momentum = "RIBASSISTA"
            macd_status = "NEGATIVO"

        # ==========================
        # OUTPUT
        # ==========================

        return {

            "trend": trend,

            "trend_strength": trend_strength,

            "adx": round(adx_value, 2),

            "ema_position": ema_position,

            "sma_position": sma_position,

            "macd_status": macd_status,

            "rsi": rsi_status,

            "momentum": momentum

        }