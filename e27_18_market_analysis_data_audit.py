import inspect

from Core.market_analyzer import MarketAnalyzer
from Core.smart_money import SmartMoney

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.18 MARKET ANALYSIS DATA AUDIT")
print("=" * 100)

# ============================================================
# MARKET ANALYZER
# ============================================================

print()
print("1. MARKET ANALYZER")
print("=" * 100)

print(
    inspect.getsource(
        MarketAnalyzer.analyze
    )
)

# ============================================================
# SMART MONEY
# ============================================================

print()
print("2. SMART MONEY")
print("=" * 100)

methods = [
    "detect_bos",
    "detect_choch",
    "detect_fvg",
    "detect_order_block",
    "detect_liquidity",
]

for method_name in methods:

    if hasattr(
        SmartMoney,
        method_name
    ):

        print()
        print("-" * 100)
        print(
            f"{method_name}()"
        )
        print("-" * 100)

        print(
            inspect.getsource(
                getattr(
                    SmartMoney,
                    method_name
                )
            )
        )

print()
print("=" * 100)
print("E.27.18 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

