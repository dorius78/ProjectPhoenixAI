from Core.core_system import CoreSystem
import Config.settings as s
import MetaTrader5 as mt5
import time

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.11.3 REAL DEMO CLOSE")
print("=" * 100)

c = CoreSystem()
bridge = c.execution.mt5

assert bridge is not None
assert s.MODE == "DEMO"

print()
print("MODE:", s.MODE)
print("MT5 SYMBOL:", s.MT5_SYMBOL)

print()
print("1. CONNESSIONE")
print("-" * 100)

assert bridge.connect() is True
print("CONNECTED: True")

print()
print("2. RICERCA POSIZIONI PHOENIX")
print("-" * 100)

positions = bridge.get_phoenix_positions()

print("COUNT:", len(positions))

assert len(positions) == 1, (
    f"STOP SICURO: attese 1 posizione Phoenix, trovate {len(positions)}"
)

position = positions[0]

print("TICKET:", position.ticket)
print("SYMBOL:", position.symbol)
print("MAGIC:", position.magic)
print("TYPE:", position.type)
print("VOLUME:", position.volume)
print("OPEN:", position.price_open)
print("CURRENT:", position.price_current)
print("SL:", position.sl)
print("TP:", position.tp)
print("PROFIT:", position.profit)
print("COMMENT:", position.comment)

assert position.magic == bridge.magic
assert position.symbol == s.MT5_SYMBOL
assert position.volume > 0

ticket = position.ticket
volume = position.volume

print()
print("3. PREPARAZIONE CHIUSURA")
print("-" * 100)

tick = mt5.symbol_info_tick(position.symbol)

assert tick is not None

if position.type == mt5.POSITION_TYPE_BUY:
    close_type = mt5.ORDER_TYPE_SELL
    price = float(tick.bid)
else:
    close_type = mt5.ORDER_TYPE_BUY
    price = float(tick.ask)

request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": position.symbol,
    "volume": float(volume),
    "type": close_type,
    "position": int(ticket),
    "price": price,
    "deviation": 20,
    "magic": bridge.magic,
    "comment": "PROJECT PHOENIX AI CLOSE",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": bridge.get_filling_mode(),
}

print("REQUEST:", request)

print()
print("4. ORDER CHECK")
print("-" * 100)

check = mt5.order_check(request)

print("CHECK:", check)

assert check is not None
assert check.retcode == 0, (
    f"STOP: order_check non superato: {check}"
)

print()
print("ORDER CHECK: PASS")

print()
print("5. CHIUSURA REALE DEMO")
print("-" * 100)

print("INVIO order_send...")
result = mt5.order_send(request)

print()
print("RESULT:", result)

assert result is not None

print()
print("RETCODE:", result.retcode)
print("DEAL:", result.deal)
print("ORDER:", result.order)
print("VOLUME:", result.volume)
print("PRICE:", result.price)
print("COMMENT:", result.comment)

assert result.retcode == mt5.TRADE_RETCODE_DONE, (
    f"STOP: chiusura rifiutata: {result}"
)

print()
print("6. VERIFICA POSIZIONE")
print("-" * 100)

time.sleep(2)

remaining = mt5.positions_get(
    ticket=int(ticket)
)

print("POSIZIONE DOPO CHIUSURA:", remaining)

assert not remaining, (
    f"STOP: la posizione {ticket} risulta ancora aperta: {remaining}"
)

print()
print("=" * 100)
print("E.27.11.3 PASS")
print("CHIUSURA REALE DEMO ESEGUITA")
print(f"TICKET CHIUSO: {ticket}")
print(f"DEAL: {result.deal}")
print(f"PRICE CLOSE: {result.price}")
print("POSIZIONE NON PIU' PRESENTE SU MT5")
print("=" * 100)

bridge.disconnect()
