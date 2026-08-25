from Core.exit_manager import ExitManager


def test_buy_stop_loss():

    manager = ExitManager()

    position = {
        "symbol": "BTC-USD",
        "side": "BUY",
        "entry": 100000.0,
        "stop_loss": 99000.0,
        "take_profit": 102000.0,
        "size": 0.01,
        "status": "OPEN"
    }

    result = manager.evaluate(
        position,
        98900.0
    )

    assert result == "STOP LOSS"


def test_buy_take_profit():

    manager = ExitManager()

    position = {
        "symbol": "BTC-USD",
        "side": "BUY",
        "entry": 100000.0,
        "stop_loss": 99000.0,
        "take_profit": 102000.0,
        "size": 0.01,
        "status": "OPEN"
    }

    result = manager.evaluate(
        position,
        102100.0
    )

    assert result == "TAKE PROFIT"


def test_sell_stop_loss():

    manager = ExitManager()

    position = {
        "symbol": "BTC-USD",
        "side": "SELL",
        "entry": 100000.0,
        "stop_loss": 101000.0,
        "take_profit": 98000.0,
        "size": 0.01,
        "status": "OPEN"
    }

    result = manager.evaluate(
        position,
        101100.0
    )

    assert result == "STOP LOSS"


def test_sell_take_profit():

    manager = ExitManager()

    position = {
        "symbol": "BTC-USD",
        "side": "SELL",
        "entry": 100000.0,
        "stop_loss": 101000.0,
        "take_profit": 98000.0,
        "size": 0.01,
        "status": "OPEN"
    }

    result = manager.evaluate(
        position,
        97900.0
    )

    assert result == "TAKE PROFIT"


def test_break_even_buy():

    manager = ExitManager()

    position = {
        "symbol": "BTC-USD",
        "side": "BUY",
        "entry": 100000.0,
        "stop_loss": 99000.0,
        "take_profit": 102000.0,
        "size": 0.01,
        "status": "OPEN",
        "break_even": False
    }

    result = manager.apply_break_even(
        position,
        101000.0
    )

    assert result["stop_loss"] == 100000.0
    assert result["break_even"] is True


def test_break_even_sell():

    manager = ExitManager()

    position = {
        "symbol": "BTC-USD",
        "side": "SELL",
        "entry": 100000.0,
        "stop_loss": 101000.0,
        "take_profit": 98000.0,
        "size": 0.01,
        "status": "OPEN",
        "break_even": False
    }

    result = manager.apply_break_even(
        position,
        99000.0
    )

    assert result["stop_loss"] == 100000.0
    assert result["break_even"] is True


def test_break_even_not_activated_in_loss():

    manager = ExitManager()

    position = {
        "symbol": "BTC-USD",
        "side": "BUY",
        "entry": 100000.0,
        "stop_loss": 99000.0,
        "take_profit": 102000.0,
        "size": 0.01,
        "status": "OPEN",
        "break_even": False
    }

    result = manager.apply_break_even(
        position,
        99500.0
    )

    assert result["stop_loss"] == 99000.0
    assert result["break_even"] is False


def test_trailing_stop_buy():

    manager = ExitManager()

    position = {
        "symbol": "BTC-USD",
        "side": "BUY",
        "entry": 100000.0,
        "stop_loss": 100000.0,
        "take_profit": 102000.0,
        "size": 0.01,
        "status": "OPEN",
        "break_even": True
    }

    result = manager.apply_trailing_stop(
        position,
        101500.0
    )

    assert result["stop_loss"] == 101000.0
    assert result["break_even"] is True


def test_trailing_stop_sell():

    manager = ExitManager()

    position = {
        "symbol": "BTC-USD",
        "side": "SELL",
        "entry": 100000.0,
        "stop_loss": 100000.0,
        "take_profit": 98000.0,
        "size": 0.01,
        "status": "OPEN",
        "break_even": True
    }

    result = manager.apply_trailing_stop(
        position,
        98500.0
    )

    assert result["stop_loss"] == 99000.0
    assert result["break_even"] is True


