import inspect

from Execution.execution_engine import ExecutionEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.54 EXECUTION ENGINE AUDIT")
print("=" * 100)

engine = ExecutionEngine()

print()
print("EXECUTION ENGINE SOURCE")
print("=" * 100)

print(
    inspect.getsource(
        ExecutionEngine
    )
)

print()
print("=" * 100)
print("E.27.54 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

