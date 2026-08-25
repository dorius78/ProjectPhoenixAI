from Execution.execution_engine import ExecutionEngine


def test_buy_execution():

    engine = ExecutionEngine()

    trade = {
        "symbol": "BTC-USD",
        "signal": "BUY",
        "side": "BUY",
        "entry": 100000.0,
        "stop_loss": 99000.0,
        "take_profit": 102000.0,
        "risk_reward": 2.0,
        "size": 0.1
    }

    order = engine.execute(trade)

    assert order["success"] is True
    assert order["symbol"] == "BTC-USD"
    assert order["side"] == "BUY"
    assert order["signal"] == "BUY"
    assert order["entry"] == 100000.0
    assert order["stop_loss"] == 99000.0
    assert order["take_profit"] == 102000.0
    assert order["risk_reward"] == 2.0
    assert order["size"] == 0.1
    assert order["status"] == "OPEN"


def test_sell_execution():

    engine = ExecutionEngine()

    trade = {
        "symbol": "BTC-USD",
        "signal": "SELL",
        "side": "SELL",
        "entry": 100000.0,
        "stop_loss": 101000.0,
        "take_profit": 98000.0,
        "risk_reward": 2.0,
        "size": 0.1
    }

    order = engine.execute(trade)

    assert order["success"] is True
    assert order["symbol"] == "BTC-USD"
    assert order["side"] == "SELL"
    assert order["signal"] == "SELL"
    assert order["size"] == 0.1
    assert order["status"] == "OPEN"


def test_strong_buy_execution():

    engine = ExecutionEngine()

    trade = {
        "symbol": "BTC-USD",
        "signal": "STRONG BUY",
        "entry": 100000.0,
        "stop_loss": 99000.0,
        "take_profit": 102000.0,
        "risk_reward": 2.0,
        "size": 0.1
    }

    order = engine.execute(trade)

    assert order["success"] is True
    assert order["signal"] == "STRONG BUY"
    assert order["side"] == "BUY"


def test_strong_sell_execution():

    engine = ExecutionEngine()

    trade = {
        "symbol": "BTC-USD",
        "signal": "STRONG SELL",
        "entry": 100000.0,
        "stop_loss": 101000.0,
        "take_profit": 98000.0,
        "risk_reward": 2.0,
        "size": 0.1
    }

    order = engine.execute(trade)

    assert order["success"] is True
    assert order["signal"] == "STRONG SELL"
    assert order["side"] == "SELL"


def test_hold_is_rejected():

    engine = ExecutionEngine()

    trade = {
        "symbol": "BTC-USD",
        "signal": "HOLD",
        "entry": 100000.0,
        "stop_loss": 99000.0,
        "take_profit": 102000.0,
        "risk_reward": 2.0,
        "size": 0.1
    }

    result = engine.execute(trade)

    assert result["success"] is False
    assert result["reason"] == "Segnale HOLD"


def test_invalid_signal_is_rejected():

    engine = ExecutionEngine()

    trade = {
        "symbol": "BTC-USD",
        "signal": "INVALID",
        "entry": 100000.0,
        "stop_loss": 99000.0,
        "take_profit": 102000.0,
        "risk_reward": 2.0,
        "size": 0.1
    }

    result = engine.execute(trade)

    assert result["success"] is False
    assert result["reason"] == "Segnale non valido"


def test_close_execution_report():

    engine = ExecutionEngine()

    closed_position = {
        "symbol": "BTC-USD",
        "side": "BUY",
        "entry": 100000.0,
        "current_price": 102000.0,
        "stop_loss": 99000.0,
        "take_profit": 102000.0,
        "size": 0.1,
        "current_profit": 200.0,
        "status": "CLOSED",
        "close_reason": "TAKE PROFIT",
        "open_time": None,
        "close_time": None
    }

    report = engine.close(closed_position)

    assert report["success"] is True
    assert report["symbol"] == "BTC-USD"
    assert report["side"] == "BUY"
    assert report["entry"] == 100000.0
    assert report["exit"] == 102000.0
    assert report["stop_loss"] == 99000.0
    assert report["take_profit"] == 102000.0
    assert report["pnl"] == 200.0
    assert report["status"] == "CLOSED"
    assert report["reason"] == "TAKE PROFIT"


if __name__ == "__main__":

    test_buy_execution()
    test_sell_execution()
    test_strong_buy_execution()
    test_strong_sell_execution()
    test_hold_is_rejected()
    test_invalid_signal_is_rejected()
    test_close_execution_report()

    print("TEST EXECUTION: OK")