"""
========================================
PROJECT PHOENIX AI
Yahoo Finance Provider
Versione 0.2
========================================
"""

import yfinance as yf


class YFinanceProvider:

    def __init__(self):
        print("Yahoo Finance Provider inizializzato.")

    def get_price(self, symbol):

        try:

            ticker = yf.Ticker(symbol)

            # Tentativo 1
            data = ticker.history(period="5d", interval="1d")

            if not data.empty:
                price = float(data["Close"].iloc[-1])
                print(f"{symbol} -> {price}")
                return price

            # Tentativo 2
            info = ticker.fast_info

            if info is not None and "lastPrice" in info:
                price = float(info["lastPrice"])
                print(f"{symbol} -> {price}")
                return price

            print(f"Nessun prezzo trovato per {symbol}")
            return None

        except Exception as e:
            print(f"Errore Yahoo Finance: {e}")
            return None