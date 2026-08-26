import inspect

from Core.phoenix_brain import PhoenixBrain
from Core.signal_manager import SignalManager

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.16 DECISION LAYER AUDIT")
print("=" * 100)

print()
print("1. PHOENIX BRAIN")
print("=" * 100)

print(
    inspect.getsource(
        PhoenixBrain.think
    )
)

print()
print("2. SIGNAL MANAGER")
print("=" * 100)

print(
    inspect.getsource(
        SignalManager.validate
    )
)

print()
print("=" * 100)
print("E.27.16 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

