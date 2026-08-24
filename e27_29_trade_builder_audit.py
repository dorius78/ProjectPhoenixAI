import inspect

from Core.trade_builder import TradeBuilder

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.29 TRADE BUILDER AUDIT")
print("=" * 100)

builder = TradeBuilder()

print()
print("1. TRADE BUILDER build()")
print("=" * 100)

print(
    inspect.getsource(
        TradeBuilder.build
    )
)

print()
print("2. TRADE BUILDER ATTRIBUTES")
print("=" * 100)

for name in dir(builder):

    if not name.startswith("__"):

        try:

            value = getattr(
                builder,
                name
            )

            print(
                f"{name}: {type(value).__name__}"
            )

        except Exception:
            pass

print()
print("=" * 100)
print("E.27.29 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

