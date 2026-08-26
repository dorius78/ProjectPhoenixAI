from pathlib import Path

path = Path(
    "Core/phoenix_brain_logic.py"
)

lines = path.read_text(
    encoding="utf-8-sig"
).splitlines()

print("=" * 100)
print("E.27.40C DECISION CORE EXACT PATCH TARGET AUDIT")
print("=" * 100)

targets = [
    "trend_bullish",
    "trend_bearish",
    "ema_alignment_bullish",
    "ema_alignment_bearish",
    "macd_buy",
    "macd_sell",
    "choch_bullish",
    "choch_bearish",
    "fvg_bullish",
    "fvg_bearish",
    "order_block_bullish",
    "order_block_bearish",
    "liquidity_bullish",
    "liquidity_bearish",
]

for target in targets:

    print()
    print("-" * 100)
    print(target)
    print("-" * 100)

    for number, line in enumerate(lines, start=1):

        if target in line:

            start = max(
                0,
                number - 3
            )

            end = min(
                len(lines),
                number + 2
            )

            for i in range(
                start,
                end
            ):

                print(
                    f"{i+1:04}: {lines[i]}"
                )

            print()

print("=" * 100)
print("E.27.40C AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

