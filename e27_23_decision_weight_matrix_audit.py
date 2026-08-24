from Core.phoenix_brain_logic import PhoenixBrainLogic

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.23 DECISION WEIGHT MATRIX")
print("=" * 100)

logic = PhoenixBrainLogic()

weights = {
    "TREND": 20,
    "EMA": 10,
    "MACD": 10,
    "RSI": 15,
    "ADX": 10,
    "VOLUME": 10,
    "BOS": 15,
    "CHoCH": 10,
    "FVG": 8,
    "ORDER BLOCK": 10,
    "LIQUIDITY": 8,
}

print()
print("1. PESI ATTUALI")
print("-" * 100)

total = 0

for name, weight in weights.items():
    total += weight
    print(f"{name:20} = {weight:>3}")

print()
print(f"PESO MASSIMO TEORICO = {total}")

print()
print("2. DISTRIBUZIONE PERCENTUALE")
print("-" * 100)

for name, weight in weights.items():
    percentage = (weight / total) * 100
    print(
        f"{name:20} = "
        f"{weight:>3} "
        f"({percentage:6.2f}%)"
    )

print()
print("3. CATEGORIE")

technical = (
    weights["TREND"]
    + weights["EMA"]
    + weights["MACD"]
    + weights["RSI"]
    + weights["ADX"]
    + weights["VOLUME"]
)

smart_money = (
    weights["BOS"]
    + weights["CHoCH"]
    + weights["FVG"]
    + weights["ORDER BLOCK"]
    + weights["LIQUIDITY"]
)

print(
    f"TECHNICAL/MARKET = {technical}"
)

print(
    f"SMART MONEY      = {smart_money}"
)

print(
    f"TOTAL             = "
    f"{technical + smart_money}"
)

print()
print("4. OSSERVAZIONE")

if technical > smart_money:
    print(
        "Technical/Market ha un peso superiore "
        "a Smart Money."
    )

elif smart_money > technical:
    print(
        "Smart Money ha un peso superiore "
        "a Technical/Market."
    )

else:
    print(
        "Technical/Market e Smart Money "
        "hanno lo stesso peso."
    )

print()
print("=" * 100)
print("E.27.23 AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

