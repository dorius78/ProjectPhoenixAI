import inspect

from Core.risk_manager import RiskManager
from Core.trade_builder import TradeBuilder

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.52 RISK AI → TRADE BUILDER CONTRACT AUDIT")
print("=" * 100)

risk = RiskManager()
builder = TradeBuilder()

print()
print("1. RISK MANAGER")
print("=" * 100)
print(inspect.getsource(RiskManager))

print()
print("2. TRADE BUILDER")
print("=" * 100)
print(inspect.getsource(TradeBuilder))

print()
print("=" * 100)
print("E.27.52 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

