from MT5_Bridge.mt5_execution_recovered import MT5ExecutionEngine
import inspect

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.49 MT5 CLOSE RESULT CONTRACT AUDIT")
print("=" * 100)

source = inspect.getsource(
    MT5ExecutionEngine.close_position
)

print()
print("=" * 100)
print("METODO close_position()")
print("=" * 100)

print(source)

print()
print("=" * 100)
print("RICERCA CAMPI RISULTATO")
print("=" * 100)

keywords = [
    "result",
    "retcode",
    "ticket",
    "order",
    "deal",
    "position",
    "order_ticket",
    "deal_ticket",
    "position_ticket",
    "executed",
    "success",
    "message",
    "mt5"
]

for number, line in enumerate(
    source.splitlines(),
    start=1
):

    if any(
        keyword.lower() in line.lower()
        for keyword in keywords
    ):

        print(
            f"{number:04}: {line}"
        )

print()
print("=" * 100)
print("E.27.12.49 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

