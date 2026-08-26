from pathlib import Path

files = [
    Path("Execution/execution_engine.py"),
    Path("MT5_Bridge/mt5_execution_recovered.py"),
    Path("Core/live_trading_engine.py"),
]

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.58 MT5 OPEN RESULT PROPAGATION AUDIT")
print("=" * 100)

for path in files:

    print()
    print("=" * 100)
    print(f"FILE: {path}")
    print("=" * 100)

    if not path.exists():

        print("FILE NOT FOUND")
        continue

    lines = path.read_text(
        encoding="utf-8"
    ).splitlines()

    targets = [
        "def execute(",
        "def _execute",
        "self.mt5.execute",
        "result = self.mt5.execute",
        "return {",
    ]

    for number, line in enumerate(
        lines,
        start=1
    ):

        if any(
            target in line
            for target in targets
        ):

            print(
                f"{number:04}: {line}"
            )


print()
print("=" * 100)
print("MT5 OPEN CONTRACT KEYWORDS")
print("=" * 100)

keywords = [
    "order_ticket",
    "deal_ticket",
    "position_ticket",
    "mt5_ticket",
    "retcode",
    "result.order",
    "result.deal",
    "result.position",
    "result.retcode",
    "TRADE_RETCODE_DONE",
]

for keyword in keywords:

    print()
    print(f"--- {keyword} ---")

    found = False

    for path in files:

        if not path.exists():
            continue

        lines = path.read_text(
            encoding="utf-8"
        ).splitlines()

        for number, line in enumerate(
            lines,
            start=1
        ):

            if keyword.lower() in line.lower():

                print(
                    f"{path}:{number}: {line.strip()}"
                )

                found = True

    if not found:
        print("NOT FOUND")


print()
print("=" * 100)
print("E.27.12.58 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

