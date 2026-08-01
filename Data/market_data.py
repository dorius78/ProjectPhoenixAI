"""
========================================
PROJECT PHOENIX AI
Market Data Manager
Versione 7.0
========================================
"""

from Logs.logger import Logger
from Data.market_provider import MarketProvider


class MarketData:

    def __init__(self):

        Logger.success("Market Data Manager V7 inizializzato.")

        self.provider = MarketProvider()

        self.markets = []

    # =====================================
    # CARICAMENTO MERCATI
    # =====================================

    def load_markets(self):

        Logger.section("MARKET DATA")

        self.provider.connect()

        self.markets = [

            "Forex",

            "Crypto",

            "Azioni",

            "Indici",

            "Futures",

            "Commodities"

        ]

        for market in self.markets:

            Logger.success(f"{market} disponibile")

        return self.markets

    # =====================================
    # PREZZO
    # =====================================

    def get_price(self, symbol):

        return self.provider.get_price(symbol)

    # =====================================
    # LISTA MERCATI
    # =====================================

    def get_markets(self):

        return self.markets