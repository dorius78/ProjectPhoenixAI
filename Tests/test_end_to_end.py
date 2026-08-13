from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from Core.analysis_engine import AnalysisEngine
from Core.trade_manager import TradeManager
from Core.position_controller import PositionController
from Core.exit_manager import ExitManager


print()
print("=" * 70)
print(" PROJECT PHOENIX AI - TEST END-TO-END")
print("=" * 70)
print()

print("[1] Inizializzazione moduli...")

analysis = AnalysisEngine()
trade_manager = TradeManager()
position_controller = PositionController()
exit_manager = ExitManager()

print()
print("[OK] Moduli inizializzati.")
print()

print("=" * 70)
print(" TEST END-TO-END COMPLETATO")
print("=" * 70)
print()
