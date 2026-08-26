import inspect

from Data.Indicators.indicator_manager import IndicatorManager

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.19 INDICATOR DATA SOURCE AUDIT")
print("=" * 100)

manager = IndicatorManager()

print()
print("1. INDICATOR MANAGER")
print("=" * 100)

print(
    inspect.getsource(
        IndicatorManager.get_indicators
    )
)

print()
print("2. ATTRIBUTI INDICATOR MANAGER")
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
print("E.27.19 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

