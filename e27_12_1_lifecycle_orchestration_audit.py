from pathlib import Path

files = [
    "Core/core_system.py",
    "Core/live_trading_engine.py",
]

patterns = [
    "position_controller",
    "position_monitor",
    "exit_manager",
    "_open_position_from_order",
    "close_position",
    "evaluate(",
    "monitor.update",
    "execution.close",
    "execution.execute",
    "get_phoenix_positions",
    "get_open_positions",
]

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.1 LIFECYCLE ORCHESTRATION AUDIT")
print("=" * 100)

for filename in files:

    path = Path(filename)

    print()
    print("=" * 100)
    print(filename)
    print("=" * 100)

    lines = path.read_text(
        encoding="utf-8"
    ).splitlines()

    for i, line in enumerate(lines, 1):

        if any(
            pattern in line
            for pattern in patterns
        ):

            start = max(1, i - 8)
            end = min(len(lines), i + 15)

            print()
            print("-" * 100)
            print(f"RIFERIMENTO: {filename}:{i}")
            print("-" * 100)

            for n in range(start, end + 1):
                print(
                    f"{n:04}: {lines[n-1]}"
                )

print()
print("=" * 100)
print("E.27.12.1 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("=" * 100)
