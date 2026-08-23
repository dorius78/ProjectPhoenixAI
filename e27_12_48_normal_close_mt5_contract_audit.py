from pathlib import Path

path = Path("Execution/execution_engine.py")
text = path.read_text(encoding="utf-8")

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.48 NORMAL CLOSE MT5 CONTRACT AUDIT")
print("=" * 100)

print()
print("RICERCA CONTRATTO CLOSE")
print("-" * 100)

lines = text.splitlines()

start = None

for i, line in enumerate(lines):

    if line.strip().startswith("def close("):

        start = i
        break

if start is None:
    raise RuntimeError(
        "STOP: def close() non trovato"
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
print("RICERCA MT5 RESULT")
print("=" * 100)

keywords = [
    "mt5",
    "result",
    "ticket",
    "order_ticket",
    "deal_ticket",
    "position_ticket",
    "retcode",
    "success",
    "executed"
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
print("E.27.12.48 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

