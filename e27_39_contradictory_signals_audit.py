from Core.phoenix_brain_logic import PhoenixBrainLogic

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.39 CONTRADICTORY SIGNALS AUDIT")
print("=" * 100)

logic = PhoenixBrainLogic()


def test(name, analysis):

    result = logic.calculate(
        analysis,
        {
            "risk_level": "BASSO"
        }
    )

    print()
    print("=" * 100)
    print(name)
    print("=" * 100)

    print("INPUT:")
    for key, value in analysis.items():
        print(f"  {key:30} = {value}")

    print()
    print("OUTPUT:")
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
        "REASONS:",
        result["reasons"]
    )

    print(
        "WARNINGS:",
        result["warnings"]
    )


# ============================================================
# 1. TREND CONTRADICTORY
# ============================================================

test(
    "1. TREND BULLISH + BEARISH",
    {
        "trend_bullish": True,
        "trend_bearish": True
    }
)


# ============================================================
# 2. EMA CONTRADICTORY
# ============================================================

test(
    "2. EMA BULLISH + BEARISH",
    {
        "ema_alignment_bullish": True,
        "ema_alignment_bearish": True
    }
)


# ============================================================
# 3. MACD CONTRADICTORY
# ============================================================

test(
    "3. MACD BUY + SELL",
    {
        "macd_buy": True,
        "macd_sell": True
    }
)


# ============================================================
# 4. BOS CONTRADICTORY
# ============================================================

test(
    "4. BOS BULLISH + BEARISH",
    {
        "bos_bullish": True,
        "bos_bearish": True
    }
)


# ============================================================
# 5. CHOCH CONTRADICTORY
# ============================================================

test(
    "5. CHOCH BULLISH + BEARISH",
    {
        "choch_bullish": True,
        "choch_bearish": True
    }
)


# ============================================================
# 6. FVG CONTRADICTORY
# ============================================================

test(
    "6. FVG BULLISH + BEARISH",
    {
        "fvg_bullish": True,
        "fvg_bearish": True
    }
)


# ============================================================
# 7. ORDER BLOCK CONTRADICTORY
# ============================================================

test(
    "7. ORDER BLOCK BULLISH + BEARISH",
    {
        "order_block_bullish": True,
        "order_block_bearish": True
    }
)


# ============================================================
# 8. LIQUIDITY CONTRADICTORY
# ============================================================

test(
    "8. LIQUIDITY BULLISH + BEARISH",
    {
        "liquidity_bullish": True,
        "liquidity_bearish": True
    }
)


# ============================================================
# 9. PURE MULTI-FACTOR CONFLICT
# ============================================================

test(
    "9. MULTI FACTOR CONFLICT",
    {
        "trend_bullish": True,
        "trend_bearish": True,

        "ema_alignment_bullish": True,
        "ema_alignment_bearish": True,

        "macd_buy": True,
        "macd_sell": True,

        "bos_bullish": True,
        "bos_bearish": True,

        "order_block_bullish": True,
        "order_block_bearish": True
    }
)


# ============================================================
# 10. BULLISH DOMINANCE WITH ONE BEARISH FACTOR
# ============================================================

test(
    "10. BULLISH DOMINANCE",
    {
        "trend_bullish": True,
        "ema_alignment_bullish": True,
        "macd_buy": True,
        "adx_strong": True,
        "bos_bullish": True,
        "macd_sell": True
    }
)


# ============================================================
# 11. BEARISH DOMINANCE WITH ONE BULLISH FACTOR
# ============================================================

test(
    "11. BEARISH DOMINANCE",
    {
        "trend_bearish": True,
        "ema_alignment_bearish": True,
        "macd_sell": True,
        "adx_strong": True,
        "bos_bearish": True,
        "macd_buy": True
    }
)


# ============================================================
# 12. EMPTY MARKET
# ============================================================

test(
    "12. EMPTY MARKET",
    {}
)


print()
print("=" * 100)
print("E.27.39 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

