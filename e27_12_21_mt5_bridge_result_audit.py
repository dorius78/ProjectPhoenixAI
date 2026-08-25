from pathlib import Path

path = Path("MT5_Bridge/mt5_execution_recovered.py")

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.21 MT5 BRIDGE RESULT CONTRACT AUDIT")
print("=" * 100)

if not path.exists():
    raise RuntimeError(
        "STOP: MT5_Bridge/mt5_execution_recovered.py non trovato"
    )

lines = path.read_text(
    encoding="utf-8"
).splitlines()

print()
print("=" * 100)
print("METODI EXECUTE / CLOSE")
print("=" * 100)

for i, line in enumerate(lines):
    if (
        line.strip().startswith("def execute(")
        or line.strip().startswith("def close_position(")
        or line.strip().startswith("def get_phoenix_positions(")
    ):
        print(f"{i+1:04}: {line}")

print()
print("=" * 100)
print("RICERCA ORDER_SEND / RESULT / TICKET / DEAL / POSITION")
print("=" * 100)

keywords = [
    "order_send",
    "result.",
    "retcode",
    "result.order",
    "result.deal",
    "result.position",
    "ticket",
    "position_id",
    "deal",
    "magic",
    "get_phoenix_positions",
]

for i, line in enumerate(lines):

    if any(
        keyword.lower() in line.lower()
        for keyword in keywords
    ):
        print(f"{i+1:04}: {line}")

print()
print("=" * 100)
print("BLOCCO EXECUTE() COMPLETO")
print("=" * 100)

start = None

for i, line in enumerate(lines):
    if line.strip().startswith("def execute("):
        start = i
        break

if start is None:
    raise RuntimeError(
        "STOP: execute() non trovato"
    )

end = min(
    start + 220,
    len(lines)
)

for i in range(start, end):
    print(f"{i+1:04}: {lines[i]}")

print()
print("=" * 100)
print("E.27.12.21 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

