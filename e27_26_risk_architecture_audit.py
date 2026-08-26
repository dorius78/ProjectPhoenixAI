import inspect

from Core.risk_position_size import RiskPositionSize
from Core.risk_drawdown import RiskDrawdown

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.26 RISK ARCHITECTURE AUDIT")
print("=" * 100)

print()
print("1. RISK POSITION SIZE")
print("=" * 100)

print(
    inspect.getsource(
        RiskPositionSize
    )
)

print()
print("2. RISK DRAWDOWN")
print("=" * 100)

print(
    inspect.getsource(
        RiskDrawdown
    )
)

print()
print("=" * 100)
print("E.27.26 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

