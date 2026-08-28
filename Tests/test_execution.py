import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Execution.execution_engine import ExecutionEngine


def trade(signal, side=None):

    if signal in ("BUY", "STRONG BUY"):
        stop = 99000.0
        target = 102000.0
        default_side = "BUY"
    else:
        stop = 101000.0
        target = 98000.0
        default_side = "SELL"

    return {
        "symbol": "BTC-USD",
        "signal": signal,
        "side": side or default_side,
        "entry": 100000.0,
        "stop_loss": stop,
        "take_profit": target,
        "risk_reward": 2.0,
        "size": 0.1,
        "atr": 100.0,
    }


def test_buy_execution():

    result = ExecutionEngine().execute(
        trade("BUY", "BUY")
    )

    assert result["success"] is True
    assert result["symbol"] == "BTC-USD"
    assert result["side"] == "BUY"
    assert result["signal"] == "BUY"
    assert result["entry"] == 100000.0
    assert result["stop_loss"] == 99000.0
    assert result["take_profit"] == 102000.0
    assert result["risk_reward"] == 2.0
    assert result["size"] == 0.1
    assert result["status"] == "OPEN"


def test_sell_execution():

    result = ExecutionEngine().execute(
        trade("SELL", "SELL")
    )

    assert result["success"] is True
    assert result["symbol"] == "BTC-USD"
    assert result["side"] == "SELL"
    assert result["signal"] == "SELL"
    assert result["size"] == 0.1
    assert result["status"] == "OPEN"


def test_strong_buy_execution():

    result = ExecutionEngine().execute(
        trade("STRONG BUY")
    )

    assert result["success"] is True
    assert result["signal"] == "STRONG BUY"
    assert result["side"] == "BUY"


def test_strong_sell_execution():

    result = ExecutionEngine().execute(
        trade("STRONG SELL")
    )

    assert result["success"] is True
    assert result["signal"] == "STRONG SELL"
    assert result["side"] == "SELL"


def test_hold_is_rejected():

    result = ExecutionEngine().execute(
        trade("HOLD")
    )

    assert result["success"] is False
    assert result["reason"] == "Segnale HOLD"


def test_invalid_signal_is_rejected():

    result = ExecutionEngine().execute(
        trade("INVALID")
    )

    assert result["success"] is False


if __name__ == "__main__":

    test_buy_execution()
    test_sell_execution()
    test_strong_buy_execution()
    test_strong_sell_execution()
    test_hold_is_rejected()
    test_invalid_signal_is_rejected()

    print("TEST EXECUTION: OK")
