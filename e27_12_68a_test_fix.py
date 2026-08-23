from pathlib import Path

path = Path(
    "e27_12_68_normal_close_result_lifecycle_test.py"
)

text = path.read_text(
    encoding="utf-8"
)

old = '''assert (
    engine.execution.close_called
    == 0
)
'''

new = '''assert (
    engine.execution.close_called
    == 1
)
'''

if old not in text:
    raise RuntimeError(
        "STOP: assertion close_called non trovata"
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
print("E.27.12.68A TEST FIX APPLICATO")
print("=" * 100)
print("Production code: NON MODIFICATO")
print("Normal close -> execution.close(): ATTESO 1")
print("NESSUN ordine MT5 reale")
print("NESSUNA apertura")
print("NESSUNA chiusura")
print("=" * 100)

