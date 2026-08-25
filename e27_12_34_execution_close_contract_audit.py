import inspect

from Execution.execution_engine import ExecutionEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.34 EXECUTION CLOSE CONTRACT AUDIT")
print("=" * 100)

engine = ExecutionEngine.__new__(
    ExecutionEngine
)

print()
print("=" * 100)
print("1. METODI CLOSE PRESENTI")
print("=" * 100)

for name in dir(ExecutionEngine):

    if "close" in name.lower():

        attribute = getattr(
            ExecutionEngine,
            name
        )

        if callable(attribute):

            print()
            print("METODO:", name)
            print("-" * 100)

            try:

                print(
                    inspect.getsource(
                        attribute
                    )
                )

            except Exception as error:

                print(
                    "SOURCE NON DISPONIBILE:",
                    error
                )

print()
print("=" * 100)
print("2. RIFERIMENTI CLOSE NEL FILE")
print("=" * 100)

from pathlib import Path

path = Path(
    "Execution/execution_engine.py"
)

lines = path.read_text(
    encoding="utf-8"
).splitlines()

keywords = [
    "def close",
    "close_position",
    "self.mt5.close",
    "mt5.close",
    "executed",
    "success",
    "dry_run",
    "retcode",
    "ticket",
    "position_ticket",
    "deal_ticket",
    "result",
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
print("3. CONTRATTO NECESSARIO")
print("=" * 100)

print(
    "Verificare come ExecutionEngine.close() "
    "conferma una chiusura MT5."
)

print(
    "Verificare quali campi restituisce "
    "al LiveTradingEngine."
)

print(
    "Verificare ticket / retcode / success / executed."
)

print()
print("=" * 100)
print("E.27.12.34 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

