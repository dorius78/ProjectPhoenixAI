from pathlib import Path

path = Path(
    "Execution/execution_engine.py"
)

lines = path.read_text(
    encoding="utf-8"
).splitlines()

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.59 EXECUTION OPEN RETURN AUDIT")
print("=" * 100)

start = None

for i, line in enumerate(lines):

    if line.strip().startswith("def execute("):

        start = i
        break

if start is None:

    raise RuntimeError(
        "STOP: def execute() non trovato"
    )

# Trova il prossimo metodo allo stesso livello
end = len(lines)

for i in range(
    start + 1,
    len(lines)
):

    if (
        lines[i].startswith("    def ")
        and i > start
    ):

        end = i
        break

print()
print("=" * 100)
print("METODO execute() COMPLETO")
print("=" * 100)

for i in range(
    start,
    end
):

    print(
        f"{i+1:04}: {lines[i]}"
    )

print()
print("=" * 100)
print("RICERCA RESULT MT5")
print("=" * 100)

keywords = [
    "self.mt5.execute",
    "result",
    "success",
    "executed",
    "dry_run",
    "order_ticket",
    "deal_ticket",
    "position_ticket",
    "retcode",
    "mt5",
]

for number in range(
    start,
    end
):

    line = lines[number]

    if any(
        keyword.lower() in line.lower()
        for keyword in keywords
    ):

        print(
            f"{number+1:04}: {line}"
        )

print()
print("=" * 100)
print("E.27.12.59 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

