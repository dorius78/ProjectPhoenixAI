import MetaTrader5 as mt5
import Config.settings as s

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.8.2 MT5 POSITION STATE AUDIT")
print("=" * 100)

if not mt5.initialize():
    print("ERRORE MT5:", mt5.last_error())
    raise SystemExit(1)

account = mt5.account_info()

print()
print("ACCOUNT")
print("-" * 100)

if account:
    print("LOGIN:", account.login)
    print("SERVER:", account.server)
    print("BALANCE:", account.balance)
    print("EQUITY:", account.equity)
    print("PROFIT:", account.profit)

print()
print("POSIZIONI PHOENIX ATTUALI")
print("-" * 100)

positions = mt5.positions_get()

if positions:
    phoenix = [
        p for p in positions
        if int(getattr(p, "magic", 0)) == 260813
    ]

    print("TOTALE POSIZIONI:", len(positions))
    print("POSIZIONI PHOENIX:", len(phoenix))

    for p in phoenix:
        print(
            "TICKET:", p.ticket,
            "| SYMBOL:", p.symbol,
            "| TYPE:", p.type,
            "| VOLUME:", p.volume,
            "| ENTRY:", p.price_open,
            "| CURRENT:", p.price_current,
            "| SL:", p.sl,
            "| TP:", p.tp,
            "| PROFIT:", p.profit,
            "| MAGIC:", p.magic
        )
else:
    print("NESSUNA POSIZIONE MT5 APERTA")

print()
print("DEAL RECENTI MAGIC 260813")
print("-" * 100)

from datetime import datetime, timedelta

date_to = datetime.now()
date_from = date_to - timedelta(days=2)

deals = mt5.history_deals_get(
    date_from,
    date_to
)

phoenix_deals = []

if deals:
    phoenix_deals = [
        d for d in deals
        if int(getattr(d, "magic", 0)) == 260813
    ]

print("DEAL PHOENIX:", len(phoenix_deals))

for d in phoenix_deals:
    print(
        "TICKET:", d.ticket,
        "| ORDER:", d.order,
        "| POSITION:", d.position_id,
        "| SYMBOL:", d.symbol,
        "| TYPE:", d.type,
        "| VOLUME:", d.volume,
        "| PRICE:", d.price,
        "| PROFIT:", d.profit,
        "| MAGIC:", d.magic,
        "| COMMENT:", d.comment
    )

print()
print("=" * 100)
print("E.27.12.8.2 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUNA NUOVA APERTURA")
print("NESSUNA CHIUSURA INVIATA")
print("=" * 100)

mt5.shutdown()
