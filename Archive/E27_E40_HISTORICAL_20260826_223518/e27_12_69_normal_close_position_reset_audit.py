from pathlib import Path

path = Path(
    "Core/live_trading_engine.py"
)

lines = path.read_text(
    encoding="utf-8"
).splitlines()

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.69 NORMAL CLOSE POSITION RESET AUDIT")
print("=" * 100)

start = None

for i, line in enumerate(lines):

    if line.strip().startswith(
        "def _process_closed_position("
    ):
        start = i
        break

if start is None:
    raise RuntimeError(
        "STOP: _process_closed_position() non trovato"
    )

print()
print("METODO _process_closed_position()")
print("-" * 100)

for i in range(
    start,
    min(start + 260, len(lines))
):

    print(
        f"{i+1:04}: {lines[i]}"
    )

print()
print("=" * 100)
print("RICERCA RESET POSITION")
print("=" * 100)

keywords = [
    "position_controller",
    "reset(",
    "remove(",
    "set_position",
    "position = None",
]

for number, line in enumerate(
    lines,
    start=1
):

    if any(
        keyword.lower() in line.lower()
        for keyword in keywords
    ):

        print(
            f"{number:04}: {line.strip()}"
        )

print()
print("=" * 100)
print("E.27.12.69 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

