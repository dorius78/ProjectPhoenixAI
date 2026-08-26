from pathlib import Path

path = Path("Execution/execution_engine.py")
lines = path.read_text(encoding="utf-8").splitlines()

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.18 MT5 RESULT FIELD AUDIT")
print("=" * 100)

print()
print("MT5ExecutionEngine.execute()")
print("-" * 100)

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
    start + 180,
    len(lines)
)

for i in range(start, end):

    print(
        f"{i+1:04}: {lines[i]}"
    )

print()
print("=" * 100)
print("MT5 RESULT FIELD ACCESS")
print("=" * 100)

keywords = [
    "result.",
    "result[",
    "retcode",
    "order",
    "deal",
    "position",
    "ticket"
]

for i in range(start, end):

    line = lines[i]

    if any(
        keyword.lower() in line.lower()
        for keyword in keywords
    ):

        print(
            f"{i+1:04}: {line}"
        )

print()
print("=" * 100)
print("E.27.12.18 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

