from pathlib import Path

path = Path(
    "Core/phoenix_brain_logic.py"
)

text = path.read_text(
    encoding="utf-8-sig"
)

replacements = [
    (
        '        if analysis.get("trend_bullish"):\n',
        '        if analysis.get("trend_bullish"):\n'
    ),
    (
        '        elif analysis.get("trend_bearish"):\n',
        '        if analysis.get("trend_bearish"):\n'
    ),
    (
        '        if analysis.get("ema_alignment_bullish"):\n',
        '        if analysis.get("ema_alignment_bullish"):\n'
    ),
    (
        '        if analysis.get("macd_buy"):\n',
        '        if analysis.get("macd_buy"):\n'
    ),
    (
        '        if analysis.get("choch_bullish"):\n',
        '        if analysis.get("choch_bullish"):\n'
    ),
    (
        '        if analysis.get("fvg_bullish"):\n',
        '        if analysis.get("fvg_bullish"):\n'
    ),
    (
        '        if analysis.get("order_block_bullish"):\n',
        '        if analysis.get("order_block_bullish"):\n'
    ),
    (
        '        if analysis.get("liquidity_bullish"):\n',
        '        if analysis.get("liquidity_bullish"):\n'
    )
]

# Sostituzione mirata:
# gli elif bearish devono diventare if indipendenti.
targets = [
    '        elif analysis.get("trend_bearish"):\n',
    '        elif analysis.get("ema_alignment_bearish"):\n',
    '        elif analysis.get("macd_sell"):\n',
    '        elif analysis.get("choch_bearish"):\n',
    '        elif analysis.get("fvg_bearish"):\n',
    '        elif analysis.get("order_block_bearish"):\n',
    '        elif analysis.get("liquidity_bearish"):\n'
]

for target in targets:

    count = text.count(target)

    if count != 1:
        raise RuntimeError(
            f"STOP: occorrenza inattesa di {target.strip()}: {count}"
        )

    text = text.replace(
        target,
        target.replace(
            "elif",
            "if",
            1
        ),
        1
    )

path.write_text(
    text,
    encoding="utf-8"
)

print("=" * 100)
print("E.27.40B DECISION CORE PATCH APPLICATA")
print("=" * 100)
print("TREND CONTRADICTION: FIX")
print("EMA CONTRADICTION: FIX")
print("MACD CONTRADICTION: FIX")
print("CHoCH CONTRADICTION: FIX")
print("FVG CONTRADICTION: FIX")
print("ORDER BLOCK CONTRADICTION: FIX")
print("LIQUIDITY CONTRADICTION: FIX")
print()
print("PESI: INVARIATI")
print("CONFIDENCE FORMULA: INVARIATA")
print("SCORE FORMULA: INVARIATA")
print("OTHER LOGIC: INVARIATA")
print()
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

