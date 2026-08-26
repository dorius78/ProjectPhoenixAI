import inspect

from Core.risk_manager import RiskManager

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.24 RISK AI DECISION INTERFACE AUDIT")
print("=" * 100)

manager = RiskManager()

print()
print("1. RISK MANAGER evaluate()")
print("=" * 100)

print(
    inspect.getsource(
        RiskManager.evaluate
    )
)

print()
print("2. RISK MANAGER ATTRIBUTES")
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
print("E.27.24 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

