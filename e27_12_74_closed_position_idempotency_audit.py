from pathlib import Path
import inspect

from Core.live_trading_engine import LiveTradingEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.74 CLOSED POSITION IDEMPOTENCY AUDIT")
print("=" * 100)

source = inspect.getsource(
    LiveTradingEngine._process_closed_position
)

print()
print("METODO COMPLETO")
print("=" * 100)
print(source)

print()
print("=" * 100)
print("E.27.12.74 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

