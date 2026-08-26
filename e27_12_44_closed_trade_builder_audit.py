from Core.live_trading_engine import LiveTradingEngine
import inspect

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.44 CLOSED TRADE BUILDER AUDIT")
print("=" * 100)

print()
print("=" * 100)
print("METODO _build_closed_trade()")
print("=" * 100)

source = inspect.getsource(
    LiveTradingEngine._build_closed_trade
)

print(source)

print()
print("=" * 100)
print("RICERCA CAMPI MT5")
print("=" * 100)

keywords = [
    "mt5_ticket",
    "mt5_symbol",
    "magic",
    "order_ticket",
    "deal_ticket",
    "position_ticket",
    "ticket",
    "trade_id",
    "pnl",
    "reason",
    "result"
]

for number, line in enumerate(
    source.splitlines(),
    start=1
):

    if any(
        keyword.lower() in line.lower()
        for keyword in keywords
    ):

        print(
            f"{number:04}: {line}"
        )

print()
print("=" * 100)
print("E.27.12.44 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

