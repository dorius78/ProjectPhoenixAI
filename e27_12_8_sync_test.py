from Core.core_system import CoreSystem
import Config.settings as s

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.8 MT5 -> PHOENIX SYNC TEST")
print("=" * 100)

c = CoreSystem()

bridge = c.execution.mt5
live = c.live_engine

assert bridge is not None, "STOP: MT5 bridge assente"
assert live is not None, "STOP: Live Trading Engine assente"

print()
print("MODE:", s.MODE)
print("MT5 ENABLED:", c.execution.mt5_enabled)
print("MT5 SYMBOL:", s.MT5_SYMBOL)

print()
print("1. CONNESSIONE")
print("-" * 100)

assert bridge.connect() is True

print("CONNECTED: True")

print()
print("2. POSIZIONI MT5 PHOENIX")
print("-" * 100)

mt5_positions = bridge.get_phoenix_positions()

print("COUNT MT5:", len(mt5_positions))

for p in mt5_positions:
    print(
        "TICKET:", p.ticket,
        "| SYMBOL:", p.symbol,
        "| TYPE:", p.type,
        "| VOLUME:", p.volume,
        "| ENTRY:", p.price_open,
        "| SL:", p.sl,
        "| TP:", p.tp,
        "| PROFIT:", p.profit,
        "| MAGIC:", p.magic
    )

assert len(mt5_positions) == 1, (
    "STOP: attesa esattamente una posizione Phoenix MT5"
)

print()
print("3. STATO POSITION CONTROLLER PRIMA")
print("-" * 100)

before = live.position_controller.get_position()

print("POSITION CONTROLLER:", before)

print()
print("4. SINCRONIZZAZIONE")
print("-" * 100)

result = live._sync_mt5_position()

print("SYNC RESULT:", result)

print()
print("5. STATO POSITION CONTROLLER DOPO")
print("-" * 100)

after = live.position_controller.get_position()

print("POSITION CONTROLLER:", after)

assert result is True, "STOP: sincronizzazione non riuscita"
assert after is not None, "STOP: posizione Phoenix non creata"

assert after.get("mt5_ticket") == mt5_positions[0].ticket
assert after.get("mt5_symbol") == mt5_positions[0].symbol
assert after.get("magic") == mt5_positions[0].magic

print()
print("=" * 100)
print("E.27.12.8 PASS")
print("MT5 -> PHOENIX SINCRONIZZAZIONE RIUSCITA")
print("TICKET:", after.get("mt5_ticket"))
print("SYMBOL:", after.get("mt5_symbol"))
print("MAGIC:", after.get("magic"))
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

bridge.disconnect()

