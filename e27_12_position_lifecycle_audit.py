from pathlib import Path

files = [
    "Core/position_controller.py",
    "Core/position_monitor.py",
    "Core/exit_manager.py",
]

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12 POSITION LIFECYCLE STRUCTURE AUDIT")
print("=" * 100)

for filename in files:

    path = Path(filename)

    print()
    print("=" * 100)
    print(filename)
    print("=" * 100)

    if not path.exists():
        print("FILE NON TROVATO")
        continue

    lines = path.read_text(
        encoding="utf-8"
    ).splitlines()

    print("LINES:", len(lines))
    print()

    for i, line in enumerate(lines, 1):
        print(f"{i:04}: {line}")

print()
print("=" * 100)
print("E.27.12 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("=" * 100)
