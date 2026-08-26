import sys
sys.path.insert(0, '.')
from Execution.mt5_broker import MT5Broker
import MetaTrader5 as mt5

broker = MT5Broker()
if broker.connect():
    symbols = mt5.symbols_get()
    print()
    print("Totale simboli visti dall'account:", len(symbols))
    print()
    print("Simboli che contengono 'EUR':")
    for s in symbols:
        if "EUR" in s.name.upper():
            print(" -", repr(s.name))
    broker.disconnect()
