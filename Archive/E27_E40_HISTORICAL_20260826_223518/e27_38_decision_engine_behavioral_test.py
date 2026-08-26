from Core.phoenix_brain_logic import PhoenixBrainLogic

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.38 DECISION ENGINE BEHAVIORAL TEST")
print("=" * 100)

logic = PhoenixBrainLogic()


def run(name, analysis, risk=None):

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
        "REASONS:",
        result["reasons"]
    )

    print(
        "WARNINGS:",
        result["warnings"]
    )


# ============================================================
# 1. TREND FORTE RIALZISTA
# ============================================================

run(
    "1. STRONG BULL TREND",
    {
        "trend_bullish": True,
        "ema_alignment_bullish": True,
        "macd_buy": True,
        "adx_strong": True,
        "volume_high": True,
        "bos_bullish": True,
        "choch_bullish": True
    }
)


# ============================================================
# 2. TREND FORTE RIBASSISTA
# ============================================================

run(
    "2. STRONG BEAR TREND",
    {
        "trend_bearish": True,
        "ema_alignment_bearish": True,
        "macd_sell": True,
        "adx_strong": True,
        "volume_high": True,
        "bos_bearish": True,
        "choch_bearish": True
    }
)


# ============================================================
# 3. RSI ESTREMO IN TREND RIALZISTA
# ============================================================

run(
    "3. BULL TREND + RSI OVERBOUGHT",
    {
        "trend_bullish": True,
        "ema_alignment_bullish": True,
        "macd_buy": True,
        "adx_strong": True,
        "volume_high": True,
        "rsi": 80
    }
)


# ============================================================
# 4. BULL TREND + RSI OVERSOLD
# ============================================================

run(
    "4. BULL TREND + RSI OVERSOLD",
    {
        "trend_bullish": True,
        "ema_alignment_bullish": True,
        "macd_buy": True,
        "adx_strong": True,
        "volume_high": True,
        "rsi": 20
    }
)


# ============================================================
# 5. BEAR TREND + RSI OVERSOLD
# ============================================================

run(
    "5. BEAR TREND + RSI OVERSOLD",
    {
        "trend_bearish": True,
        "ema_alignment_bearish": True,
        "macd_sell": True,
        "adx_strong": True,
        "volume_high": True,
        "rsi": 20
    }
)


# ============================================================
# 6. PERFETTO EQUILIBRIO
# ============================================================

run(
    "6. PERFECT BALANCE",
    {
        "trend_bullish": True,
        "trend_bearish": True,
        "ema_alignment_bullish": True,
        "ema_alignment_bearish": True,
        "macd_buy": True,
        "macd_sell": True
    }
)


# ============================================================
# 7. CONFLITTO REALE
# ============================================================

run(
    "7. REAL MARKET CONFLICT",
    {
        "trend_bullish": True,
        "ema_alignment_bullish": True,
        "macd_sell": True,
        "rsi": 80,
        "bos_bullish": True,
        "order_block_bearish": True,
        "liquidity_bearish": True
    }
)


# ============================================================
# 8. FORTE SEGNALE + RISCHIO ALTO
# ============================================================

run(
    "8. STRONG SIGNAL + HIGH RISK",
    {
        "trend_bullish": True,
        "ema_alignment_bullish": True,
        "macd_buy": True,
        "adx_strong": True,
        "volume_high": True,
        "bos_bullish": True,
        "choch_bullish": True,
        "fvg_bullish": True,
        "order_block_bullish": True,
        "liquidity_bullish": True
    },
    {
        "risk_level": "ALTO"
    }
)


print()
print("=" * 100)
print("E.27.38 TEST COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

