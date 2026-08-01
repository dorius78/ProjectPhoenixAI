"""
========================================
PROJECT PHOENIX AI
Market Analyzer Test
Versione 1.1
========================================
"""

import os
import sys

# =====================================
# ROOT DEL PROGETTO
# =====================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# =====================================
# IMPORT
# =====================================

from Core.market_analyzer import MarketAnalyzer

# =====================================
# TEST
# =====================================

def test_market():

    print("\n==============================")
    print(" MARKET ANALYZER TEST")
    print("==============================\n")

    analyzer = MarketAnalyzer()

    indicators = {

        "ema20": 105,
        "ema50": 100,

        "rsi": 55,

        "macd": 2.0,
        "macd_signal": 1.0,

        "adx": 30,

        "atr": 2,

        "price": 100,

        "volume": 100000,

        "volume_ratio": 1.50,

        "breakout": True,
        "support": True,
        "resistance_break": True,
        "order_block": True,
        "liquidity": True,
        "smart_money": True

    }

    analysis = analyzer.analyze(indicators)

    print("\nRISULTATO ANALISI\n")

    for key, value in analysis.items():
        print(f"{key:<20} {value}")

    print("\nTEST COMPLETATO\n")


# =====================================
# MAIN
# =====================================

if __name__ == "__main__":

    test_market()