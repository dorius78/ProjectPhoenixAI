from pathlib import Path

path = Path("MT5_Bridge/mt5_execution_recovered.py")
lines = path.read_text(encoding="utf-8").splitlines()

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.22 MT5 POSITION/TICKET CONTRACT AUDIT")
print("=" * 100)

# ============================================================
# 1. GET PHOENIX POSITIONS
# ============================================================

print()
print("=" * 100)
print("1. get_phoenix_positions()")
print("=" * 100)

start = None

for i, line in enumerate(lines):
    if line.strip().startswith("def get_phoenix_positions("):
        start = i
        break

if start is None:
    raise RuntimeError("STOP: get_phoenix_positions() non trovato")

end = min(start + 100, len(lines))

for i in range(start, end):
    print(f"{i+1:04}: {lines[i]}")

# ============================================================
# 2. TICKET / POSITION ID
# ============================================================

print()
print("=" * 100)
print("2. TICKET / POSITION ID / DEAL")
print("=" * 100)

keywords = [
    "position_id",
    "ticket",
    "deal",
    "result.order",
    "result.deal",
    "result.position",
]

for i, line in enumerate(lines):
    if any(
        keyword.lower() in line.lower()
        for keyword in keywords
    ):
        print(f"{i+1:04}: {line}")

# ============================================================
# 3. CLOSE POSITION
# ============================================================

print()
print("=" * 100)
print("3. close_position()")
print("=" * 100)

start = None

for i, line in enumerate(lines):
    if line.strip().startswith("def close_position("):
        start = i
        break

if start is None:
    raise RuntimeError("STOP: close_position() non trovato")

end = min(start + 310, len(lines))

for i in range(start, end):
    print(f"{i+1:04}: {lines[i]}")

print()
print("=" * 100)
print("E.27.12.22 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

