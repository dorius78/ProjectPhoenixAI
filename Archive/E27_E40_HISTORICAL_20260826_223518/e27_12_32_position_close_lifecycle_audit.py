from pathlib import Path
import inspect

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.32 POSITION CLOSE LIFECYCLE AUDIT")
print("=" * 100)

print()
print("=" * 100)
print("1. POSITION CONTROLLER")
print("=" * 100)

from Core.position_controller import PositionController

print(
    inspect.getsource(
        PositionController
    )
)

print()
print("=" * 100)
print("2. LIVE TRADING ENGINE - CLOSE REFERENCES")
print("=" * 100)

from Core.live_trading_engine import LiveTradingEngine

lines = Path(
    "Core/live_trading_engine.py"
).read_text(
    encoding="utf-8"
).splitlines()

keywords = [
    "close_position",
    "position_controller",
    "portfolio",
    "exit_manager",
    "mt5_ticket",
    "execution",
    "closed",
    "close",
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
print("3. METODI CLOSE POSITION")
print("=" * 100)

for name in dir(PositionController):

    if (
        "close" in name.lower()
        or "remove" in name.lower()
        or "reset" in name.lower()
        or "clear" in name.lower()
    ):

        attribute = getattr(
            PositionController,
            name
        )

        if callable(attribute):

            print()
            print(
                "METODO:",
                name
            )

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
print("4. PORTFOLIO CLOSE / REMOVE")
print("=" * 100)

from Core.portfolio_manager import PortfolioManager

for name in dir(PortfolioManager):

    if (
        "close" in name.lower()
        or "remove" in name.lower()
        or "delete" in name.lower()
        or "update" in name.lower()
    ):

        attribute = getattr(
            PortfolioManager,
            name
        )

        if callable(attribute):

            print()
            print(
                "PORTFOLIO METODO:",
                name
            )

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
print("E.27.12.32 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

