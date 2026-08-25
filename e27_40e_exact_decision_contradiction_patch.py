from pathlib import Path

path = Path("Core/phoenix_brain_logic.py")

text = path.read_text(
    encoding="utf-8-sig"
)

# Backup ulteriore prima della modifica
backup = Path(
    "Core/phoenix_brain_logic.py.E27.40D.backup"
)

backup.write_text(
    text,
    encoding="utf-8"
)

# ============================================================
# PATCH SOLO DELLE 7 COPPIE DECISIONALI PRINCIPALI
# ============================================================

replacements = [

    (
        '''        if analysis.get("trend_bullish"):

            bullish_score += 20

        elif analysis.get("trend_bearish"):''',

        '''        if analysis.get("trend_bullish"):

            bullish_score += 20

        if analysis.get("trend_bearish"):'''
    ),

    (
        '''        if analysis.get("ema_alignment_bullish"):

            bullish_score += 10

        elif analysis.get("ema_alignment_bearish"):''',

        '''        if analysis.get("ema_alignment_bullish"):

            bullish_score += 10

        if analysis.get("ema_alignment_bearish"):'''
    ),

    (
        '''        if analysis.get("macd_buy"):

            bullish_score += 10

        elif analysis.get("macd_sell"):''',

        '''        if analysis.get("macd_buy"):

            bullish_score += 10

        if analysis.get("macd_sell"):'''
    ),

    (
        '''        if analysis.get("choch_bullish"):

            bullish_score += 10

        elif analysis.get("choch_bearish"):''',

        '''        if analysis.get("choch_bullish"):

            bullish_score += 10

        if analysis.get("choch_bearish"):'''
    ),

    (
        '''        if analysis.get("fvg_bullish"):

            bullish_score += 8

        elif analysis.get("fvg_bearish"):''',

        '''        if analysis.get("fvg_bullish"):

            bullish_score += 8

        if analysis.get("fvg_bearish"):'''
    ),

    (
        '''        if analysis.get("order_block_bullish"):

            bullish_score += 10

        elif analysis.get("order_block_bearish"):''',

        '''        if analysis.get("order_block_bullish"):

            bullish_score += 10

        if analysis.get("order_block_bearish"):'''
    ),

    (
        '''        if analysis.get("liquidity_bullish"):

            bullish_score += 8

        elif analysis.get("liquidity_bearish"):''',

        '''        if analysis.get("liquidity_bullish"):

            bullish_score += 8

        if analysis.get("liquidity_bearish"):'''
    ),
]

print("=" * 100)
print("E.27.40E EXACT DECISION CONTRADICTION PATCH")
print("=" * 100)

for number, (old, new) in enumerate(
    replacements,
    start=1
):

    count = text.count(old)

    print(
        f"PATCH {number}: occurrences = {count}"
    )

    if count != 1:

        raise RuntimeError(
            f"STOP PATCH {number}: "
            f"blocco non trovato in modo univoco."
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
print("7/7 DECISION PAIRS MODIFICATE")
print()
print("TREND: FIX")
print("EMA: FIX")
print("MACD: FIX")
print("CHoCH: FIX")
print("FVG: FIX")
print("ORDER BLOCK: FIX")
print("LIQUIDITY: FIX")
print()
print("ADX/Volume trend logic: NON TOCCATA")
print("PESI: INVARIATI")
print("SCORE: INVARIATO")
print("CONFIDENCE: INVARIATA")
print("RISK: INVARIATO")
print("MT5: INVARIATO")
print()
print("BACKUP:", backup)
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

