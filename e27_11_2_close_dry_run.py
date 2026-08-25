from Core.core_system import CoreSystem
import Config.settings as s

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.11.2 CLOSE POSITION DRY RUN")
print("=" * 100)

c = CoreSystem()
bridge = c.execution.mt5

assert bridge is not None
assert bridge.connect() is True

print()
print("1. POSIZIONI PHOENIX")
print("-" * 100)

positions = bridge.get_phoenix_positions()

print("COUNT:", len(positions))

for p in positions:
    print()
    print("TICKET:", p.ticket)
    print("SYMBOL:", p.symbol)
    print("TYPE:", p.type)
    print("VOLUME:", p.volume)
    print("PRICE OPEN:", p.price_open)
    print("PRICE CURRENT:", p.price_current)
    print("SL:", p.sl)
    print("TP:", p.tp)
    print("PROFIT:", p.profit)
    print("MAGIC:", p.magic)

assert len(positions) == 1

position = positions[0]

print()
print("2. CLOSE POSITION DRY RUN")
print("-" * 100)

result = bridge.close_position(
    position,
    dry_run=True
)

print("RESULT:", result)

print()
print("EXECUTED:", result.get("executed"))
print("DRY RUN:", result.get("dry_run"))
print("MESSAGE:", result.get("message"))
print("ORDER:", result.get("order"))

assert result.get("executed") is False
assert result.get("dry_run") is True
assert result.get("order") is not None

print()
print("=" * 100)
print("E.27.11.2 PASS")
print("CHIUSURA PREPARATA CORRETTAMENTE")
print("NESSUN order_send")
print("NESSUNA CHIUSURA MT5")
print("=" * 100)

bridge.disconnect()
