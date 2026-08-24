from Core.phoenix_brain import PhoenixBrain

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.21 DECISION SCORE STRESS AUDIT")
print("=" * 100)

brain = PhoenixBrain()

logic = brain.logic

# ============================================================
# SCENARIO BUILDER
# ============================================================

def scenario(
    name,
    analysis,
    risk=None
):

    if risk is None:

        risk = {
            "risk_level": "BASSO"
        }

    result = logic.calculate(
        analysis,
        risk
    )

    print()
    print("=" * 100)
    print(name)
    print("=" * 100)

    print(
        "BULLISH SCORE:",
        result["bullish_score"]
    )

    print(
        "BEARISH SCORE:",
        result["bearish_score"]
    )

    print(
        "NET SCORE:",
        result["score"]
    )

    print(
        "CONFIDENCE:",
        result["confidence"]
    )

    print(
        "DIRECTION:",
        result["dominant_direction"]
    )

    print(
        "CONFLICT:",
        result["conflict"]
    )

    print(
        "BULLISH REASONS:",
        result["bullish_reasons"]
    )

    print(
        "BEARISH REASONS:",
        result["bearish_reasons"]
    )

    return result


# ============================================================
# 1. NEUTRAL
# ============================================================

scenario(
    "1. COMPLETELY NEUTRAL",
    {}
)


# ============================================================
# 2. PURE BULLISH TREND
# ============================================================

scenario(
    "2. PURE BULLISH TREND",
    {
        "trend_bullish": True
    }
)


# ============================================================
# 3. ALL BULLISH
# ============================================================

scenario(
    "3. ALL BULLISH FACTORS",
    {
        "trend_bullish": True,
        "ema_alignment_bullish": True,
        "macd_buy": True,
        "rsi": 20,
        "adx_strong": True,
        "volume_high": True,
        "bos_bullish": True,
        "choch_bullish": True,
        "fvg_bullish": True,
        "order_block_bullish": True,
        "liquidity_bullish": True
    }
)


# ============================================================
# 4. ALL BEARISH
# ============================================================

scenario(
    "4. ALL BEARISH FACTORS",
    {
        "trend_bearish": True,
        "ema_alignment_bearish": True,
        "macd_sell": True,
        "rsi": 80,
        "adx_strong": True,
        "volume_high": True,
        "bos_bearish": True,
        "choch_bearish": True,
        "fvg_bearish": True,
        "order_block_bearish": True,
        "liquidity_bearish": True
    }
)


# ============================================================
# 5. BULLISH / BEARISH CONFLICT
# ============================================================

scenario(
    "5. STRONG CONFLICT",
    {
        "trend_bullish": True,
        "trend_bearish": False,
        "ema_alignment_bullish": True,
        "macd_sell": True,
        "rsi": 80,
        "bos_bullish": True,
        "order_block_bearish": True
    }
)


# ============================================================
# 6. HIGH RISK
# ============================================================

scenario(
    "6. BULLISH + HIGH RISK",
    {
        "trend_bullish": True,
        "ema_alignment_bullish": True,
        "macd_buy": True,
        "bos_bullish": True
    },
    {
        "risk_level": "ALTO"
    }
)


print()
print("=" * 100)
print("E.27.21 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

