import inspect
from Execution.execution_engine import MT5ExecutionEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.19 MT5 RESULT CONTRACT DEEP AUDIT")
print("=" * 100)

engine = MT5ExecutionEngine(
    symbol="BTCUSD"
)

print()
print("=" * 100)
print("1. METODO execute() DEL BRIDGE")
print("=" * 100)

print(
    inspect.getsource(
        MT5ExecutionEngine.execute
    )
)

print()
print("=" * 100)
print("2. METODO check_order()")
print("=" * 100)

print(
    inspect.getsource(
        MT5ExecutionEngine.check_order
    )
)

print()
print("=" * 100)
print("3. METODI PREPARAZIONE ORDINE")
print("=" * 100)

print(
    inspect.getsource(
        MT5ExecutionEngine.prepare_order
    )
)

print()
print("=" * 100)
print("4. CONTRATTO RESULT")
print("=" * 100)

print("Il bridge restituisce il risultato MT5 sotto:")
print("result['result']")
print()
print("Nessun ordine viene inviato da questo audit.")

print()
print("=" * 100)
print("E.27.12.19 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

