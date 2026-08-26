from pathlib import Path

path = Path("Execution/execution_engine.py")
lines = path.read_text(encoding="utf-8").splitlines()

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.15 EXECUTION RESULT CONTRACT AUDIT")
print("=" * 100)

start = None

for i, line in enumerate(lines):
    if line.strip().startswith("def execute("):
        start = i
        break

if start is None:
    raise RuntimeError(
        "STOP: metodo execute() non trovato"
    )

print()
print("=" * 100)
print("METODO EXECUTE()")
print("=" * 100)

end = min(start + 190, len(lines))

for i in range(start, end):
    print(f"{i+1:04}: {lines[i]}")

print()
print("=" * 100)
print("RIFERIMENTI MT5 / TICKET / RESULT")
print("=" * 100)

keywords = [
    "mt5",
    "ticket",
    "order",
    "result",
    "retcode",
    "deal",
    "position",
    "executed",
    "dry_run"
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
print("E.27.12.15 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