def test_trailing_stop_buy_does_not_move_backward():

    manager = ExitManager()

    position = {
        "symbol": "BTC-USD",
        "side": "BUY",
        "entry": 100000.0,
        "stop_loss": 101000.0,
        "take_profit": 102000.0,
        "size": 0.01,
        "status": "OPEN",
        "break_even": True
    }

    result = manager.apply_trailing_stop(
        position,
        100500.0
    )

    assert result["stop_loss"] == 101000.0
    assert result["break_even"] is True


def test_trailing_stop_sell_does_not_move_backward():

    manager = ExitManager()

    position = {
        "symbol": "BTC-USD",
        "side": "SELL",
        "entry": 100000.0,
        "stop_loss": 99000.0,
        "take_profit": 98000.0,
        "size": 0.01,
        "status": "OPEN",
        "break_even": True
    }

    result = manager.apply_trailing_stop(
        position,
        99500.0
    )

    assert result["stop_loss"] == 99000.0
    assert result["break_even"] is True


if __name__ == "__main__":

    test_buy_stop_loss()
    test_buy_take_profit()
    test_sell_stop_loss()
    test_sell_take_profit()

    test_break_even_buy()
    test_break_even_sell()
    test_break_even_not_activated_in_loss()

    test_trailing_stop_buy()
    test_trailing_stop_sell()
    test_trailing_stop_buy_does_not_move_backward()
    test_trailing_stop_sell_does_not_move_backward()

    print("TEST EXIT MANAGER: OK")
def test_buy_intrabar_stop_loss():

    manager = ExitManager()

    position = {
        "symbol": "BTC-USD",
        "side": "BUY",
        "entry": 100000.0,
        "stop_loss": 99000.0,
        "take_profit": 102000.0,
        "size": 0.01,
        "status": "OPEN",
        "break_even": True
    }

    result = manager.evaluate(
        position,
        100500.0,
        high=101000.0,
        low=98900.0
    )

    assert result == "STOP LOSS"


def test_buy_intrabar_take_profit():

    manager = ExitManager()

    position = {
        "symbol": "BTC-USD",
        "side": "BUY",
        "entry": 100000.0,
        "stop_loss": 99000.0,
        "take_profit": 102000.0,
        "size": 0.01,
        "status": "OPEN",
        "break_even": True
    }

    result = manager.evaluate(
        position,
        101500.0,
        high=102100.0,
        low=100500.0
    )

    assert result == "TAKE PROFIT"


def test_sell_intrabar_stop_loss():

    manager = ExitManager()

    position = {
        "symbol": "BTC-USD",
        "side": "SELL",
        "entry": 100000.0,
        "stop_loss": 101000.0,
        "take_profit": 98000.0,
        "size": 0.01,
        "status": "OPEN",
        "break_even": True
    }

    result = manager.evaluate(
        position,
        100500.0,
        high=101100.0,
        low=99500.0
    )

    assert result == "STOP LOSS"


def test_sell_intrabar_take_profit():

    manager = ExitManager()

    position = {
        "symbol": "BTC-USD",
        "side": "SELL",
        "entry": 100000.0,
        "stop_loss": 101000.0,
        "take_profit": 98000.0,
        "size": 0.01,
        "status": "OPEN",
        "break_even": True
    }

    result = manager.evaluate(
        position,
        98500.0,
        high=99500.0,
        low=97900.0
    )

    assert result == "TAKE PROFIT"


def test_buy_intrabar_stop_loss_has_priority_over_take_profit():

    manager = ExitManager()

    position = {
        "symbol": "BTC-USD",
        "side": "BUY",
        "entry": 100000.0,
        "stop_loss": 99000.0,
        "take_profit": 102000.0,
        "size": 0.01,
        "status": "OPEN",
        "break_even": True
    }

    result = manager.evaluate(
        position,
        100000.0,
        high=102500.0,
        low=98500.0
    )

    assert result == "STOP LOSS"


def test_sell_intrabar_stop_loss_has_priority_over_take_profit():

    manager = ExitManager()

    position = {
        "symbol": "BTC-USD",
        "side": "SELL",
        "entry": 100000.0,
        "stop_loss": 101000.0,
        "take_profit": 98000.0,
        "size": 0.01,
        "status": "OPEN",
        "break_even": True
    }

    result = manager.evaluate(
        position,
        100000.0,
        high=101500.0,
        low=97500.0
    )

    assert result == "STOP LOSS"

from Core.exit_manager import ExitManager
