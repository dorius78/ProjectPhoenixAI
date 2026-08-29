import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from Config.settings import MODE
from Execution.execution_engine import ExecutionEngine

print("=" * 100)
print("PHOENIX DEMO SAFETY GATE TEST")
print("=" * 100)

print("MODE =", MODE)

engine = ExecutionEngine(
    symbol="BTCUSD",
    mt5_enabled=True,
    mt5_dry_run=False
)

print("MT5 ENABLED =", engine.mt5_enabled)
print("MT5 DRY RUN =", engine.mt5_dry_run)

assert str(MODE).upper() == "DEMO"
assert engine.mt5_dry_run is True

print("")
print("PASS = True")
print("=" * 100)
print("NESSUN ORDER_SEND")
print("NESSUN ORDINE MT5")
print("NESSUN LIVE")
print("=" * 100)
