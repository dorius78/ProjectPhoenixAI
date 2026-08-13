from Core.trade_builder import TradeBuilder


class FakeRiskManager:

    def __init__(self, trade=None):
        self.trade = trade

    def build_trade(
        self,
        symbol,
        signal,
        current_price,
        atr,
        account_balance
    ):
        return self.trade


def test_hold_returns_none():

    builder = TradeBuilder()

    risk = FakeRiskManager()

    result = builder.build(
        risk_manager=risk,
        symbol="BTC-USD",
        price=100000,
        signal="HOLD",
        atr=2000,
        account_balance=10000
    )

    assert result is None


def test_buy_builds_trade():

    builder = TradeBuilder()

    risk = FakeRiskManager(
        trade={
            "entry": 100000,
            "size": 0.01
        }
    )

    result = builder.build(
        risk_manager=risk,
        symbol="BTC-USD",
        price=100000,
        signal="BUY",
        atr=2000,
        account_balance=10000
    )

    assert result is not None
    assert result["symbol"] == "BTC-USD"
    assert result["signal"] == "BUY"
    assert result["side"] == "BUY"


def test_strong_buy_becomes_buy():

    builder = TradeBuilder()

    risk = FakeRiskManager(
        trade={
            "entry": 100000,
            "size": 0.01
        }
    )

    result = builder.build(
        risk_manager=risk,
        symbol="BTC-USD",
        price=100000,
        signal="STRONG BUY",
        atr=2000,
        account_balance=10000
    )

    assert result["signal"] == "STRONG BUY"
    assert result["side"] == "BUY"


def test_strong_sell_becomes_sell():

    builder = TradeBuilder()

    risk = FakeRiskManager(
        trade={
            "entry": 100000,
            "size": 0.01
        }
    )

    result = builder.build(
        risk_manager=risk,
        symbol="BTC-USD",
        price=100000,
        signal="STRONG SELL",
        atr=2000,
        account_balance=10000
    )

    assert result["signal"] == "STRONG SELL"
    assert result["side"] == "SELL"


def test_risk_manager_can_reject_trade():

    builder = TradeBuilder()

    risk = FakeRiskManager(
        trade=None
    )

    result = builder.build(
        risk_manager=risk,
        symbol="BTC-USD",
        price=100000,
        signal="BUY",
        atr=2000,
        account_balance=10000
    )

    assert result is None
