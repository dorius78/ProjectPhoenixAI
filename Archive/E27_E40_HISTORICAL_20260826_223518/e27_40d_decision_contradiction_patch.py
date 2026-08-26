from pathlib import Path

path = Path(
    "Core/phoenix_brain_logic.py"
)

text = path.read_text(
    encoding="utf-8-sig"
)

targets = [
    '        elif analysis.get("trend_bearish"):\n',
    '        elif analysis.get("ema_alignment_bearish"):\n',
    '        elif analysis.get("macd_sell"):\n',
    '        elif analysis.get("choch_bearish"):\n',
    '        elif analysis.get("fvg_bearish"):\n',
    '        elif analysis.get("order_block_bearish"):\n',
    '        elif analysis.get("liquidity_bearish"):\n',
]

print("=" * 100)
print("E.27.40D DECISION CORE CONTRADICTION PATCH")
print("=" * 100)

for target in targets:

    count = text.count(target)

    print(
        f"{target.strip():65} -> {count}"
    )

    if count != 1:
        raise RuntimeError(
            "STOP: target non univoco: "
            + target.strip()
        )

print()
print("TUTTI I 7 TARGET SONO UNIVOCI.")
print("APPLICAZIONE PATCH...")

for target in targets:

    replacement = target.replace(
        "elif",
        "if",
        1
    )

    text = text.replace(
        target,
        replacement,
        1
    )

path.write_text(
    text,
    encoding="utf-8"
)

print()
print("PATCH APPLICATA: OK")
print()
print("MODIFICHE:")
print("  trend contradiction       FIX")
print("  EMA contradiction         FIX")
print("  MACD contradiction        FIX")
print("  CHoCH contradiction       FIX")
print("  FVG contradiction         FIX")
print("  Order Block contradiction FIX")
print("  Liquidity contradiction   FIX")
print()
print("PESI: INVARIATI")
print("SCORE FORMULA: INVARIATA")
print("CONFIDENCE: INVARIATA")
print("RISK AI: INVARIATO")
print("MT5: INVARIATO")
print()
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

