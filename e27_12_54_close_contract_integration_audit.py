from pathlib import Path
import inspect

from Execution.execution_engine import ExecutionEngine
from MT5_Bridge.mt5_execution_recovered import MT5ExecutionEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.54 CLOSE CONTRACT INTEGRATION AUDIT")
print("=" * 100)

print()
print("=" * 100)
print("1. EXECUTION ENGINE - CLOSE")
print("=" * 100)

print(
    inspect.getsource(
        ExecutionEngine.close
    )
)

print()
print("=" * 100)
print("2. MT5 BRIDGE - CLOSE_POSITION")
print("=" * 100)

print(
    inspect.getsource(
        MT5ExecutionEngine.close_position
    )
)

print()
print("=" * 100)
print("3. METADATI MT5")
print("=" * 100)

engine_source = inspect.getsource(
    ExecutionEngine.close
)

bridge_source = inspect.getsource(
    MT5ExecutionEngine.close_position
)

keywords = [
    "order_ticket",
    "deal_ticket",
    "position_ticket",
    "mt5_ticket",
    "mt5_symbol",
    "magic",
    "success",
    "executed",
    "retcode",
    "result"
]

print()
print("EXECUTION ENGINE:")

for number, line in enumerate(
    engine_source.splitlines(),
    start=1
):

    if any(
        keyword.lower() in line.lower()
        for keyword in keywords
    ):

        print(
            f"{number:04}: {line}"
        )

print()
print("MT5 BRIDGE:")

for number, line in enumerate(
    bridge_source.splitlines(),
    start=1
):

    if any(
        keyword.lower() in line.lower()
        for keyword in keywords
    ):

        print(
            f"{number:04}: {line}"
        )

print()
print("=" * 100)
print("E.27.12.54 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

