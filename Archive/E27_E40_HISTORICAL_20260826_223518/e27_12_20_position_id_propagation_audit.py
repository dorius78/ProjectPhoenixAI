from pathlib import Path

files = [
    "Execution/execution_engine.py",
    "Execution/mt5_execution_engine.py",
    "Core/live_trading_engine.py",
    "Core/position_controller.py",
]

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.20 POSITION ID PROPAGATION AUDIT")
print("=" * 100)

for filename in files:

    path = Path(filename)

    print()
    print("=" * 100)
    print(filename)
    print("=" * 100)

    if not path.exists():
        print("FILE NON PRESENTE")
        continue

    lines = path.read_text(
        encoding="utf-8"
    ).splitlines()

    keywords = [
        "def execute(",
        "result",
        "executed",
        "retcode",
        "mt5",
        "ticket",
        "deal",
        "position",
        "magic",
        "symbol",
        "return {",
        "_open_position_from_order",
        "open_position",
    ]

    for i, line in enumerate(lines):

        if any(
            keyword.lower() in line.lower()
            for keyword in keywords
        ):
            print(
                f"{i+1:04}: {line}"
            )

print()
print("=" * 100)
print("E.27.12.20 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

