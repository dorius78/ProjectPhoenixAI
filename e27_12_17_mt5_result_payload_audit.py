from Core.core_system import CoreSystem

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.17 MT5 RESULT PAYLOAD AUDIT")
print("=" * 100)

c = CoreSystem()

engine = c.execution
bridge = engine.mt5

print()
print("MT5 ENABLED:", engine.mt5_enabled)
print("MT5 DRY RUN:", engine.mt5_dry_run)

assert bridge is not None

print()
print("=" * 100)
print("METODO MT5 EXECUTE()")
print("=" * 100)

import inspect

print(
    inspect.getsource(
        bridge.execute
    )
)

print()
print("=" * 100)
print("AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)
