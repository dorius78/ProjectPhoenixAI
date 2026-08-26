from pathlib import Path
import inspect

from Core.live_trading_engine import LiveTradingEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.75 TRADE IDEMPOTENCY KEY AUDIT")
print("=" * 100)

source = inspect.getsource(
    LiveTradingEngine._build_closed_trade
)

print()
print("1. _build_closed_trade()")
print("=" * 100)
print(source)

print()
print("=" * 100)
print("2. TRADE ID / MT5 TICKET NEL LIVE ENGINE")
print("=" * 100)

path = Path(
    "Core/live_trading_engine.py"
)

lines = path.read_text(
    encoding="utf-8"
).splitlines()

keywords = [
    "trade_id",
    "mt5_ticket",
    "mt5_order_ticket",
    "mt5_deal_ticket",
]

for number, line in enumerate(
    lines,
    start=1
):

    if any(
        keyword in line
        for keyword in keywords
    ):

        print(
            f"{number:04}: {line.strip()}"
        )

print()
print("=" * 100)
print("3. DATABASE API DISPONIBILE")
print("=" * 100)

from Database.database_manager import DatabaseManager

methods = [
    name
    for name in dir(DatabaseManager)
    if not name.startswith("__")
]

for method in methods:
    attribute = getattr(
        DatabaseManager,
        method
    )

    if callable(attribute):
        print(method)

print()
print("=" * 100)
print("E.27.12.75 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

