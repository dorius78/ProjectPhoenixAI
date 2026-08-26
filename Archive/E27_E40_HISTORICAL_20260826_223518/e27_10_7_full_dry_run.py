from Core.core_system import CoreSystem
import Config.settings as s

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.10.7 MT5 FULL DRY RUN")
print("=" * 100)

c = CoreSystem()

bridge = c.execution.mt5

assert bridge is not None
assert s.MODE == "DEMO"

print()
print("MODE:", s.MODE)
print("MT5 SYMBOL:", s.MT5_SYMBOL)

print()
print("1. CONNESSIONE MT5")
print("-" * 100)

assert bridge.connect() is True

print("CONNECTED: True")

print()
print("2. TRADE PHOENIX DI TEST")
print("-" * 100)

trade = {
    "symbol": "BTC-USD",
    "side": "BUY",
    "entry": 77200.0,
    "stop_loss": 76700.0,
    "take_profit": 78200.0,
    "size": 0.2,
    "signal": "STRONG BUY"
}

print("TRADE:", trade)

print()
print("3. PREPARE ORDER")
print("-" * 100)

prepared = bridge.prepare_order(trade)

print("PREPARED:", prepared)

print()
print("4. CHECK ORDER")
print("-" * 100)

checked = bridge.check_order(trade)

print("VALID:", checked.get("valid"))
print("CHECK:", checked.get("check"))
print("RISK GATE:", checked.get("risk_gate"))
print("ORDER:", checked.get("order"))

print()
print("5. DRY RUN")
print("-" * 100)

result = bridge.execute(
    trade,
    dry_run=True
)

print("EXECUTED:", result.get("executed"))
print("DRY RUN:", result.get("dry_run"))
print("MESSAGE:", result.get("message"))

assert result.get("dry_run") is True
assert result.get("executed") is False

print()
print("=" * 100)
print("E.27.10.7 PASS")
print("PIPELINE MT5 VERIFICATA IN DRY RUN")
print("NESSUN order_send ESEGUITO")
print("NESSUN ORDINE MT5 INVIATO")
print("=" * 100)

bridge.disconnect()
