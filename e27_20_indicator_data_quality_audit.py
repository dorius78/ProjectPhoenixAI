import math
import pandas as pd

from Data.Indicators.indicator_manager import IndicatorManager

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.20 INDICATOR DATA QUALITY AUDIT")
print("=" * 100)

# ============================================================
# TEST DATA
# ============================================================

rows = 100

data = pd.DataFrame({

    "Open": [
        100000 + i * 10
        for i in range(rows)
    ],

    "High": [
        100500 + i * 10
        for i in range(rows)
    ],

    "Low": [
        99500 + i * 10
        for i in range(rows)
    ],

    "Close": [
        100000 + i * 10
        for i in range(rows)
    ],

    "Volume": [
        1000 + i * 5
        for i in range(rows)
    ]

})

# ============================================================
# INDICATORS
# ============================================================

manager = IndicatorManager()

indicators = manager.get_indicators(
    data
)

print()
print("1. INDICATOR OUTPUT")
print("=" * 100)

for key, value in indicators.items():

    print(
        f"{key:20} = {value}"
    )

# ============================================================
# DATA QUALITY
# ============================================================

print()
print("2. DATA QUALITY")
print("=" * 100)

invalid = []

for key, value in indicators.items():

    if isinstance(
        value,
        (int, float)
    ):

        if not math.isfinite(
            float(value)
        ):

            invalid.append(
                (key, value)
            )

print(
    "INVALID VALUES:",
    len(invalid)
)

for item in invalid:

    print(
        "INVALID:",
        item
    )

# ============================================================
# ZERO VALUES
# ============================================================

print()
print("3. ZERO VALUES")
print("=" * 100)

zeros = []

for key, value in indicators.items():

    if isinstance(
        value,
        (int, float)
    ):

        if float(value) == 0:

            zeros.append(
                key
            )

print(
    "ZERO FIELDS:",
    zeros
)

# ============================================================
# REQUIRED FIELDS
# ============================================================

print()
print("4. REQUIRED FIELDS")
print("=" * 100)

required = [

    "price",
    "ema20",
    "ema50",
    "sma20",
    "rsi",
    "macd",
    "macd_signal",
    "macd_histogram",
    "atr",
    "adx",
    "bb_upper",
    "bb_middle",
    "bb_lower",
    "volume",
    "volume_avg",
    "volume_ratio"

]

missing = [

    key
    for key in required
    if key not in indicators

]

print(
    "MISSING:",
    missing
)

# ============================================================
# RESULT
# ============================================================

print()
print("=" * 100)

if (
    len(invalid) == 0
    and len(missing) == 0
):

    print(
        "E.27.20 DATA QUALITY: PASS"
    )

else:

    print(
        "E.27.20 DATA QUALITY: ATTENTION"
    )

print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

