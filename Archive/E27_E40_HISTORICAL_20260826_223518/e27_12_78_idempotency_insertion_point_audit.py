from pathlib import Path
import inspect

from Core.live_trading_engine import LiveTradingEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.78 IDEMPOTENCY INSERTION POINT AUDIT")
print("=" * 100)

source = inspect.getsource(
    LiveTradingEngine._process_closed_position
)

lines = source.splitlines()

for number, line in enumerate(
    lines,
    start=1
):

    if (
        "trade_id" in line
        or
        "execution.close" in line
        or
        "external_mt5_close" in line
        or
        "report =" in line
        or
        "execution_success" in line
    ):

        start = max(
            0,
            number - 5
        )

        end = min(
            len(lines),
            number + 8
        )

        print()
        print(
            f"--- CONTEXT {number} ---"
        )
        print("-" * 100)

        for i in range(
            start,
            end
        ):

            print(
                f"{i+1:04}: {lines[i]}"
            )

print()
print("=" * 100)
print("DATABASE has_trade()")
print("=" * 100)

from Database.database_manager import DatabaseManager

print(
    inspect.getsource(
        DatabaseManager.has_trade
    )
)

print()
print("=" * 100)
print("E.27.12.78 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

