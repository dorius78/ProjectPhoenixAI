from pathlib import Path
import inspect

from Core.live_trading_engine import LiveTradingEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.56 MT5 LIFECYCLE FINAL AUDIT")
print("=" * 100)

methods = [
    "_sync_mt5_position",
    "_open_position_from_order",
    "_process_closed_position",
    "_build_closed_trade",
]

source_file = Path(
    "Core/live_trading_engine.py"
)

text = source_file.read_text(
    encoding="utf-8"
)

print()
print("=" * 100)
print("1. METODI LIFECYCLE")
print("=" * 100)

for method in methods:

    print()
    print(f"--- {method} ---")

    if hasattr(
        LiveTradingEngine,
        method
    ):
        print("PRESENT: OK")
    else:
        print("PRESENT: FAIL")


print()
print("=" * 100)
print("2. MT5 CONTRACT FIELDS")
print("=" * 100)

fields = [
    "mt5_ticket",
    "mt5_order_ticket",
    "mt5_deal_ticket",
    "mt5_symbol",
    "magic",
    "current_price",
    "current_profit",
]

for field in fields:

    count = text.count(
        f'"{field}"'
    )

    print(
        f"{field}: {count} occurrence(s)"
    )


print()
print("=" * 100)
print("3. CLOSE ROUTING")
print("=" * 100)

checks = {
    "MT5 EXTERNAL CLOSE":
        "external_mt5_close",

    "execution.close":
        "self.execution.close",

    "database.save_trade":
        "self.database.save_trade",

    "backtest.add_trade":
        "self.backtest.add_trade",

    "portfolio.update_balance":
        "self.portfolio.update_balance",

    "guard.register_trade":
        "self.guard.register_trade",

    "portfolio.remove":
        "self.portfolio.remove",
}

for name, token in checks.items():

    print(
        f"{name}: "
        f"{'FOUND' if token in text else 'NOT FOUND'}"
    )


print()
print("=" * 100)
print("4. ORDER SEND LOCATIONS")
print("=" * 100)

for number, line in enumerate(
    text.splitlines(),
    start=1
):

    if "order_send" in line:

        print(
            f"{number:04}: {line.strip()}"
        )


print()
print("=" * 100)
print("5. BACKUP / VERSION STATE")
print("=" * 100)

backups = sorted(
    Path("Core").glob(
        "live_trading_engine.py.E27.*.backup"
    )
)

for backup in backups:

    print(
        backup.name
    )

print()
print(
    f"BACKUP COUNT: {len(backups)}"
)

print()
print("=" * 100)
print("E.27.12.56 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

