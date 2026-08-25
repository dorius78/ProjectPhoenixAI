from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from Core.position_controller import PositionController


print()
print("=" * 70)
print(" PROJECT PHOENIX AI - TEST CICLO POSIZIONE")
print("=" * 70)
print()


controller = PositionController()


print("[1] Apertura posizione BUY...")

opened = controller.open_position(
    side="BUY",
    entry=100000,
    stop_loss=98000,
    take_profit=104000,
    symbol="BTC-USD",
    size=0.01
)

assert opened is True
assert controller.has_position() is True

print("[OK] Posizione aperta.")
print()


print("[2] Aggiornamento posizione in profitto...")

position = controller.update(
    current_price=101000
)

assert position is not None
assert position["status"] == "OPEN"
assert position["current_profit"] > 0

print("[OK] Posizione aggiornata.")
print()


print("[3] Verifica Break Even...")

position = controller.get_position()

assert position["break_even"] is True
assert position["stop_loss"] == position["entry"]

print("[OK] Break Even attivato.")
print()


print("[4] Aggiornamento verso Take Profit...")

closed = controller.update(
    current_price=104000
)

assert closed is not None
assert closed["status"] == "CLOSED"
assert closed["close_reason"] == "TAKE PROFIT"
assert closed["current_profit"] > 0

print("[OK] Take Profit raggiunto.")
print()


print("[5] Verifica posizione chiusa...")

assert controller.has_position() is False
assert controller.get_position() is None

print("[OK] Nessuna posizione residua.")
print()


print("=" * 70)
print(" TEST CICLO POSIZIONE: SUPERATO")
print("=" * 70)
print()
