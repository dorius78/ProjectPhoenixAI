import inspect

from Core.phoenix_brain_logic import PhoenixBrainLogic

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.37 DECISION CORE DEEP AUDIT")
print("=" * 100)

logic = PhoenixBrainLogic()

print()
print("METODO calculate() COMPLETO")
print("=" * 100)

print(
    inspect.getsource(
        PhoenixBrainLogic.calculate
    )
)

print()
print("=" * 100)
print("ATTRIBUTI")
print("=" * 100)

for name in dir(logic):

    if not name.startswith("__"):

        try:

            value = getattr(
                logic,
                name
            )

            print(
                f"{name}: {type(value).__name__}"
            )

        except Exception:
            pass

print()
print("=" * 100)
print("E.27.37 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

