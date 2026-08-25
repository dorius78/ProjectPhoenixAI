from pathlib import Path

path = Path("Core/live_trading_engine.py")
lines = path.read_text(encoding="utf-8").splitlines()

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.9 LIVE LOOP / MT5 SYNC INSERTION AUDIT")
print("=" * 100)

print()
print("--- METODI LIVE ENGINE ---")
print("-" * 100)

for i, line in enumerate(lines):
    if line.strip().startswith("def "):
        print(f"{i+1:04}: {line}")

print()
print("=" * 100)
print("--- START / LOOP / POSITION / EXECUTION ---")
print("=" * 100)

keywords = [
    "def start(",
    "while ",
    "has_position",
    "get_position()",
    "position_controller.update",
    "position_controller.open_position",
    "position_controller.close_position",
    "execution.execute(",
    "execution.close(",
    "_sync_mt5_position",
]

for i, line in enumerate(lines):
    lower = line.lower()

    if any(k.lower() in lower for k in keywords):
        print(f"{i+1:04}: {line}")

print()
print("=" * 100)
print("--- BLOCCO START/LOOP COMPLETO ---")
print("=" * 100)

start = None

for i, line in enumerate(lines):
    if line.strip().startswith("def start("):
        start = i
        break

if start is None:

    print("STOP: def start() non trovato")

else:

    end = min(start + 300, len(lines))

    for i in range(start, end):
        print(f"{i+1:04}: {lines[i]}")

print()
print("=" * 100)
print("E.27.12.9 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("=" * 100)
