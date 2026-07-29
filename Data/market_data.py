"""
========================================
PROJECT PHOENIX AI
Market Data Manager
Versione 0.1
========================================
"""

from Data.market_provider import MarketProvider


class MarketData:

    def __init__(self):
        print("Market Data Manager inizializzato.")
        self.provider = MarketProvider()

    def load_markets(self):
        print("Caricamento dei mercati...")

        self.provider.connect()

        markets = [
            "Forex",
            "Crypto",
            "Azioni",
            "Indici",
            "Futures",
            "Commodities"
        ]

        for market in markets:
            print(f"✔ {market} disponibile")

        return markets

    def get_price(self, symbol):
        return self.provider.get_price(symbol)