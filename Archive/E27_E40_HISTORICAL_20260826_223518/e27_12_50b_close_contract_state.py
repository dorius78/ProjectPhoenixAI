from pathlib import Path

path = Path(
    "MT5_Bridge/mt5_execution_recovered.py"
)

lines = path.read_text(
    encoding="utf-8"
).splitlines()

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.50B CLOSE CONTRACT STATE")
print("=" * 100)

start = None

for i, line in enumerate(lines):

    if line.strip().startswith("def close_position("):

        start = i
        break

if start is None:
    raise RuntimeError(
        "STOP: close_position() non trovato"
    )

end = min(
    start + 230,
    len(lines)
)

for i in range(start, end):

    print(
        f"{i+1:04}: {lines[i]}"
    )

print()
print("=" * 100)
print("RICERCA TICKET")
print("=" * 100)

keywords = [
    '"success"',
    '"order_ticket"',
    '"deal_ticket"',
    '"position_ticket"',
    '"retcode"',
    '"result"',
    'result.order',
    'result.deal',
    'result.position'
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
print("E.27.12.50B COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

