from pathlib import Path
import inspect

from Core.live_trading_engine import LiveTradingEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.35 CLOSED POSITION FLOW AUDIT")
print("=" * 100)

print()
print("=" * 100)
print("1. _sync_mt5_position()")
print("=" * 100)

print(
    inspect.getsource(
        LiveTradingEngine._sync_mt5_position
    )
)

print()
print("=" * 100)
print("2. _process_closed_position()")
print("=" * 100)

print(
    inspect.getsource(
        LiveTradingEngine._process_closed_position
    )
)

print()
print("=" * 100)
print("3. RICERCA CLOSED POSITION NEL LIVE ENGINE")
print("=" * 100)

path = Path(
    "Core/live_trading_engine.py"
)

lines = path.read_text(
    encoding="utf-8"
).splitlines()

keywords = [
    "status",
    "CLOSED",
    "close_reason",
    "current_profit",
    "current_price",
    "open_time",
    "close_time",
    "trade_id",
    "mt5_ticket",
    "_process_closed_position",
    "get_position",
    "has_position",
]

for i, line in enumerate(lines):

    if any(
        keyword.lower() in line.lower()
        for keyword in keywords
    ):

        print(
            f"{i+1:04}: {line}"
        )

print()
print("=" * 100)
print("4. BLOCCO START() RELATIVO ALLA POSIZIONE")
print("=" * 100)

start = None

for i, line in enumerate(lines):

    if line.strip().startswith("def start("):

        start = i
        break

if start is None:

    raise RuntimeError(
        "STOP: start() non trovato"
    )

end = min(
    start + 230,
    len(lines)
)

for i in range(start, end):

    print(
        f"{i+1:04}: {lines[i]}"
    )

print()
print("=" * 100)
print("5. OBIETTIVO E.27.12.35")
print("=" * 100)

print(
    "Individuare esattamente dove Phoenix "
    "deve riconoscere la scomparsa della "
    "posizione MT5."
)

print(
    "Individuare come costruire il dizionario "
    "closed per _process_closed_position()."
)

print(
    "NESSUNA PATCH IN QUESTA FASE."
)

print()
print("=" * 100)
print("E.27.12.35 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

