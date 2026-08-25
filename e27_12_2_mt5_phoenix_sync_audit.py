import inspect

from Core.live_trading_engine import LiveTradingEngine
from Execution.execution_engine import MT5ExecutionEngine
from Core.position_controller import PositionController

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.2 MT5/Phoenix SYNCHRONIZATION AUDIT")
print("=" * 100)

print()
print("=" * 100)
print("1. MT5 EXECUTION ENGINE")
print("=" * 100)

print()
print("METODI DISPONIBILI:")
print([
    x for x in dir(MT5ExecutionEngine)
    if not x.startswith("__")
])

print()
print("GET PHOENIX POSITIONS:")
print(inspect.getsource(
    MT5ExecutionEngine.get_phoenix_positions
))

print()
print("GET OPEN POSITIONS:")
print(inspect.getsource(
    MT5ExecutionEngine.get_open_positions
))

print()
print("=" * 100)
print("2. POSITION CONTROLLER")
print("=" * 100)

print()
print("METODI DISPONIBILI:")
print([
    x for x in dir(PositionController)
    if not x.startswith("__")
])

print()
print("UPDATE:")
print(inspect.getsource(
    PositionController.update
))

print()
print("=" * 100)
print("3. LIVE ENGINE - POSIZIONE")
print("=" * 100)

print()
print(inspect.getsource(
    LiveTradingEngine._close_position
))

print()
print("=" * 100)
print("E.27.12.2 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("=" * 100)
