from pathlib import Path

path = Path("Execution/execution_engine.py")
lines = path.read_text(encoding="utf-8").splitlines()

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.16 EXECUTION RETURN CONTRACT")
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

end = min(start + 260, len(lines))

print()
print("=" * 100)
print("BLOCCO COMPLETO EXECUTE()")
print("=" * 100)

for i in range(start, end):
    print(f"{i+1:04}: {lines[i]}")

print()
print("=" * 100)
print("RICERCA RETURN")
print("=" * 100)

for i in range(start, end):
    if lines[i].strip().startswith("return"):
        print(f"{i+1:04}: {lines[i]}")

print()
print("=" * 100)
print("RICERCA CAMPI MT5")
print("=" * 100)

keywords = [
    "result",
    "mt5",
    "ticket",
    "order",
    "deal",
    "position",
    "retcode",
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
print("E.27.12.16 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

