from pathlib import Path
import inspect

from Core.live_trading_engine import LiveTradingEngine


print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.64A MAGIC RECOVERY AUDIT")
print("=" * 100)


# ============================================================
# 1. SYNC METHOD
# ============================================================

print()
print("=" * 100)
print("1. _sync_mt5_position()")
print("=" * 100)

source = inspect.getsource(
    LiveTradingEngine._sync_mt5_position
)

print(source)


# ============================================================
# 2. MAGIC REFERENCES
# ============================================================

print()
print("=" * 100)
print("2. MAGIC REFERENCES NEL METODO")
print("=" * 100)

for number, line in enumerate(
    source.splitlines(),
    start=1
):

    if "magic" in line.lower():

        print(
            f"{number:04}: {line}"
        )


# ============================================================
# 3. MT5 POSITION ATTRIBUTES
# ============================================================

print()
print("=" * 100)
print("3. ATTRIBUTI MT5 USATI DAL RECOVERY")
print("=" * 100)

keywords = [
    "ticket",
    "symbol",
    "type",
    "volume",
    "price_open",
    "sl",
    "tp",
    "price_current",
    "profit",
    "magic",
]

for keyword in keywords:

    print(
        f"{keyword}: "
        f"{keyword in source}"
    )


# ============================================================
# 4. BRIDGE
# ============================================================

print()
print("=" * 100)
print("4. BRIDGE REFERENCES")
print("=" * 100)

bridge_path = Path(
    "MT5_Bridge/mt5_execution_recovered.py"
)

bridge_text = bridge_path.read_text(
    encoding="utf-8"
)

for number, line in enumerate(
    bridge_text.splitlines(),
    start=1
):

    if (
        "get_phoenix_positions"
        in line
        or
        "magic"
        in line.lower()
    ):

        print(
            f"{number:04}: {line.strip()}"
        )


# ============================================================
# RESULT
# ============================================================

print()
print("=" * 100)
print("E.27.12.64A AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

