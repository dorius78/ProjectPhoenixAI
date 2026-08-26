from Core.core_system import CoreSystem
import Config.settings as s

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.10.6 MT5 BRIDGE DRY RUN TEST")
print("=" * 100)

c = CoreSystem()

bridge = c.execution.mt5

assert bridge is not None, "STOP: bridge MT5 assente"

print("MODE:", s.MODE)
print("MT5 ENABLED:", c.execution.mt5_enabled)
print("DRY RUN ENGINE:", c.execution.mt5_dry_run)

print()
print("1. CONNESSIONE")
connected = bridge.connect()
print("CONNECTED:", connected)
assert connected is True

print()
print("2. TEST VOLUME")

symbol = s.MT5_SYMBOL

for size in [0.01, 0.1, 0.2, 1.0]:
    volume = bridge._to_volume(symbol, size)
    print(f"Phoenix units {size} -> MT5 volume {volume}")
    assert volume is not None
    assert volume > 0

print()
print("3. TEST DRY RUN")

trade = {
    "symbol": "BTC-USD",
    "side": "BUY",
    "entry": 77200.0,
    "stop_loss": 76700.0,
    "take_profit": 78200.0,
    "size": 0.2,
    "signal": "STRONG BUY"
}

result = bridge.execute(
    trade,
    dry_run=True
)

print("RESULT:", result)

assert result.get("dry_run") is True
assert result.get("success") is False
assert result.get("executed", False) is False

print()
print("=" * 100)
print("E.27.10.6 PASS")
print("DRY RUN FUNZIONANTE")
print("NESSUN order_send ESEGUITO")
print("NESSUN ORDINE MT5 INVIATO")
print("=" * 100)

bridge.disconnect()
