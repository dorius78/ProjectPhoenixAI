from Core.live_trading_engine import LiveTradingEngine
import inspect

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.40 CLOSE ROUTING AUDIT")
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
print("3. RICERCA CLOSE REASON")
print("=" * 100)

source1 = inspect.getsource(
    LiveTradingEngine._process_closed_position
)

source2 = inspect.getsource(
    LiveTradingEngine._build_closed_trade
)

combined = source1 + "\n" + source2

keywords = [
    "close_reason",
    "MT5 EXTERNAL CLOSE",
    "execution.close",
    "success",
    "pnl",
    "reason",
    "result",
    "database",
    "backtest",
    "portfolio",
    "guard"
]

for number, line in enumerate(
    combined.splitlines(),
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
print("E.27.12.40 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

