import pandas as pd

from Core.analysis_engine import AnalysisEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.42 END-TO-END BEHAVIORAL TEST")
print("=" * 100)

rows = 150

data = pd.DataFrame({

    "Open": [
        100000 + i * 20
        for i in range(rows)
    ],

    "High": [
        100500 + i * 20
        for i in range(rows)
    ],

    "Low": [
        99500 + i * 20
        for i in range(rows)
    ],

    "Close": [
        100000 + i * 20
        for i in range(rows)
    ],

    "Volume": [
        1000 + i * 10
        for i in range(rows)
    ]

})

price = float(
    data["Close"].iloc[-1]
)

engine = AnalysisEngine()

result = engine.analyze(
    data=data,
    price=price,
    symbol="BTC-USD",
    account_balance=10000.0
)

print()
print("=" * 100)
print("1. ANALYSIS")
print("=" * 100)

analysis = result["analysis"]

for key, value in analysis.items():
    print(
        f"{key:30} = {value}"
    )

print()
print("=" * 100)
print("2. RISK")
print("=" * 100)

risk = result["risk"]

for key, value in risk.items():
    print(
        f"{key:30} = {value}"
    )

print()
print("=" * 100)
print("3. DECISION")
print("=" * 100)

decision = result["decision"]

for key, value in decision.items():
    print(
        f"{key:30} = {value}"
    )

print()
print("=" * 100)
print("4. SIGNAL")
print("=" * 100)

signal = result["signal"]

for key, value in signal.items():
    print(
        f"{key:30} = {value}"
    )

print()
print("=" * 100)
print("5. TRADE")
print("=" * 100)

trade = result["trade"]

print(
    "TRADE:",
    trade
)

print()
print("=" * 100)
print("6. END-TO-END CHECKS")
print("=" * 100)

checks = {

    "ANALYSIS_PRESENT":
        result["analysis"] is not None,

    "INDICATORS_PRESENT":
        result["indicators"] is not None,

    "RISK_PRESENT":
        result["risk"] is not None,

    "DECISION_PRESENT":
        result["decision"] is not None,

    "SIGNAL_PRESENT":
        result["signal"] is not None,

    "TRADE_CONTRACT_VALID":
        (
            trade is None
            or all(
                key in trade
                for key in [
                    "symbol",
                    "side",
                    "entry",
                    "stop_loss",
                    "take_profit",
                    "atr",
                    "risk_reward",
                    "risk_percent",
                    "account_balance",
                    "size",
                    "size_unit"
                ]
            )
        )

}

for name, passed in checks.items():

    print(
        f"{name:30} = "
        f"{'PASS' if passed else 'FAIL'}"
    )

print()
print("=" * 100)

if all(checks.values()):

    print(
        "E.27.42 END-TO-END STRUCTURE: PASS"
    )

else:

    print(
        "E.27.42 END-TO-END STRUCTURE: ATTENTION"
    )

print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

