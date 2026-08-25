import inspect

from Core.risk_manager import RiskManager

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.27 RISK TO TRADE INTEGRATION AUDIT")
print("=" * 100)

manager = RiskManager()

print()
print("1. RISK MANAGER build_trade()")
print("=" * 100)

print(
    inspect.getsource(
        RiskManager.build_trade
    )
)

print()
print("2. calculate_position_size()")
print("=" * 100)

print(
    inspect.getsource(
        RiskManager.calculate_position_size
    )
)

print()
print("3. calculate_drawdown()")
print("=" * 100)

print(
    inspect.getsource(
        RiskManager.calculate_drawdown
    )
)

print()
print("=" * 100)
print("E.27.27 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

