"""
========================================
PROJECT PHOENIX AI
Bollinger Bands
Versione 1.0
========================================
"""

from Config.settings import SMA_PERIOD


class Bollinger:

    def __init__(self):

        print("Bollinger Bands inizializzate.")

    def calculate(self, data, period=SMA_PERIOD, std=2):

        close = data["Close"]

        middle_band = close.rolling(
            window=period
        ).mean()

        standard_deviation = close.rolling(
            window=period
        ).std()

        upper_band = (
            middle_band +
            (standard_deviation * std)
        )

        lower_band = (
            middle_band -
            (standard_deviation * std)
        )

        return (
            upper_band,
            middle_band,
            lower_band
        )