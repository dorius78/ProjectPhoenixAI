from pathlib import Path

path = Path(
    "Core/signal_manager.py"
)

text = path.read_text(
    encoding="utf-8-sig"
)

lines = text.splitlines()

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.46 STRONG SIGNAL GATE TARGET AUDIT")
print("=" * 100)

print()

for number, line in enumerate(lines, start=1):

    if (
        'elif signal == "STRONG BUY"' in line
        or 'elif signal == "STRONG SELL"' in line
        or 'if confidence < MIN_CONFIDENCE' in line
    ):

        start = max(
            0,
            number - 6
        )

        end = min(
            len(lines),
            number + 10
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
print("E.27.46 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

