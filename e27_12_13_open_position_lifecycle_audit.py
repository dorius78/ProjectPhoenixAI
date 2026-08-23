from pathlib import Path

path = Path("Core/live_trading_engine.py")
lines = path.read_text(encoding="utf-8").splitlines()

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.13 OPEN POSITION LIFECYCLE AUDIT")
print("=" * 100)

print()
print("1. BLOCCO ANALISI -> SIGNAL -> EXECUTION")
print("-" * 100)

for i in range(1015, min(1110, len(lines))):
    print(f"{i+1:04}: {lines[i]}")

print()
print("=" * 100)
print("2. RICERCA POSITION CONTROLLER / PORTFOLIO")
print("=" * 100)

keywords = [
    "execution.execute",
    "position_controller.open_position",
    "portfolio.add",
    "mt5_ticket",
    "mt5_symbol",
    "magic",
    "success",
    "executed"
]

for i, line in enumerate(lines):
    if any(k.lower() in line.lower() for k in keywords):
        print(f"{i+1:04}: {line}")

print()
print("=" * 100)
print("3. AUDIT")
print("=" * 100)

print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

