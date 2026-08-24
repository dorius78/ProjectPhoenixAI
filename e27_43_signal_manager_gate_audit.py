import inspect

from Core.signal_manager import SignalManager

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.43 SIGNAL MANAGER GATE AUDIT")
print("=" * 100)

manager = SignalManager()

print()
print("SIGNAL MANAGER SOURCE")
print("=" * 100)

print(
    inspect.getsource(
        SignalManager
    )
)

print()
print("=" * 100)
print("E.27.43 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

