from pathlib import Path

path = Path(
    "e27_12_64_mt5_open_recovery_no_duplicate_test.py"
)

text = path.read_text(
    encoding="utf-8"
)

old = '''class FakeMT5Position:

    ticket = 55555555
    symbol = "BTCUSD"

    type = 0
'''

new = '''class FakeMT5Position:

    ticket = 55555555
    symbol = "BTCUSD"

    magic = 260813

    type = 0
'''

if old not in text:
    raise RuntimeError(
        "STOP: FakeMT5Position non trovato"
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
print("E.27.12.64B TEST FIX APPLICATO")
print("=" * 100)
print("Production code: NON MODIFICATO")
print("Fake MT5 magic: 260813")
print("NESSUN order_send")
print("NESSUNA apertura")
print("NESSUNA chiusura")
print("=" * 100)

