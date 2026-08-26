import inspect

from Core.trade_manager import TradeManager

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.51 TRADE MANAGER → TRADE BUILDER AUDIT")
print("=" * 100)

manager = TradeManager()

print()
print("TRADE MANAGER SOURCE")
print("=" * 100)

print(
    inspect.getsource(
        TradeManager
    )
)

print()
print("=" * 100)
print("E.27.51 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

