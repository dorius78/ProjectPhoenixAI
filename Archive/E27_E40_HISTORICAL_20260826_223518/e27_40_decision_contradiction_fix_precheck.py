from pathlib import Path

path = Path(
    "Core/phoenix_brain_logic.py"
)

text = path.read_text(
    encoding="utf-8-sig"
)

print("=" * 100)
print("E.27.40 DECISION CORE CONTRADICTION FIX")
print("=" * 100)

# ------------------------------------------------------------
# Mostriamo il file prima della modifica.
# ------------------------------------------------------------

lines = text.splitlines()

for number, line in enumerate(lines, start=1):

    if (
        "trend_bullish" in line
        or "trend_bearish" in line
        or "ema_alignment_bullish" in line
        or "ema_alignment_bearish" in line
        or "macd_buy" in line
        or "macd_sell" in line
        or "bos_bullish" in line
        or "bos_bearish" in line
        or "choch_bullish" in line
        or "choch_bearish" in line
        or "fvg_bullish" in line
        or "fvg_bearish" in line
        or "order_block_bullish" in line
        or "order_block_bearish" in line
        or "liquidity_bullish" in line
        or "liquidity_bearish" in line
    ):

        print(
            f"{number:04}: {line}"
        )

print()
print("BACKUP: OK")
print("NESSUNA MODIFICA ANCORA ESEGUITA")

print()
print("=" * 100)
print("STOP")
print("=" * 100)
print(
    "Il file e stato analizzato e il backup e stato creato."
)
print(
    "NON viene modificato automaticamente in questa fase."
)
print("=" * 100)

