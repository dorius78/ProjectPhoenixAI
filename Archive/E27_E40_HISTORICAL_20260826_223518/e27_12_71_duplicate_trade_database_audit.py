from pathlib import Path

files = [
    Path("Core/live_trading_engine.py"),
    Path("Core/database.py"),
    Path("Database/database.py"),
]

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.71 DUPLICATE TRADE DATABASE AUDIT")
print("=" * 100)

for path in files:

    print()
    print("=" * 100)
    print(f"FILE: {path}")
    print("=" * 100)

    if not path.exists():

        print("FILE NOT FOUND")
        continue

    lines = path.read_text(
        encoding="utf-8"
    ).splitlines()

    keywords = [
        "def save_trade",
        "def get_trade",
        "def find_trade",
        "def exists",
        "trade_id",
        "mt5_ticket",
        "SELECT",
        "INSERT",
        "duplicate",
        "already",
    ]

    for number, line in enumerate(
        lines,
        start=1
    ):

        if any(
            keyword.lower() in line.lower()
            for keyword in keywords
        ):

            print(
                f"{number:04}: {line.strip()}"
            )

print()
print("=" * 100)
print("E.27.12.71 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

