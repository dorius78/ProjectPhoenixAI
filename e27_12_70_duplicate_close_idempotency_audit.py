from pathlib import Path

path = Path(
    "Core/live_trading_engine.py"
)

lines = path.read_text(
    encoding="utf-8"
).splitlines()

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.70 DUPLICATE CLOSE / IDEMPOTENCY AUDIT")
print("=" * 100)

print()
print("1. IDENTIFICAZIONE TRADE")
print("-" * 100)

keywords = [
    "trade_id",
    "mt5_ticket",
    "mt5_order_ticket",
    "mt5_deal_ticket",
    "save_trade",
    "saved",
    "duplicate",
    "already",
    "CLOSED",
]

for number, line in enumerate(
    lines,
    start=1
):

    if any(
        keyword.lower() in line.lower()
        for keyword in keywords
    ):

        print(
            f"{number:04}: {line.strip()}"
        )

print()
print("=" * 100)
print("2. _process_closed_position()")
print("=" * 100)

start = None

for i, line in enumerate(lines):

    if line.strip().startswith(
        "def _process_closed_position("
    ):

        start = i
        break

if start is None:
    raise RuntimeError(
        "STOP: _process_closed_position() non trovato"
    )

for i in range(
    start,
    min(start + 240, len(lines))
):

    print(
        f"{i+1:04}: {lines[i]}"
    )

print()
print("=" * 100)
print("3. BUILD CLOSED TRADE")
print("=" * 100)

start = None

for i, line in enumerate(lines):

    if line.strip().startswith(
        "def _build_closed_trade("
    ):

        start = i
        break

if start is None:
    raise RuntimeError(
        "STOP: _build_closed_trade() non trovato"
    )

for i in range(
    start,
    min(start + 180, len(lines))
):

    print(
        f"{i+1:04}: {lines[i]}"
    )

print()
print("=" * 100)
print("E.27.12.70 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

