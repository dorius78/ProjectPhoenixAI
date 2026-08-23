from pathlib import Path

path = Path("Core/live_trading_engine.py")
lines = path.read_text(encoding="utf-8").splitlines()

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.12 LIVE LOOP FLOW AUDIT")
print("=" * 100)

print()
print("1. BLOCCO START()")
print("-" * 100)

start = None

for i, line in enumerate(lines):
    if line.strip().startswith("def start("):
        start = i
        break

if start is None:
    raise RuntimeError("STOP: start() non trovato")

for i in range(start, min(start + 180, len(lines))):
    print(f"{i+1:04}: {lines[i]}")

print()
print("=" * 100)
print("2. CHIAMATE CRITICHE")
print("=" * 100)

keywords = [
    "_sync_mt5_position",
    "has_position",
    "get_position()",
    "position_controller.update",
    "execution.execute",
    "execution.close",
    "analysis",
    "signal",
    "guard"
]

for i, line in enumerate(lines):
    if any(k.lower() in line.lower() for k in keywords):
        print(f"{i+1:04}: {line}")

print()
print("=" * 100)
print("3. RISULTATO AUDIT")
print("=" * 100)

sync_lines = [
    i + 1
    for i, line in enumerate(lines)
    if "_sync_mt5_position()" in line
]

print("SYNC CALLS:", sync_lines)

assert len(sync_lines) == 1

print()
print("SYNC PRESENTE NEL LIVE LOOP: OK")
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("=" * 100)

