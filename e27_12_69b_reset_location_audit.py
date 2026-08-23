from pathlib import Path

path = Path(
    "Core/live_trading_engine.py"
)

lines = path.read_text(
    encoding="utf-8"
).splitlines()

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.69B RESET LOCATION AUDIT")
print("=" * 100)

for number, line in enumerate(
    lines,
    start=1
):

    if "position_controller.reset()" in line:

        print()
        print(
            f"RESET TROVATO ALLA RIGA {number}"
        )

        start = max(
            0,
            number - 12
        )

        end = min(
            len(lines),
            number + 12
        )

        print("-" * 100)

        for i in range(
            start,
            end
        ):

            print(
                f"{i+1:04}: {lines[i]}"
            )

print()
print("=" * 100)
print("E.27.12.69B COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

