from pathlib import Path

path = Path(
    "e27_12_55_close_ticket_propagation_test.py"
)

text = path.read_text(
    encoding="utf-8"
)

old = '''position = (
    engine.position_controller.get_position()
)

engine.execution = FakeExecution()

engine.database = FakeDatabase()

engine.backtest = FakeBacktest()

engine.portfolio = FakePortfolio()

engine.guard = FakeGuard()

engine.position_controller = (
    FakePositionController()
)

position = (
    engine.position_controller.get_position()
)
'''

new = '''engine.execution = FakeExecution()

engine.database = FakeDatabase()

engine.backtest = FakeBacktest()

engine.portfolio = FakePortfolio()

engine.guard = FakeGuard()

engine.position_controller = (
    FakePositionController()
)

position = (
    engine.position_controller.get_position()
)
'''

if old not in text:
    raise RuntimeError(
        "STOP: blocco inizializzazione test non trovato"
    )

text = text.replace(
    old,
    new,
    1
)

path.write_text(
    text,
    encoding="utf-8"
)

print("=" * 100)
print("E.27.12.55 TEST FIX APPLICATO")
print("=" * 100)
print("Production code: NON MODIFICATO")
print("Position Controller: inizializzato correttamente")
print("NESSUN order_send")
print("NESSUNA apertura")
print("NESSUNA chiusura")
print("=" * 100)

