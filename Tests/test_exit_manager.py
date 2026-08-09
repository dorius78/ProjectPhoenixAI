"""
========================================
PROJECT PHOENIX AI
Exit Manager Tests
Versione 1.0
========================================
"""

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