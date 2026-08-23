from Core.core_system import CoreSystem
import Config.settings as s

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.11 LIVE SYNC INTEGRATION AUDIT")
print("=" * 100)

c = CoreSystem()

live = c.live_engine
bridge = c.execution.mt5

assert live is not None
assert bridge is not None

print()
print("MODE:", s.MODE)
print("MT5 ENABLED:", c.execution.mt5_enabled)
print("MT5 SYMBOL:", s.MT5_SYMBOL)

print()
print("1. CONNESSIONE MT5")
print("-" * 100)

assert bridge.connect() is True

print("CONNECTED: True")

print()
print("2. POSIZIONI MT5 PHOENIX")
print("-" * 100)

positions = bridge.get_phoenix_positions()

print("COUNT:", len(positions))

for p in positions:
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

print()
print("3. POSITION CONTROLLER PRIMA")
print("-" * 100)

before = live.position_controller.get_position()

print("POSITION:", before)

print()
print("4. ESECUZIONE SYNC")
print("-" * 100)

sync_result = live._sync_mt5_position()

print("SYNC RESULT:", sync_result)

print()
print("5. POSITION CONTROLLER DOPO")
print("-" * 100)

after = live.position_controller.get_position()

print("POSITION:", after)

print()
print("6. VERIFICA INTEGRITA'")
print("-" * 100)

if positions:
    assert sync_result is True
    assert after is not None

    mt5 = positions[0]

    assert after.get("mt5_ticket") == mt5.ticket
    assert after.get("mt5_symbol") == mt5.symbol
    assert after.get("magic") == mt5.magic
    assert after.get("entry") == mt5.price_open
    assert after.get("size") == mt5.volume

    print("TICKET SYNC: OK")
    print("SYMBOL SYNC: OK")
    print("MAGIC SYNC: OK")
    print("ENTRY SYNC: OK")
    print("SIZE SYNC: OK")

else:
    print("ATTENZIONE: nessuna posizione Phoenix MT5 presente.")
    print("Sync correttamente non ha creato una posizione.")

print()
print("=" * 100)
print("E.27.12.11 AUDIT COMPLETATO")
print("NESSUN order_send")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

bridge.disconnect()
