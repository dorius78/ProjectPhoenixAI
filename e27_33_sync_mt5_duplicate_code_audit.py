from pathlib import Path

path = Path(
    "Core/live_trading_engine.py"
)

lines = path.read_text(
    encoding="utf-8-sig"
).splitlines()

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.33 SYNC MT5 DUPLICATE CODE AUDIT")
print("=" * 100)

inside = False

for number, line in enumerate(
    lines,
    start=1
):

    if "def _sync_mt5_position" in line:

        inside = True

    if inside:

        print(
            f"{number:04}: {line}"
        )

        if (
            number > 1
            and line.startswith("    def ")
            and
            "_sync_mt5_position"
            not in line
        ):

            break

print()
print("=" * 100)
print("SEARCH RETURN TRUE")
print("=" * 100)

for number, line in enumerate(
    lines,
    start=1
):

    if (
        "_sync_mt5_position"
        in "\n".join(lines[
            max(0, number-1):
            number+1
        ])
        and
        "return True" in line
    ):

        print(
            f"{number:04}: {line.strip()}"
        )

print()
print("=" * 100)
print("E.27.33 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

