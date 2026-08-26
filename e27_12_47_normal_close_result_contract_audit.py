from Core.live_trading_engine import LiveTradingEngine
import inspect

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.47 NORMAL CLOSE RESULT CONTRACT AUDIT")
print("=" * 100)

print()
print("=" * 100)
print("1. _process_closed_position()")
print("=" * 100)

print(
    inspect.getsource(
        LiveTradingEngine._process_closed_position
    )
)

print()
print("=" * 100)
print("2. _build_closed_trade()")
print("=" * 100)

print(
    inspect.getsource(
        LiveTradingEngine._build_closed_trade
    )
)

print()
print("=" * 100)
print("3. EXECUTION CLOSE")
print("=" * 100)

from Execution.execution_engine import ExecutionEngine

print(
    inspect.getsource(
        ExecutionEngine.close
    )
)

print()
print("=" * 100)
print("4. CAMPI CONTRATTO")
print("=" * 100)

keywords = [
    "success",
    "executed",
    "dry_run",
    "symbol",
    "side",
    "entry",
    "exit",
    "pnl",
    "reason",
    "close_time",
    "mt5_ticket",
    "order_ticket",
    "deal_ticket",
    "position_ticket",
    "retcode",
    "result"
]

sources = [
    (
        "PROCESS CLOSED",
        inspect.getsource(
            LiveTradingEngine._process_closed_position
        )
    ),
    (
        "BUILD CLOSED TRADE",
        inspect.getsource(
            LiveTradingEngine._build_closed_trade
        )
    ),
    (
        "EXECUTION CLOSE",
        inspect.getsource(
            ExecutionEngine.close
        )
    )
]

for name, source in sources:

    print()
    print("-" * 100)
    print(name)
    print("-" * 100)

    for number, line in enumerate(
        source.splitlines(),
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
print("E.27.12.47 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

