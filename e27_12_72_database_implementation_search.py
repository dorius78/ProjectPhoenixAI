from pathlib import Path

root = Path(".")

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.72 DATABASE IMPLEMENTATION SEARCH")
print("=" * 100)

keywords = [
    "class Database",
    "class TradeDatabase",
    "def save_trade",
    "save_trade(",
    "sqlite3",
    "sqlite",
    "trades",
]

for keyword in keywords:

    print()
    print("=" * 100)
    print(f"SEARCH: {keyword}")
    print("=" * 100)

    found = False

    for path in root.rglob("*.py"):

        # Escludiamo cache e ambienti virtuali
        if (
            "__pycache__" in path.parts
            or ".venv" in path.parts
            or "venv" in path.parts
        ):
            continue

        try:
            lines = path.read_text(
                encoding="utf-8"
            ).splitlines()

        except Exception:
            continue

        for number, line in enumerate(
            lines,
            start=1
        ):

            if keyword.lower() in line.lower():

                print(
                    f"{path}:{number}: "
                    f"{line.strip()}"
                )

                found = True

    if not found:
        print("NOT FOUND")

print()
print("=" * 100)
print("E.27.12.72 SEARCH COMPLETATA")
print("=" * 100)
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

