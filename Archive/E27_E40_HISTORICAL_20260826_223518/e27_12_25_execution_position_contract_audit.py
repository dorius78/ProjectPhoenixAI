from pathlib import Path
import inspect

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.25 EXECUTION -> POSITION CONTRACT AUDIT")
print("=" * 100)

print()
print("=" * 100)
print("1. EXECUTION ENGINE")
print("=" * 100)

from Execution.execution_engine import ExecutionEngine

print(inspect.getsource(
    ExecutionEngine.execute
))

print()
print("=" * 100)
print("2. LIVE TRADING ENGINE - OPEN POSITION")
print("=" * 100)

from Core.live_trading_engine import LiveTradingEngine

print(inspect.getsource(
    LiveTradingEngine._open_position_from_order
))

print()
print("=" * 100)
print("3. RICERCA CAMPI MT5")
print("=" * 100)

path = Path("Core/live_trading_engine.py")
lines = path.read_text(
    encoding="utf-8"
).splitlines()

keywords = [
    "order_ticket",
    "deal_ticket",
    "position_ticket",
    "mt5_ticket",
    "mt5_symbol",
    "magic",
    "executed",
    "success",
    "portfolio.add",
    "position_controller.open_position",
]

for i, line in enumerate(lines):

    if any(
        keyword.lower() in line.lower()
        for keyword in keywords
    ):
        print(
            f"{i+1:04}: {line}"
        )

print()
print("=" * 100)
print("E.27.12.25 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)
