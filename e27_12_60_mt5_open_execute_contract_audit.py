from pathlib import Path

path = Path(
    "MT5_Bridge/mt5_execution_recovered.py"
)

lines = path.read_text(
    encoding="utf-8"
).splitlines()

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.60 MT5 OPEN EXECUTE CONTRACT AUDIT")
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
print("MT5_Bridge.execute() COMPLETO")
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
print("CAMPI CONTRATTO")
print("=" * 100)

keywords = [
    "executed",
    "success",
    "dry_run",
    "message",
    "order_ticket",
    "deal_ticket",
    "position_ticket",
    "mt5_ticket",
    "retcode",
    "result",
]

for keyword in keywords:

    print()
    print(f"--- {keyword} ---")

    found = False

    for i in range(
        start,
        end
    ):

        if keyword.lower() in lines[i].lower():

            print(
                f"{i+1:04}: {lines[i]}"
            )

            found = True

    if not found:

        print("NOT FOUND")

print()
print("=" * 100)
print("E.27.12.60 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

