"""
========================================
PROJECT PHOENIX AI
Market Provider
Versione 0.2
========================================
"""

from Data.yfinance_provider import YFinanceProvider


class MarketProvider:

    def __init__(self):
        print("Market Provider inizializzato.")
        self.provider = YFinanceProvider()

    def connect(self):
        print("Connessione a Yahoo Finance...")

    def disconnect(self):
        print("Disconnessione.")

    def get_price(self, symbol):
        return self.provider.get_price(symbol)