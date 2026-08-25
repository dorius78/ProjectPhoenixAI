import inspect

from Core.analysis_engine import AnalysisEngine
from Core.signal_manager import SignalManager
from Core.trade_builder import TradeBuilder

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.50 DECISION → SIGNAL → TRADE BUILDER AUDIT")
print("=" * 100)

print()
print("1. ANALYSIS ENGINE")
print("=" * 100)
print(inspect.getsource(AnalysisEngine))

print()
print("2. SIGNAL MANAGER")
print("=" * 100)
print(inspect.getsource(SignalManager))

print()
print("3. TRADE BUILDER")
print("=" * 100)
print(inspect.getsource(TradeBuilder))

print()
print("=" * 100)
print("E.27.50 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

