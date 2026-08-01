"""
========================================
PROJECT PHOENIX AI
Indicator Manager
Versione 7.0
========================================
"""

from Logs.logger import Logger

from .ema import EMA
from .sma import SMA
from .rsi import RSI
from .macd import MACD
from .atr import ATR
from .adx import ADX
from .bollinger import Bollinger


class IndicatorManager:

    def __init__(self):

        Logger.success("Indicator Manager V7 inizializzato.")

        self.ema = EMA()
        self.sma = SMA()
        self.rsi = RSI()
        self.macd = MACD()
        self.atr = ATR()
        self.adx = ADX()
        self.bollinger = Bollinger()

    # =====================================
    # INDICATORI COMPLETI
    # =====================================

    def get_indicators(self, data):

        ema20 = self.ema.calculate(data, 20)
        ema50 = self.ema.calculate(data, 50)

        sma20 = self.sma.calculate(data, 20)

        rsi = self.rsi.calculate(data, 14)

        macd, macd_signal, histogram = (
            self.macd.calculate(data)
        )

        atr = self.atr.calculate(data, 14)

        adx = self.adx.calculate(data, 14)

        price = float(data["Close"].iloc[-1])

        volume = float(data["Volume"].iloc[-1])

        volume_avg = float(
            data["Volume"].tail(20).mean()
        )

        volume_ratio = (

            volume / volume_avg

            if volume_avg > 0

            else 1.0

        )

        return {

            "price": price,

            "ema20": float(ema20.iloc[-1]),
            "ema50": float(ema50.iloc[-1]),

            "sma20": float(sma20.iloc[-1]),

            "rsi": float(rsi.iloc[-1]),

            "macd": float(macd.iloc[-1]),
            "macd_signal": float(macd_signal.iloc[-1]),
            "macd_histogram": float(histogram.iloc[-1]),

            "atr": float(atr.iloc[-1]),

            "adx": float(adx.iloc[-1]),

            "volume": volume,

            "volume_ratio": volume_ratio,

            "breakout": False,
            "support": False,
            "resistance_break": False,
            "order_block": False,
            "liquidity": False,
            "smart_money": False

        }