import inspect

from Core.analysis_engine import AnalysisEngine
from Core.risk_manager import RiskManager
from Core.trade_manager import TradeManager

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.41 DECISION -> RISK -> TRADE END-TO-END AUDIT")
print("=" * 100)

print()
print("1. ANALYSIS ENGINE")
print("=" * 100)

print(inspect.getsource(AnalysisEngine))

print()
print("2. RISK MANAGER")
print("=" * 100)

print(inspect.getsource(RiskManager))

print()
print("3. TRADE MANAGER")
print("=" * 100)

print(inspect.getsource(TradeManager))

print()
print("=" * 100)
print("E.27.41 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

