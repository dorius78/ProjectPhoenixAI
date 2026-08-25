from Core.live_trading_engine import LiveTradingEngine
import inspect

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.39 CLOSED POSITION PROCESS AUDIT")
print("=" * 100)

print()
print("=" * 100)
print("METODO _process_closed_position()")
print("=" * 100)

print(
    inspect.getsource(
        LiveTradingEngine._process_closed_position
    )
)

print()
print("=" * 100)
print("RICERCA DATABASE / PORTFOLIO / GUARD / BACKTEST")
print("=" * 100)

source = inspect.getsource(
    LiveTradingEngine._process_closed_position
)

keywords = [
    "database",
    "db.",
    "portfolio",
    "guard",
    "backtest",
    "trade",
    "profit",
    "close",
    "ticket",
    "mt5_ticket",
    "save",
    "add",
    "update",
    "remove"
]

for line_number, line in enumerate(
    source.splitlines(),
    start=1
):

    if any(
        keyword.lower() in line.lower()
        for keyword in keywords
    ):

        print(
            f"{line_number:04}: {line}"
        )

print()
print("=" * 100)
print("E.27.12.39 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

