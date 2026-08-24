import inspect

from Core.risk_limits import RiskLimits

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.25 RISK LIMITS LOGIC AUDIT")
print("=" * 100)

manager = RiskLimits()

print()
print("1. RISK LIMITS evaluate()")
print("=" * 100)

print(
    inspect.getsource(
        RiskLimits.evaluate
    )
)

print()
print("2. RISK LIMITS ATTRIBUTES")
print("=" * 100)

for name in dir(manager):

    if not name.startswith("__"):

        try:

            value = getattr(
                manager,
                name
            )

            print(
                f"{name}: {type(value).__name__} = {value}"
            )

        except Exception:
            pass

print()
print("=" * 100)
print("E.27.25 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

