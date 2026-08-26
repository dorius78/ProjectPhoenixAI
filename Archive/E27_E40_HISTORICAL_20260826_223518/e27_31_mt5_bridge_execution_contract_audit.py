import inspect

from MT5_Bridge.mt5_execution_recovered import MT5ExecutionRecovered

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.31 MT5 BRIDGE EXECUTION CONTRACT AUDIT")
print("=" * 100)

bridge = MT5ExecutionRecovered()

print()
print("1. EXECUTE()")
print("=" * 100)

print(
    inspect.getsource(
        MT5ExecutionRecovered.execute
    )
)

print()
print("2. CLOSE_POSITION()")
print("=" * 100)

print(
    inspect.getsource(
        MT5ExecutionRecovered.close_position
    )
)

print()
print("3. BRIDGE ATTRIBUTES")
print("=" * 100)

for name in dir(bridge):

    if not name.startswith("__"):

        try:

            value = getattr(
                bridge,
                name
            )

            print(
                f"{name}: {type(value).__name__}"
            )

        except Exception:
            pass

print()
print("=" * 100)
print("E.27.31 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

