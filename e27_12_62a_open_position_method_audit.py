from Core.live_trading_engine import LiveTradingEngine
import inspect

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.62A OPEN POSITION METHOD AUDIT")
print("=" * 100)

print()
print("FIRMA:")
print("-" * 100)

print(
    inspect.signature(
        LiveTradingEngine._open_position_from_order
    )
)

print()
print("SOURCE:")
print("-" * 100)

print(
    inspect.getsource(
        LiveTradingEngine._open_position_from_order
    )
)

print()
print("=" * 100)
print("E.27.12.62A AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

