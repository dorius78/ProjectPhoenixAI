from Core.risk_manager import RiskManager
from Core.trade_builder import TradeBuilder

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.53 RISK GATE → TRADE CONTRACT TEST")
print("=" * 100)

risk = RiskManager()
builder = TradeBuilder()

account_balance = 10000.0
price = 100000.0
atr = 1000.0
symbol = "BTC-USD"

print()
print("1. BUY")
print("=" * 100)

trade_buy = builder.build(
    risk_manager=risk,
    symbol=symbol,
    price=price,
    signal="BUY",
    atr=atr,
    account_balance=account_balance
)

print("TRADE BUY:")
print(trade_buy)

print()
print("2. SELL")
print("=" * 100)

trade_sell = builder.build(
    risk_manager=risk,
    symbol=symbol,
    price=price,
    signal="SELL",
    atr=atr,
    account_balance=account_balance
)

print("TRADE SELL:")
print(trade_sell)

print()
print("3. HOLD")
print("=" * 100)

trade_hold = builder.build(
    risk_manager=risk,
    symbol=symbol,
    price=price,
    signal="HOLD",
    atr=atr,
    account_balance=account_balance
)

print("TRADE HOLD:")
print(trade_hold)

print()
print("4. INVALID SIGNAL")
print("=" * 100)

trade_invalid = builder.build(
    risk_manager=risk,
    symbol=symbol,
    price=price,
    signal="INVALID",
    atr=atr,
    account_balance=account_balance
)

print("TRADE INVALID:")
print(trade_invalid)

print()
print("5. CONTRACT CHECK")
print("=" * 100)

required_keys = [
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

if trade_buy is not None:

    for key in required_keys:

        print(
            f"{key:20} = "
            f"{'PASS' if key in trade_buy else 'FAIL'}"
        )

print()
print("=" * 100)
print("E.27.53 TEST COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

