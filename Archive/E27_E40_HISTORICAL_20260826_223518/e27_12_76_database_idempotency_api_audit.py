from pathlib import Path
import inspect

from Database.database_manager import DatabaseManager

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.76 DATABASE IDEMPOTENCY API AUDIT")
print("=" * 100)

print()
print("1. DATABASE save_trade()")
print("=" * 100)

print(
    inspect.getsource(
        DatabaseManager.save_trade
    )
)

print()
print("2. DATABASE ATTRIBUTI")
print("=" * 100)

methods = [
    name
    for name in dir(DatabaseManager)
    if not name.startswith("__")
]

for name in methods:

    attribute = getattr(
        DatabaseManager,
        name
    )

    if callable(attribute):

        print(
            f"{name}: METHOD"
        )

print()
print("3. DATABASE INTERNALS")
print("=" * 100)

source = Path(
    "Database/database_manager.py"
).read_text(
    encoding="utf-8"
)

keywords = [
    "self.connection",
    "self.cursor",
    "SELECT",
    "trade_id",
    "load_trades",
    "save_trade",
]

for number, line in enumerate(
    source.splitlines(),
    start=1
):

    if any(
        keyword.lower()
        in line.lower()
        for keyword in keywords
    ):

        print(
            f"{number:04}: {line.strip()}"
        )

print()
print("=" * 100)
print("E.27.12.76 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

