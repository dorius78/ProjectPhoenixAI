"""
========================================
PROJECT PHOENIX AI
Market Analyzer
Versione 7.1
========================================
"""

from Logs.logger import Logger


class MarketAnalyzer:

    def __init__(self):

        self.last_analysis = None

        Logger.success("Market Analyzer V7 inizializzato.")

    # =====================================
    # ANALISI MERCATO
    # =====================================

    def analyze(self, indicators):

        ema20 = float(indicators.get("ema20", 0))
        ema50 = float(indicators.get("ema50", 0))

        rsi = float(indicators.get("rsi", 50))

        macd = float(indicators.get("macd", 0))
        macd_signal = float(indicators.get("macd_signal", 0))

        adx = float(indicators.get("adx", 0))
        atr = float(indicators.get("atr", 0))

        price = float(indicators.get("price", 0))

        volume = float(indicators.get("volume", 0))
        volume_ratio = float(indicators.get("volume_ratio", 1))

        analysis = {

            # Trend

            "trend": (
                "RIALZISTA"
                if ema20 > ema50
                else "RIBASSISTA"
                if ema20 < ema50
                else "LATERALE"
            ),

            "trend_bullish": ema20 > ema50,
            "trend_bearish": ema20 < ema50,

            "ema_alignment": abs(ema20 - ema50) > 0,

            # RSI

            "rsi": rsi,

            "rsi_state": (
                "IPERCOMPRATO"
                if rsi > 70
                else "IPERVENDUTO"
                if rsi < 30
                else "NEUTRALE"
            ),

            "rsi_ok": 30 <= rsi <= 70,

            # MACD

            "macd": macd,
            "macd_signal": macd_signal,

            "macd_buy": macd > macd_signal,
            "macd_sell": macd < macd_signal,

            # ADX

            "adx": adx,
            "adx_strong": adx >= 25,

            # ATR

            "atr": atr,

            # Prezzo

            "price": price,

            # Volume

            "volume": volume,
            "volume_ratio": volume_ratio,
            "volume_high": volume_ratio >= 1.20,

            # Smart Money

            "breakout": indicators.get("breakout", False),

            "support": indicators.get("support", False),

            "resistance_break": indicators.get(
                "resistance_break",
                False
            ),

            "order_block": indicators.get(
                "order_block",
                False
            ),

            "liquidity": indicators.get(
                "liquidity",
                False
            ),

            "smart_money": indicators.get(
                "smart_money",
                False
            )

        }

        self.last_analysis = analysis

        Logger.info("Analisi mercato completata.")

        return analysis

    # =====================================
    # EXPORT
    # =====================================

    def export(self):

        return self.last_analysis