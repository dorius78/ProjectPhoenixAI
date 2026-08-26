from Core.core_system import CoreSystem
import Config.settings as s

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.10.9 PHOENIX -> MT5 PRE-LIVE DEMO")
print("=" * 100)

c = CoreSystem()

assert s.MODE == "DEMO"
assert c.execution.mt5_enabled is True
assert c.execution.mt5 is not None

bridge = c.execution.mt5

print()
print("1. MT5")
print("-" * 100)

assert bridge.connect() is True

print("CONNECTED: True")
print("ACCOUNT:", bridge.account_info())

print()
print("2. MERCATO")
print("-" * 100)

data = c.candles.get_candles(
    "BTC-USD",
    period="5d",
    interval="1h"
)

price = float(data["Close"].iloc[-1])

print("PRICE:", price)

print()
print("3. PHOENIX ANALYSIS")
print("-" * 100)

result = c.analysis.analyze(
    data,
    price,
    "BTC-USD",
    c.portfolio.get_balance()
)

signal = result["signal"]
risk = result["risk"]
trade = result["trade"]

print("SIGNAL:", signal)
print("RISK:", risk)
print("TRADE:", trade)

if trade is None:
    print()
    print("NESSUN TRADE GENERATO.")
    print("STOP SICURO: nessun ordine possibile.")
else:

    print()
    print("4. MT5 CHECK ORDER")
    print("-" * 100)

    checked = bridge.check_order(trade)

    print("VALID:", checked.get("valid"))
    print("CHECK:", checked.get("check"))
    print("RISK GATE:", checked.get("risk_gate"))
    print("ORDER:", checked.get("order"))

    assert checked.get("valid") is True

    print()
    print("5. RISULTATO")
    print("-" * 100)
    print("ORDER MT5 PREPARATO E VALIDATO.")
    print("NESSUN order_send ESEGUITO.")

print()
print("=" * 100)
print("E.27.10.9 PASS")
print("PHOENIX -> MT5 VALIDAZIONE COMPLETATA")
print("NESSUN ORDINE INVIATO")
print("=" * 100)

bridge.disconnect()
