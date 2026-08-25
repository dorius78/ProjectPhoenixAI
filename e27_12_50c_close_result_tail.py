from pathlib import Path

path = Path(
    "MT5_Bridge/mt5_execution_recovered.py"
)

lines = path.read_text(
    encoding="utf-8"
).splitlines()

start = None

for i, line in enumerate(lines):

    if line.strip().startswith("def close_position("):
        start = i
        break

if start is None:
    raise RuntimeError(
        "STOP: close_position() non trovato"
    )

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.50C CLOSE RESULT")
print("=" * 100)

print()

# Stampa dalla parte REAL CLOSE fino alla fine del metodo
for i in range(
    start + 215,
    min(start + 285, len(lines))
):

    print(
        f"{i+1:04}: {lines[i]}"
    )

print()
print("=" * 100)
print("E.27.12.50C COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

