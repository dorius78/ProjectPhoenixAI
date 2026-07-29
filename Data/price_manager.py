"""
========================================
PROJECT PHOENIX AI
Price Manager
Versione 0.1
========================================
"""

from Data.market_provider import MarketProvider


class PriceManager:

    def __init__(self):
        print("Price Manager inizializzato.")
        self.provider = MarketProvider()

    def get_last_price(self, symbol):
        return self.provider.get_price(symbol)