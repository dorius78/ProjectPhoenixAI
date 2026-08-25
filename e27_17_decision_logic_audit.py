import inspect

from Core.phoenix_brain import PhoenixBrain

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.17 DECISION LOGIC AUDIT")
print("=" * 100)

brain = PhoenixBrain()

print()
print("1. PHOENIX BRAIN ATTRIBUTI")
print("=" * 100)

for name in dir(brain):
    if not name.startswith("__"):
        try:
            value = getattr(brain, name)
            print(
                f"{name}: {type(value).__name__}"
            )
        except Exception:
            pass

print()
print("2. LOGIC OBJECT")
print("=" * 100)

logic = brain.logic

print(
    "TYPE:",
    type(logic).__name__
)

print()
print("3. CALCULATE()")
print("=" * 100)

print(
    inspect.getsource(
        logic.calculate
    )
)

print()
print("=" * 100)
print("E.27.17 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

