from Core.signal_manager import SignalManager

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.44 SIGNAL THRESHOLD BEHAVIORAL TEST")
print("=" * 100)

manager = SignalManager()

def test(name, decision):

    result = manager.validate(decision)

    print()
    print("=" * 100)
    print(name)
    print("=" * 100)

    print("INPUT:")
    print("  action              =", decision.get("action"))
    print("  confidence          =", decision.get("confidence"))
    print("  dominant_direction  =", decision.get("dominant_direction"))
    print("  conflict            =", decision.get("conflict"))

    print()
    print("OUTPUT:")

    for key, value in result.items():

        print(
            f"  {key:22} = {value}"
        )


# ------------------------------------------------------------
# BUY - CONFIDENCE 49
# ------------------------------------------------------------

test(
    "1. BUY CONFIDENCE 49",
    {
        "action": "BUY",
        "confidence": 49,
        "score": 75,
        "dominant_direction": "BULLISH",
        "conflict": False
    }
)


# ------------------------------------------------------------
# BUY - CONFIDENCE 50
# ------------------------------------------------------------

test(
    "2. BUY CONFIDENCE 50",
    {
        "action": "BUY",
        "confidence": 50,
        "score": 75,
        "dominant_direction": "BULLISH",
        "conflict": False
    }
)


# ------------------------------------------------------------
# BUY - CONFIDENCE 51
# ------------------------------------------------------------

test(
    "3. BUY CONFIDENCE 51",
    {
        "action": "BUY",
        "confidence": 51,
        "score": 75,
        "dominant_direction": "BULLISH",
        "conflict": False
    }
)


# ------------------------------------------------------------
# SELL - CONFIDENCE 51
# ------------------------------------------------------------

test(
    "4. SELL CONFIDENCE 51",
    {
        "action": "SELL",
        "confidence": 51,
        "score": 25,
        "dominant_direction": "BEARISH",
        "conflict": False
    }
)


# ------------------------------------------------------------
# STRONG BUY - LOW CONFIDENCE
# ------------------------------------------------------------

test(
    "5. STRONG BUY LOW CONFIDENCE",
    {
        "action": "STRONG BUY",
        "confidence": 10,
        "score": 60,
        "dominant_direction": "BULLISH",
        "conflict": False
    }
)


# ------------------------------------------------------------
# STRONG SELL - LOW CONFIDENCE
# ------------------------------------------------------------

test(
    "6. STRONG SELL LOW CONFIDENCE",
    {
        "action": "STRONG SELL",
        "confidence": 10,
        "score": 40,
        "dominant_direction": "BEARISH",
        "conflict": False
    }
)


# ------------------------------------------------------------
# BUY + CONFLICT
# ------------------------------------------------------------

test(
    "7. BUY + CONFLICT",
    {
        "action": "BUY",
        "confidence": 100,
        "score": 80,
        "dominant_direction": "BULLISH",
        "conflict": True
    }
)


# ------------------------------------------------------------
# BUY + WRONG DIRECTION
# ------------------------------------------------------------

test(
    "8. BUY + WRONG DIRECTION",
    {
        "action": "BUY",
        "confidence": 100,
        "score": 80,
        "dominant_direction": "BEARISH",
        "conflict": False
    }
)


# ------------------------------------------------------------
# HOLD
# ------------------------------------------------------------

test(
    "9. HOLD",
    {
        "action": "HOLD",
        "confidence": 100,
        "score": 50,
        "dominant_direction": "NEUTRAL",
        "conflict": False
    }
)


print()
print("=" * 100)
print("E.27.44 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

