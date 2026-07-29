"""
========================================
PROJECT PHOENIX AI
ADX Indicator
Versione 1.0
========================================
"""

from Logs.logger import Logger


class ADX:

    def __init__(self):

        Logger.success("ADX Indicator inizializzato.")

    def calculate(self, data, period=14):

        high = data["High"]
        low = data["Low"]
        close = data["Close"]

        # ==========================
        # MOVIMENTI DIREZIONALI
        # ==========================

        plus_dm = high.diff()
        minus_dm = -low.diff()

        plus_dm = plus_dm.where(
            (plus_dm > minus_dm) & (plus_dm > 0),
            0
        )

        minus_dm = minus_dm.where(
            (minus_dm > plus_dm) & (minus_dm > 0),
            0
        )

        # ==========================
        # TRUE RANGE
        # ==========================

        tr1 = high - low
        tr2 = (high - close.shift()).abs()
        tr3 = (low - close.shift()).abs()

        tr = tr1.combine(tr2, max).combine(tr3, max)

        atr = tr.rolling(window=period).mean()

        # ==========================
        # INDICATORI DIREZIONALI
        # ==========================

        plus_di = 100 * (
            plus_dm.rolling(window=period).mean() / atr
        )

        minus_di = 100 * (
            minus_dm.rolling(window=period).mean() / atr
        )

        # ==========================
        # DX
        # ==========================

        dx = (
            (plus_di - minus_di).abs()
            /
            (plus_di + minus_di)
        ) * 100

        # ==========================
        # ADX
        # ==========================

        adx = dx.rolling(window=period).mean()

        return adx