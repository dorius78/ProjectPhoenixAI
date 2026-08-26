import inspect

from Execution.execution_engine import ExecutionEngine
from Core.live_trading_engine import LiveTradingEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.32 MT5 TICKET PROPAGATION AUDIT")
print("=" * 100)

print()
print("1. EXECUTION ENGINE execute()")
print("=" * 100)

print(
    inspect.getsource(
        ExecutionEngine.execute
    )
)

print()
print("2. LIVE ENGINE _open_position_from_order()")
print("=" * 100)

print(
    inspect.getsource(
        LiveTradingEngine._open_position_from_order
    )
)

print()
print("3. LIVE ENGINE _sync_mt5_position()")
print("=" * 100)

print(
    inspect.getsource(
        LiveTradingEngine._sync_mt5_position
    )
)

print()
print("=" * 100)
print("E.27.32 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

