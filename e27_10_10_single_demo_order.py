from Core.core_system import CoreSystem
import Config.settings as s
import MetaTrader5 as mt5

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.10.10 SINGLE DEMO ORDER")
print("=" * 100)

c = CoreSystem()

assert s.MODE == "DEMO"
assert c.execution.mt5_enabled is True
assert c.execution.mt5 is not None

bridge = c.execution.mt5

print()
print("MODE:", s.MODE)
print("MT5 SYMBOL:", s.MT5_SYMBOL)

print()
print("1. CONNESSIONE MT5")
print("-" * 100)

assert bridge.connect() is True

account = bridge.account_info()
print("ACCOUNT:", account)

print()
print("2. PHOENIX ANALYSIS")
print("-" * 100)

data = c.candles.get_candles(
    "BTC-USD",
    period="5d",
    interval="1h"
)

price = float(data["Close"].iloc[-1])

result = c.analysis.analyze(
    data,
    price,
    "BTC-USD",
    c.portfolio.get_balance()
)

signal = result["signal"]
risk = result["risk"]
trade = result["trade"]

print("PRICE:", price)
print("SIGNAL:", signal)
print("RISK:", risk)
print("TRADE:", trade)

if trade is None:
    print()
    print("STOP: Phoenix non ha generato alcun trade.")
    bridge.disconnect()
    raise SystemExit(0)

print()
print("3. CONTROLLO POSIZIONI PHOENIX")
print("-" * 100)

positions = bridge.get_phoenix_positions()

print("POSIZIONI PHOENIX:", positions)

if positions:
    print()
    print("STOP SICURO: esiste già una posizione Phoenix.")
    print("Nessun nuovo ordine verrà inviato.")
    bridge.disconnect()
    raise SystemExit(0)

print()
print("4. CHECK ORDER")
print("-" * 100)

checked = bridge.check_order(trade)

print("VALID:", checked.get("valid"))
print("CHECK:", checked.get("check"))
print("RISK GATE:", checked.get("risk_gate"))
print("ORDER:", checked.get("order"))

assert checked.get("valid") is True

print()
print("5. ORDINE CHE VERRA' INVIATO")
print("-" * 100)

order = checked["order"]

for key, value in order.items():
    print(f"{key}: {value}")

print()
print("=" * 100)
print("ATTENZIONE")
print("=" * 100)
print("QUESTO E' UN ORDINE DEMO REALE SU METATRADER 5.")
print("NON E' DRY RUN.")
print("L'ORDINE VERRA' INVIATO SOLO DOPO CONFERMA MANUALE.")
print("=" * 100)

confirm = input(
    "DIGITA INVIA per inviare UN SOLO ORDINE DEMO: "
).strip()

if confirm != "INVIA":
    print()
    print("ORDINE ANNULLATO.")
    print("NESSUN order_send ESEGUITO.")
    bridge.disconnect()
    raise SystemExit(0)

print()
print("6. INVIO ORDINE DEMO")
print("-" * 100)

result_mt5 = mt5.order_send(order)

print("RESULT:", result_mt5)

if result_mt5 is None:
    print("ERRORE: nessuna risposta da MT5.")
else:
    print("RETCODE:", result_mt5.retcode)
    print("COMMENT:", result_mt5.comment)
    print("ORDER:", result_mt5.order)
    print("DEAL:", result_mt5.deal)
    print("PRICE:", result_mt5.price)
    print("VOLUME:", result_mt5.volume)

print()
print("7. VERIFICA POSIZIONE")
print("-" * 100)

mt5_symbol = s.MT5_SYMBOL

positions_after = mt5.positions_get(
    symbol=mt5_symbol
)

print("POSIZIONI MT5:", positions_after)

print()
print("=" * 100)
print("E.27.10.10 COMPLETATO")
print("=" * 100)

bridge.disconnect()

