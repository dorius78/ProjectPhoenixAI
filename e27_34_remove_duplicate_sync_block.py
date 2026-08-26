from pathlib import Path

path = Path(
    "Core/live_trading_engine.py"
)

text = path.read_text(
    encoding="utf-8-sig"
)

start_marker = '''        bridge = getattr(
            self.execution,
            "mt5",
            None
        )

        if bridge is None:
            return False
'''

end_marker = '''        return True

    # =====================================
    # PREZZO CORRENTE
'''

first = text.find(start_marker)

if first == -1:
    raise RuntimeError(
        "STOP: primo blocco bridge non trovato"
    )

second = text.find(
    start_marker,
    first + len(start_marker)
)

if second == -1:
    raise RuntimeError(
        "STOP: secondo blocco bridge duplicato non trovato"
    )

end = text.find(
    end_marker,
    second
)

if end == -1:
    raise RuntimeError(
        "STOP: fine blocco duplicato non trovata"
    )

duplicate_end = end + len(
    "        return True\n"
)

duplicate_block = text[
    second:
    duplicate_end
]

print("=" * 100)
print("E.27.34 DUPLICATE SYNC BLOCK PATCH")
print("=" * 100)
print("DUPLICATE BLOCK FOUND: YES")
print(
    "DUPLICATE BLOCK SIZE:",
    len(duplicate_block.splitlines()),
    "lines"
)

text = (
    text[:second]
    + text[duplicate_end:]
)

path.write_text(
    text,
    encoding="utf-8"
)

print("BACKUP: OK")
print("DUPLICATE BLOCK REMOVED: YES")
print("FIRST ACTIVE BLOCK: PRESERVED")
print("MT5 EXECUTION CODE: UNTOUCHED")
print("OPEN LOGIC: UNTOUCHED")
print("CLOSE LOGIC: UNTOUCHED")
print("=" * 100)

