import inspect

from Core.trade_manager import TradeManager

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.28 TRADE MANAGER INTEGRATION AUDIT")
print("=" * 100)

manager = TradeManager()

print()
print("1. TRADE MANAGER generate_trade()")
print("=" * 100)

print(
    inspect.getsource(
        TradeManager.generate_trade
    )
)

print()
print("2. TRADE MANAGER ATTRIBUTES")
print("=" * 100)

for name in dir(manager):

    if not name.startswith("__"):

        try:

            value = getattr(
                manager,
                name
            )

            print(
                f"{name}: {type(value).__name__}"
            )

        except Exception:
            pass

print()
print("=" * 100)
print("E.27.28 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

