import MetaTrader5 as mt5

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.23 MT5 RESULT OBJECT CONTRACT")
print("=" * 100)

if not mt5.initialize():
    print("ERRORE MT5:", mt5.last_error())
    raise SystemExit(1)

print()
print("MT5 VERSION")
print("-" * 100)
print(mt5.version())

print()
print("RESULT OBJECT ATTRIBUTES")
print("-" * 100)

result_type = getattr(mt5, "OrderSendResult", None)

print("OrderSendResult:", result_type)

if result_type is not None:
    fields = [
        "retcode",
        "deal",
        "order",
        "volume",
        "price",
        "bid",
        "ask",
        "comment",
        "request_id",
        "retcode_external",
    ]

    for field in fields:
        print(
            f"{field:20} = "
            f"{hasattr(result_type, field)}"
        )

print()
print("NESSUNA ISTANZA DI ORDINE CREATA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")

print()
print("=" * 100)
print("E.27.12.23 AUDIT COMPLETATO")
print("=" * 100)

mt5.shutdown()

