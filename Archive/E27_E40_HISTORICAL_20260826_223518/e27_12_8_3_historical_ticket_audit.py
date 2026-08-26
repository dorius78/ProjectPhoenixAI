import MetaTrader5 as mt5
from datetime import datetime, timedelta

TICKET = 85562165
MAGIC = 260813

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.8.3 HISTORICAL TICKET AUDIT")
print("=" * 100)

if not mt5.initialize():
    print("ERRORE MT5:", mt5.last_error())
    raise SystemExit(1)

account = mt5.account_info()

print()
print("ACCOUNT")
print("-" * 100)

print("LOGIN:", account.login)
print("SERVER:", account.server)
print("BALANCE:", account.balance)
print("EQUITY:", account.equity)

date_to = datetime.now()
date_from = date_to - timedelta(days=30)

print()
print("RICERCA ORDINI STORICI")
print("-" * 100)

orders = mt5.history_orders_get(
    date_from,
    date_to
)

print("ORDINI TOTALI:", 0 if orders is None else len(orders))

if orders:

    phoenix_orders = [
        o for o in orders
        if int(getattr(o, "magic", 0)) == MAGIC
        or int(getattr(o, "ticket", 0)) == TICKET
        or int(getattr(o, "position_id", 0)) == TICKET
    ]

    print("ORDINI PHOENIX:", len(phoenix_orders))

    for o in phoenix_orders:
        print()
        print("ORDER:", o.ticket)
        print("POSITION ID:", getattr(o, "position_id", 0))
        print("SYMBOL:", o.symbol)
        print("TYPE:", o.type)
        print("STATE:", o.state)
        print("VOLUME:", o.volume_initial)
        print("PRICE:", o.price_open)
        print("SL:", o.sl)
        print("TP:", o.tp)
        print("MAGIC:", o.magic)
        print("COMMENT:", o.comment)

print()
print("RICERCA DEAL STORICI")
print("-" * 100)

deals = mt5.history_deals_get(
    date_from,
    date_to
)

print("DEAL TOTALI:", 0 if deals is None else len(deals))

if deals:

    phoenix_deals = [
        d for d in deals
        if int(getattr(d, "magic", 0)) == MAGIC
        or int(getattr(d, "position_id", 0)) == TICKET
        or int(getattr(d, "order", 0)) == TICKET
    ]

    print("DEAL PHOENIX:", len(phoenix_deals))

    for d in phoenix_deals:
        print()
        print("DEAL:", d.ticket)
        print("ORDER:", d.order)
        print("POSITION:", d.position_id)
        print("SYMBOL:", d.symbol)
        print("TYPE:", d.type)
        print("ENTRY:", d.entry)
        print("VOLUME:", d.volume)
        print("PRICE:", d.price)
        print("PROFIT:", d.profit)
        print("MAGIC:", d.magic)
        print("COMMENT:", d.comment)

print()
print("=" * 100)
print("E.27.12.8.3 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

mt5.shutdown()
