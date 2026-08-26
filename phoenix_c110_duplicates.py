from pathlib import Path

print("=" * 70)
print("PHOENIX AI - C.1.10 - DUPLICATE SAVE PATH ANALYSIS")
print("=" * 70)

files = [
    "Core/core_system.py",
    "Core/live_trading_engine.py",
    "Database/database_manager.py",
]

patterns = [
    "save_trade(",
    "add_trade(",
    "_process_closed_position(",
    "_build_closed_trade(",
    "close_position(",
]

for file_name in files:

    path = Path(file_name)

    print()
    print("=" * 70)
    print(file_name)
    print("=" * 70)

    if not path.exists():
        print("FILE NON TROVATO")
        continue

    lines = path.read_text(
        encoding="utf-8"
    ).splitlines()

    for number, line in enumerate(lines, start=1):

        for pattern in patterns:

            if pattern in line:

                print()
                print(
                    f"--- MATCH: {pattern} "
                    f"alla riga {number} ---"
                )

                start = max(1, number - 8)
                end = min(len(lines), number + 12)

                for n in range(start, end + 1):
                    print(
                        f"{n:5}: {lines[n - 1]}"
                    )

                break

print()
print("=" * 70)
print("C.1.10 ANALISI COMPLETATA")
print("NESSUNA MODIFICA APPLICATA")
print("=" * 70)
