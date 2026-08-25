from Core.trade_manager import TradeManager


def test_generate_trade_returns_trade():

    manager = TradeManager()

    result = manager.generate_trade(
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


def test_hold_returns_none():

    manager = TradeManager()

    result = manager.generate_trade(
        symbol="BTC-USD",
        price=100000,
        signal="HOLD",
        atr=2000,
        account_balance=10000
    )

    assert result is None


def test_strong_buy_is_supported():

    manager = TradeManager()

    result = manager.generate_trade(
        symbol="BTC-USD",
        price=100000,
        signal="STRONG BUY",
        atr=2000,
        account_balance=10000
    )

    assert result is not None
    assert result["signal"] == "STRONG BUY"
    assert result["side"] == "BUY"


def test_strong_sell_is_supported():

    manager = TradeManager()

    result = manager.generate_trade(
        symbol="BTC-USD",
        price=100000,
        signal="STRONG SELL",
        atr=2000,
        account_balance=10000
    )

    assert result is not None
    assert result["signal"] == "STRONG SELL"
    assert result["side"] == "SELL"


def test_summary_accepts_trade():

    manager = TradeManager()

    trade = {
        "symbol": "BTC-USD",
        "signal": "BUY",
        "side": "BUY",
        "entry": 100000,
        "size": 0.01
    }

    manager.summary(trade)


def test_reset_does_not_raise():

    manager = TradeManager()

    manager.reset()
