import pandas as pd

from MT5_Bridge.mt5_bridge import MT5DataBridge
from Core.analysis_engine import AnalysisEngine
from Core.risk_manager import RiskManager
from Core.trade_manager import TradeManager


SYMBOL = "EURUSD"
TIMEFRAME = "M5"
ACCOUNT_BALANCE = 49872.27


print()
print("=" * 70)
print(" PROJECT PHOENIX AI - LIVE DEMO PIPELINE")
print("=" * 70)

print()
print("[1] Connessione MT5...")

bridge = MT5DataBridge(SYMBOL, TIMEFRAME)

if not bridge.connect():
    raise RuntimeError("Impossibile collegarsi a MT5")

print("[OK] MT5 collegato.")

print()
print("[2] Acquisizione mercato...")

candles = bridge.candles(200)

if not candles:
    bridge.disconnect()
    raise RuntimeError("Nessuna candela ricevuta da MT5")

data = pd.DataFrame(candles)

tick = bridge.tick()

if tick is None:
    bridge.disconnect()
    raise RuntimeError("Nessun tick ricevuto")

price = float(tick["bid"])

print(f"[OK] Candele: {len(data)}")
print(f"[OK] Prezzo: {price}")

bridge.disconnect()

print()
print("[3] Analisi Phoenix...")

analysis_engine = AnalysisEngine()

analysis = analysis_engine.analyze(
    data,
    price,
    SYMBOL,
    ACCOUNT_BALANCE
)

signal_data = analysis.get("signal", {})

print()
print(f"SIGNAL     : {signal_data.get('signal')}")
print(f"CONFIDENCE : {signal_data.get('confidence')}")
print(f"SCORE      : {signal_data.get('score')}")
print(f"DIRECTION  : {signal_data.get('dominant_direction')}")

print()
print("[4] Risk Manager...")

risk_manager = RiskManager()

risk_result = risk_manager.evaluate(analysis)

print("RISK RESULT:")
print(risk_result)

print()
print("[5] Trade Manager...")

trade_manager = TradeManager()

signal = signal_data.get("signal")
atr = analysis.get("indicators", {}).get("ATR")

if atr is None:
    atr = 0.001

trade = trade_manager.generate_trade(
    SYMBOL,
    price,
    signal,
    float(atr),
    ACCOUNT_BALANCE
)

print()
print("TRADE RESULT:")
print(trade)

print()
print("=" * 70)
print(" PHOENIX LIVE DEMO PIPELINE COMPLETATA")
print("=" * 70)
print()
print("ORDINI MT5: DISABILITATI")
print("NESSUN ORDINE REALE INVIATO")
print()
