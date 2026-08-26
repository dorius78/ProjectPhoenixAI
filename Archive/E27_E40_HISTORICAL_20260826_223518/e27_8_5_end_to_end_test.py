from Core.core_system import CoreSystem
import Config.settings as s

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.8.5 END-TO-END MT5 PRE-EXECUTION TEST")
print("=" * 100)

c = CoreSystem()

print("MODE:", s.MODE)
print("MT5 SYMBOL:", s.MT5_SYMBOL)
print("MT5 ENABLED:", c.execution.mt5_enabled)
print("DRY RUN:", c.execution.mt5_dry_run)

assert s.MODE == "DEMO"
assert c.execution.mt5_enabled is True
assert c.execution.mt5 is not None

print()
print("1. CONNESSIONE MT5")
connected = c.execution.connect_mt5()
print("CONNECTED:", connected)

assert connected is True

print()
print("2. ACCOUNT")
bridge = c.execution.mt5

account = bridge.account_info()

print("ACCOUNT:", account)

print()
print("3. TICK")
tick = bridge.tick()

print("TICK:", tick)

print()
print("4. DATI MERCATO")
data = c.candles.get_candles(
    "BTC-USD",
    period="5d",
    interval="1h"
)

price = float(data["Close"].iloc[-1])

print("PRICE:", price)

print()
print("5. ANALISI")
result = c.analysis.analyze(
    data,
    price,
    "BTC-USD",
    c.portfolio.get_balance()
)

decision = result["decision"]
signal = result["signal"]
trade = result["trade"]

print("SIGNAL VALID:", signal.get("valid"))
print("SIGNAL:", signal.get("signal"))
print("SCORE:", signal.get("score"))
print("CONFIDENCE:", signal.get("confidence"))
print("DOMINANT:", signal.get("dominant_direction"))
print("CONFLICT:", signal.get("conflict"))
print("REJECTION:", signal.get("rejection_reason"))

print()
print("6. TRADE")
print("TRADE:", trade)

if trade is None:
    print()
    print("NESSUN TRADE GENERATO.")
    print("IL BLOCCO E' PRIMA DELLA FASE MT5.")
else:
    print()
    print("7. PREPARE ORDER")
    prepared = bridge.prepare_order(trade)

    print("PREPARED:", prepared)

    print()
    print("8. ORDER CHECK")
    if prepared.get("valid"):
        checked = bridge.check_order(trade)
        print("CHECKED:", checked)
    else:
        print("ORDER NON PREPARATO.")

print()
print("=" * 100)
print("E.27.8.5 COMPLETATO")
print("NESSUN order_send ESEGUITO")
print("NESSUN ORDINE MT5 INVIATO")
print("=" * 100)

bridge.disconnect()
