from pathlib import Path

path = Path(
    "Core/phoenix_brain_logic.py"
)

text = path.read_text(
    encoding="utf-8-sig"
)

patches = [

    (
        '        elif analysis.get("trend_bearish"):\n\n            bearish_score += 20',
        '        if analysis.get("trend_bearish"):\n\n            bearish_score += 20'
    ),

    (
        '        elif analysis.get("ema_alignment_bearish"):\n\n            bearish_score += 10',
        '        if analysis.get("ema_alignment_bearish"):\n\n            bearish_score += 10'
    ),

    (
        '        elif analysis.get("macd_sell"):\n\n            bearish_score += 10',
        '        if analysis.get("macd_sell"):\n\n            bearish_score += 10'
    ),

    (
        '        elif analysis.get("choch_bearish"):\n\n            bearish_score += 10',
        '        if analysis.get("choch_bearish"):\n\n            bearish_score += 10'
    ),

    (
        '        elif analysis.get("fvg_bearish"):\n\n            bearish_score += 8',
        '        if analysis.get("fvg_bearish"):\n\n            bearish_score += 8'
    ),

    (
        '        elif analysis.get("order_block_bearish"):\n\n            bearish_score += 10',
        '        if analysis.get("order_block_bearish"):\n\n            bearish_score += 10'
    ),

    (
        '        elif analysis.get("liquidity_bearish"):\n\n            bearish_score += 8',
        '        if analysis.get("liquidity_bearish"):\n\n            bearish_score += 8'
    ),
]

print("=" * 100)
print("E.27.40G EXACT DECISION CORE PATCH")
print("=" * 100)

for number, (old, new) in enumerate(
    patches,
    start=1
):

    count = text.count(old)

    print(
        f"PATCH {number}: occurrences = {count}"
    )

    if count != 1:
        raise RuntimeError(
            f"STOP PATCH {number}: "
            "blocco non trovato in modo univoco."
        )

    text = text.replace(
        old,
        new,
        1
    )

path.write_text(
    text,
    encoding="utf-8"
)

print()
print("PATCH APPLICATA: OK")
print("7/7 CONTRADICTION PAIRS CORRETTE")
print()
print("TREND: FIX")
print("EMA: FIX")
print("MACD: FIX")
print("CHoCH: FIX")
print("FVG: FIX")
print("ORDER BLOCK: FIX")
print("LIQUIDITY: FIX")
print()
print("BOS: GIA CORRETTO")
print("ADX: NON TOCCATO")
print("VOLUME: NON TOCCATO")
print("PESI: INVARIATI")
print("SCORE: INVARIATO")
print("CONFIDENCE: INVARIATA")
print("RISK: INVARIATO")
print("MT5: INVARIATO")
print()
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

