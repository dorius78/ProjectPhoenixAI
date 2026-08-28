import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Core.risk_manager import RiskManager
from Core.risk_position_size import RiskPositionSize


def test_position_size_one_percent():
    calculator = RiskPositionSize()

    size = calculator.calculate(
        account_balance=10000,
        risk_percent=1,
        entry=100000,
        stop_loss=99000
    )

    assert size == 0.1


def test_position_size_zero_stop_distance():
    calculator = RiskPositionSize()

    size = calculator.calculate(
        account_balance=10000,
        risk_percent=1,
        entry=100000,
        stop_loss=100000
    )

    assert size == 0


def test_position_size_smaller_with_wider_stop():
    calculator = RiskPositionSize()

    close_stop = calculator.calculate(
        account_balance=10000,
        risk_percent=1,
        entry=100000,
        stop_loss=99000
    )

    wide_stop = calculator.calculate(
        account_balance=10000,
        risk_percent=1,
        entry=100000,
        stop_loss=98000
    )

    assert wide_stop < close_stop


def test_buy_trade():
    manager = RiskManager()

    trade = manager.build_trade(
        symbol="BTC-USD",
        signal="BUY",
        current_price=100000,
        atr=1000,
        account_balance=10000
    )

    assert trade is not None
    assert trade["symbol"] == "BTC-USD"
    assert trade["side"] == "BUY"
    assert trade["entry"] == 100000.0
    assert trade["stop_loss"] == 99000.0
    assert trade["take_profit"] == 102000.0
    assert trade["risk_reward"] == 2.0
    assert trade["size"] == 0.1


def test_sell_trade():
    manager = RiskManager()

    trade = manager.build_trade(
        symbol="BTC-USD",
        signal="SELL",
        current_price=100000,
        atr=1000,
        account_balance=10000
    )

    assert trade is not None
    assert trade["symbol"] == "BTC-USD"
    assert trade["side"] == "SELL"
    assert trade["entry"] == 100000.0
    assert trade["stop_loss"] == 101000.0
    assert trade["take_profit"] == 98000.0
    assert trade["risk_reward"] == 2.0
    assert trade["size"] == 0.1


def test_strong_buy_is_supported():
    manager = RiskManager()

    trade = manager.build_trade(
        symbol="BTC-USD",
        signal="STRONG BUY",
        current_price=100000,
        atr=1000,
        account_balance=10000
    )

    assert trade is not None
    assert trade["side"] == "BUY"


def test_strong_sell_is_supported():
    manager = RiskManager()

    trade = manager.build_trade(
        symbol="BTC-USD",
        signal="STRONG SELL",
        current_price=100000,
        atr=1000,
        account_balance=10000
    )

    assert trade is not None
    assert trade["side"] == "SELL"


def test_hold_does_not_create_trade():
    manager = RiskManager()

    trade = manager.build_trade(
        symbol="BTC-USD",
        signal="HOLD",
        current_price=100000,
        atr=1000,
        account_balance=10000
    )

    assert trade is None


def test_invalid_signal_does_not_create_trade():
    manager = RiskManager()

    trade = manager.build_trade(
        symbol="BTC-USD",
        signal="INVALID",
        current_price=100000,
        atr=1000,
        account_balance=10000
    )

    assert trade is None


if __name__ == "__main__":
    test_position_size_one_percent()
    test_position_size_zero_stop_distance()
    test_position_size_smaller_with_wider_stop()
    test_buy_trade()
    test_sell_trade()
    test_strong_buy_is_supported()
    test_strong_sell_is_supported()
    test_hold_does_not_create_trade()
    test_invalid_signal_does_not_create_trade()

    print("TEST RISK: OK")
