from Core.core_system import CoreSystem
import MetaTrader5 as mt5
import Config.settings as s

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.10.2 BTCUSD MT5 SYMBOL AUDIT")
print("=" * 100)

c = CoreSystem()

assert s.MODE == "DEMO"
assert c.execution.mt5 is not None

bridge = c.execution.mt5

print()
print("CONNESSIONE MT5")
print("-" * 100)

connected = bridge.connect()

print("CONNECTED:", connected)
assert connected is True

symbol = s.MT5_SYMBOL

print()
print("SIMBOLO:", symbol)
print("-" * 100)

info = mt5.symbol_info(symbol)

assert info is not None, f"SIMBOLO {symbol} NON TROVATO"

print("VISIBLE:", info.visible)
print("TRADE MODE:", info.trade_mode)
print("DIGITS:", info.digits)
print("POINT:", info.point)
print("CONTRACT SIZE:", info.trade_contract_size)
print("VOLUME MIN:", info.volume_min)
print("VOLUME MAX:", info.volume_max)
print("VOLUME STEP:", info.volume_step)
print("STOPS LEVEL:", info.trade_stops_level)
print("FREEZE LEVEL:", info.trade_freeze_level)
print("FILLING MODE:", info.filling_mode)

print()
print("TICK")
print("-" * 100)

tick = mt5.symbol_info_tick(symbol)

print("BID:", tick.bid)
print("ASK:", tick.ask)
print("LAST:", tick.last)

print()
print("CONVERSIONE PHOENIX")
print("-" * 100)

for size in [0.01, 0.1, 0.2, 1.0]:
    volume = bridge._to_volume(symbol, size)
    print(f"Phoenix units {size} -> MT5 volume {volume}")

print()
print("=" * 100)
print("E.27.10.2 COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN order_send")
print("NESSUN ORDINE MT5 INVIATO")
print("=" * 100)

bridge.disconnect()
