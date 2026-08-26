import inspect

import Core.signal_manager as module
from Core.signal_manager import SignalManager

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.45 MIN CONFIDENCE SOURCE AUDIT")
print("=" * 100)

print()
print("1. SIGNAL MANAGER MODULE")
print("=" * 100)

print(
    inspect.getsource(module)
)

print()
print("2. RUNTIME MIN_CONFIDENCE")
print("=" * 100)

print(
    "MIN_CONFIDENCE =",
    getattr(
        module,
        "MIN_CONFIDENCE",
        "NOT FOUND"
    )
)

print()
print("3. SIGNAL MANAGER CONSTANTS")
print("=" * 100)

manager = SignalManager()

for name in dir(module):

    if "CONFIDENCE" in name.upper():

        try:

            print(
                name,
                "=",
                getattr(module, name)
            )

        except Exception:
            pass

print()
print("=" * 100)
print("E.27.45 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

