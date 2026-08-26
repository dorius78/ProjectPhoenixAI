from pathlib import Path
import inspect

from Core.live_trading_engine import LiveTradingEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.33 MT5 CLOSE SYNC DESIGN AUDIT")
print("=" * 100)

print()
print("=" * 100)
print("1. _sync_mt5_position() COMPLETO")
print("=" * 100)

print(
    inspect.getsource(
        LiveTradingEngine._sync_mt5_position
    )
)

print()
print("=" * 100)
print("2. _process_closed_position() COMPLETO")
print("=" * 100)

print(
    inspect.getsource(
        LiveTradingEngine._process_closed_position
    )
)

print()
print("=" * 100)
print("3. _build_closed_trade() COMPLETO")
print("=" * 100)

print(
    inspect.getsource(
        LiveTradingEngine._build_closed_trade
    )
)

print()
print("=" * 100)
print("4. EXECUTION CLOSE")
print("=" * 100)

try:

    print(
        inspect.getsource(
            LiveTradingEngine.execution
        )
    )

except Exception:

    pass

print()
print("=" * 100)
print("5. RIFERIMENTI CLOSE / MT5")
print("=" * 100)

path = Path(
    "Core/live_trading_engine.py"
)

lines = path.read_text(
    encoding="utf-8"
).splitlines()

keywords = [
    "_sync_mt5_position",
    "close_position",
    "_process_closed_position",
    "_build_closed_trade",
    "execution.close",
    "portfolio.remove",
    "portfolio.update_balance",
    "mt5_ticket",
    "position_ticket",
    "current_profit",
    "close_reason",
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
print("6. OBIETTIVO E.27.12.33")
print("=" * 100)

print(
    "MT5 posizione scomparsa -> "
    "Phoenix deve riconoscere la chiusura."
)

print(
    "La chiusura deve passare dal "
    "Position Controller esistente."
)

print(
    "Il Portfolio deve essere aggiornato "
    "senza generare una nuova apertura."
)

print()
print("=" * 100)
print("E.27.12.33 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

