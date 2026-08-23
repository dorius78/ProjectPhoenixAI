import inspect

from Core.live_trading_engine import LiveTradingEngine
from Core.position_controller import PositionController

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.36 EXTERNAL MT5 CLOSE CONTRACT AUDIT")
print("=" * 100)

print()
print("=" * 100)
print("1. _build_closed_trade()")
print("=" * 100)

print(
    inspect.getsource(
        LiveTradingEngine._build_closed_trade
    )
)

print()
print("=" * 100)
print("2. POSITION CONTROLLER - METODI CHIUSURA")
print("=" * 100)

for name in dir(PositionController):

    if any(
        key in name.lower()
        for key in [
            "close",
            "remove",
            "clear",
            "reset",
            "update"
        ]
    ):

        attribute = getattr(
            PositionController,
            name
        )

        if callable(attribute):

            print()
            print("METODO:", name)
            print("-" * 100)

            try:

                print(
                    inspect.getsource(
                        attribute
                    )
                )

            except Exception as error:

                print(
                    "SOURCE NON DISPONIBILE:",
                    error
                )

print()
print("=" * 100)
print("3. POSITION CONTROLLER - CAMPI INTERNI")
print("=" * 100)

path = __import__("pathlib").Path(
    "Core/position_controller.py"
)

lines = path.read_text(
    encoding="utf-8"
).splitlines()

keywords = [
    "self.position",
    "position =",
    "status",
    "CLOSED",
    "close_reason",
    "current_price",
    "current_profit",
    "open_time",
    "close_time",
    "trade_id",
    "mt5_ticket"
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
print("4. OBIETTIVO")
print("=" * 100)

print(
    "Determinare come costruire una posizione "
    "CLOSED quando MT5 la chiude esternamente."
)

print(
    "Determinare come rimuovere la posizione "
    "dal Position Controller senza inviare "
    "un nuovo ordine MT5."
)

print(
    "Determinare quali dati sono necessari "
    "per Database / Portfolio / Trading Guard."
)

print()
print("=" * 100)
print("E.27.12.36 AUDIT COMPLETATO")
print("NESSUNA PATCH")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

