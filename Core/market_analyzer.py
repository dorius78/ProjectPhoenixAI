"""
========================================
PROJECT PHOENIX AI
Market Analyzer
Versione 7.0
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

        ema20 = float(indicators["ema20"])
        ema50 = float(indicators["ema50"])

        rsi = float(indicators["rsi"])

        macd = float(indicators["macd"])
        macd_signal = float(indicators["macd_signal"])

        adx = float(indicators["adx"])

        atr = float(indicators["atr"])

        volume_ratio = float(indicators["volume_ratio"])

        analysis = {

            # ==========================
            # TREND
            # ==========================

            "trend_bullish": ema20 > ema50,

            "trend_bearish": ema20 < ema50,

            "ema_alignment": abs(ema20 - ema50) > 0,

            # ==========================
            # RSI
            # ==========================

            "rsi": rsi,

            "rsi_ok": 30 <= rsi <= 70,

            # ==========================
            # MACD
            # ==========================

            "macd_buy": macd > macd_signal,

            "macd_sell": macd < macd_signal,

            # ==========================
            # ADX
            # ==========================

            "adx": adx,

            "adx_strong": adx >= 25,

            # ==========================
            # ATR
            # ==========================

            "atr": atr,

            # ==========================
            # PREZZO
            # ==========================

            "price": float(indicators["price"]),

            # ==========================
            # VOLUME
            # ==========================

            "volume": float(indicators["volume"]),

            "volume_ratio": volume_ratio,

            "volume_high": volume_ratio >= 1.20,

            # ==========================
            # SMART MONEY
            # ==========================

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