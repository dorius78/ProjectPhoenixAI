import inspect

import MT5_Bridge.mt5_execution_recovered as bridge_module

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.31A MT5 BRIDGE CLASS AUDIT")
print("=" * 100)

print()
print("OGGETTI PRESENTI NEL MODULO")
print("=" * 100)

for name, value in vars(bridge_module).items():

    if not name.startswith("__"):

        print(
            f"{name}: {type(value).__name__}"
        )

print()
print("=" * 100)
print("CLASSI")
print("=" * 100)

for name, value in vars(bridge_module).items():

    if inspect.isclass(value):

        print()
        print(f"CLASS: {name}")
        print("-" * 100)

        try:
            print(
                inspect.getsource(value)
            )
        except Exception as exc:
            print(
                f"SOURCE NON DISPONIBILE: {exc}"
            )

print()
print("=" * 100)
print("E.27.31A AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

