from pathlib import Path

path = Path("Core/live_trading_engine.py")
lines = path.read_text(encoding="utf-8").splitlines()

print("=" * 70)
print("PHOENIX AI - C.1.11 - CLOSED POSITION IDEMPOTENCY")
print("=" * 70)

for start, end in [
    (410, 560),
    (650, 735),
]:
    print()
    print("=" * 70)
    print(f"LIVE TRADING ENGINE - LINES {start}-{end}")
    print("=" * 70)

    for number in range(start, min(end, len(lines)) + 1):
        print(f"{number:5}: {lines[number - 1]}")

print()
print("=" * 70)
print("C.1.11 ANALISI COMPLETATA")
print("NESSUNA MODIFICA APPLICATA")
print("=" * 70)
