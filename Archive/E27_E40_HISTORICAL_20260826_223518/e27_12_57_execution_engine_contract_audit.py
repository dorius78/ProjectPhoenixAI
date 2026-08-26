from pathlib import Path

path = Path(
    "Execution/execution_engine.py"
)

text = path.read_text(
    encoding="utf-8"
)

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.57 EXECUTION ENGINE CONTRACT AUDIT")
print("=" * 100)

lines = text.splitlines()

methods = [
    "def execute(",
    "def open(",
    "def close(",
]

print()
print("=" * 100)
print("1. EXECUTION METHODS")
print("=" * 100)

for method in methods:

    found = False

    for number, line in enumerate(
        lines,
        start=1
    ):

        if line.strip().startswith(method):

            print(
                f"{method} -> FOUND line {number}"
            )

            found = True
            break

    if not found:
        print(
            f"{method} -> NOT FOUND"
        )


print()
print("=" * 100)
print("2. OPEN / EXECUTION CONTRACT")
print("=" * 100)

keywords = [
    "success",
    "executed",
    "dry_run",
    "order_ticket",
    "deal_ticket",
    "position_ticket",
    "mt5_ticket",
    "retcode",
    "result",
    "symbol",
    "side",
    "entry",
    "stop_loss",
    "take_profit",
    "size",
]

for keyword in keywords:

    count = text.lower().count(
        keyword.lower()
    )

    print(
        f"{keyword}: {count} occurrence(s)"
    )


print()
print("=" * 100)
print("3. MT5 CALLS")
print("=" * 100)

for number, line in enumerate(
    lines,
    start=1
):

    if (
        "self.mt5." in line
        or
        "mt5." in line
    ):

        print(
            f"{number:04}: {line.strip()}"
        )


print()
print("=" * 100)
print("4. ORDER SEND")
print("=" * 100)

for number, line in enumerate(
    lines,
    start=1
):

    if "order_send" in line:

        print(
            f"{number:04}: {line.strip()}"
        )


print()
print("=" * 100)
print("5. RESULT PROPAGATION")
print("=" * 100)

result_tokens = [
    "result.get",
    '"result"',
    '"order_ticket"',
    '"deal_ticket"',
    '"position_ticket"',
    '"retcode"',
]

for token in result_tokens:

    print(
        f"{token}: "
        f"{'FOUND' if token in text else 'NOT FOUND'}"
    )


print()
print("=" * 100)
print("E.27.12.57 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

