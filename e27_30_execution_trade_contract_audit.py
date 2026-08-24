import inspect

from Execution.execution_engine import ExecutionEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.30 EXECUTION TRADE CONTRACT AUDIT")
print("=" * 100)

engine = ExecutionEngine()

print()
print("1. EXECUTION ENGINE execute()")
print("=" * 100)

print(
    inspect.getsource(
        ExecutionEngine.execute
    )
)

print()
print("2. EXECUTION ENGINE close()")
print("=" * 100)

print(
    inspect.getsource(
        ExecutionEngine.close
    )
)

print()
print("3. EXECUTION ENGINE ATTRIBUTES")
print("=" * 100)

for name in dir(engine):

    if not name.startswith("__"):

        try:

            value = getattr(
                engine,
                name
            )

            print(
                f"{name}: {type(value).__name__}"
            )

        except Exception:
            pass

print()
print("=" * 100)
print("E.27.30 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

