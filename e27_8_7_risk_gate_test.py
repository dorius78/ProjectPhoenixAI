from Core.core_system import CoreSystem

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.8.7 RISK GATE DIAGNOSTIC")
print("=" * 100)

c = CoreSystem()

data = c.candles.get_candles(
    "BTC-USD",
    period="5d",
    interval="1h"
)

price = float(data["Close"].iloc[-1])

result = c.analysis.analyze(
    data,
    price,
    "BTC-USD",
    c.portfolio.get_balance()
)

print()
print("PRICE:", price)

print()
print("========== RISK ==========")

risk = result["risk"]

for key, value in risk.items():
    print(f"{key}: {value}")

print()
print("========== DECISION ==========")

decision = result["decision"]

print("ACTION:", decision.get("action"))
print("SCORE:", decision.get("score"))
print("CONFIDENCE:", decision.get("confidence"))
print("DOMINANT:", decision.get("dominant_direction"))
print("CONFLICT:", decision.get("conflict"))
print("BULLISH:", decision.get("bullish_score"))
print("BEARISH:", decision.get("bearish_score"))

print()
print("========== SIGNAL ==========")

signal = result["signal"]

print("VALID:", signal.get("valid"))
print("SIGNAL:", signal.get("signal"))
print("REJECTION:", signal.get("rejection_reason"))

print()
print("========== TRADE ==========")

print("TRADE:", result["trade"])

print()
print("=" * 100)
print("E.27.8.7 COMPLETATO")
print("NESSUNA MODIFICA")
print("NESSUN ORDINE MT5 INVIATO")
print("=" * 100)
