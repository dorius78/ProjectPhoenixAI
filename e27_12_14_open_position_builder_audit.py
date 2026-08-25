from pathlib import Path

path = Path("Core/live_trading_engine.py")
lines = path.read_text(encoding="utf-8").splitlines()

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.14 OPEN POSITION BUILDER AUDIT")
print("=" * 100)

start = None

for i, line in enumerate(lines):
    if line.strip().startswith("def _open_position_from_order("):
        start = i
        break

if start is None:
    raise RuntimeError(
        "STOP: metodo _open_position_from_order non trovato"
    )

print()
print("=" * 100)
print("METODO _open_position_from_order()")
print("=" * 100)

end = min(
    start + 110,
    len(lines)
)

for i in range(start, end):
    print(f"{i+1:04}: {lines[i]}")

print()
print("=" * 100)
print("RIFERIMENTI IMPORTANTI")
print("=" * 100)

keywords = [
    "execution",
    "mt5",
    "ticket",
    "magic",
    "position_controller",
    "portfolio",
    "success",
    "executed"
]

for i in range(start, end):

    line = lines[i]

    if any(
        keyword.lower() in line.lower()
        for keyword in keywords
    ):
        print(f"{i+1:04}: {line}")

print()
print("=" * 100)
print("E.27.12.14 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

