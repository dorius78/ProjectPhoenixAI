from pathlib import Path

path = Path(
    "Database/database_manager.py"
)

lines = path.read_text(
    encoding="utf-8"
).splitlines()

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.73 DATABASE TRADE SCHEMA AUDIT")
print("=" * 100)

for number, line in enumerate(
    lines,
    start=1
):

    if (
        30 <= number <= 125
        or
        145 <= number <= 175
    ):

        print(
            f"{number:04}: {line}"
        )

print()
print("=" * 100)
print("E.27.12.73 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

