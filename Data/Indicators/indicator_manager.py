"""
========================================
PROJECT PHOENIX AI
Indicator Manager
Versione 0.7
========================================
"""

from .ema import EMA
from .sma import SMA
from .rsi import RSI
from .macd import MACD
from .atr import ATR
from .adx import ADX
from .bollinger import Bollinger


class IndicatorManager:

    def __init__(self):

        print("Indicator Manager inizializzato.")

        self.ema = EMA()
        self.sma = SMA()
        self.rsi = RSI()
        self.macd = MACD()
        self.atr = ATR()
        self.adx = ADX()
        self.bollinger = Bollinger()

    # ==========================
    # EMA
    # ==========================

    def calculate_ema(self, data, period=20):
        return self.ema.calculate(data, period)

    # ==========================
    # SMA
    # ==========================

    def calculate_sma(self, data, period=20):
        return self.sma.calculate(data, period)

    # ==========================
    # RSI
    # ==========================

    def calculate_rsi(self, data, period=14):
        return self.rsi.calculate(data, period)

    # ==========================
    # MACD
    # ==========================

    def calculate_macd(self, data):
        return self.macd.calculate(data)

    # ==========================
    # ATR
    # ==========================

    def calculate_atr(self, data, period=14):
        return self.atr.calculate(data, period)

    # ==========================
    # ADX
    # ==========================

    def calculate_adx(self, data, period=14):
        return self.adx.calculate(data, period)

    # ==========================
    # BOLLINGER BANDS
    # ==========================

    def calculate_bollinger(self, data):
        return self.bollinger.calculate(data)