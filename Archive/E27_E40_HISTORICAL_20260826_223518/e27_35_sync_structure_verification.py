import inspect

from Core.live_trading_engine import LiveTradingEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.35 SYNC STRUCTURE VERIFICATION")
print("=" * 100)

source = inspect.getsource(
    LiveTradingEngine._sync_mt5_position
)

print()
print("METODO _sync_mt5_position()")
print("=" * 100)
print(source)

print()
print("OCCORRENZE get_phoenix_positions():")
print(
    source.count(
        "get_phoenix_positions"
    )
)

print()
print("OCCORRENZE return True:")
print(
    source.count(
        "return True"
    )
)

print()
print("=" * 100)

if source.count("get_phoenix_positions") == 1:
    print("SYNC METHOD: SINGLE IMPLEMENTATION: PASS")
else:
    print("SYNC METHOD: ATTENTION")

if source.count("return True") == 1:
    print("SYNC RETURN STRUCTURE: PASS")
else:
    print("SYNC RETURN STRUCTURE: ATTENTION")

print("=" * 100)
print("E.27.35 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

