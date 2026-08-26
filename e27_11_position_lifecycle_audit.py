from Core.core_system import CoreSystem
import Config.settings as s

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.11 POSITION LIFECYCLE AUDIT")
print("=" * 100)

c = CoreSystem()
bridge = c.execution.mt5

assert bridge is not None

print()
print("MODE:", s.MODE)
print("MT5 SYMBOL:", s.MT5_SYMBOL)
print("MT5 ENABLED:", c.execution.mt5_enabled)

print()
print("1. CONNESSIONE MT5")
print("-" * 100)

connected = bridge.connect()
print("CONNECTED:", connected)

assert connected is True

print()
print("2. POSIZIONI PHOENIX")
print("-" * 100)

positions = bridge.get_phoenix_positions()

print("PHOENIX POSITIONS:", positions)
print("COUNT:", len(positions))

print()
print("3. POSIZIONI MT5 BTCUSD")
print("-" * 100)

import MetaTrader5 as mt5

mt5_positions = mt5.positions_get(
    symbol=s.MT5_SYMBOL
)

print("MT5 POSITIONS:", mt5_positions)

if mt5_positions:
    for p in mt5_positions:
        print()
        print("TICKET:", p.ticket)
        print("SYMBOL:", p.symbol)
        print("MAGIC:", p.magic)
        print("TYPE:", p.type)
        print("VOLUME:", p.volume)
        print("PRICE OPEN:", p.price_open)
        print("PRICE CURRENT:", p.price_current)
        print("SL:", p.sl)
        print("TP:", p.tp)
        print("PROFIT:", p.profit)
        print("COMMENT:", p.comment)

print()
print("=" * 100)
print("E.27.11 AUDIT COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUNA NUOVA APERTURA")
print("NESSUNA CHIUSURA INVIATA")
print("=" * 100)

bridge.disconnect()
