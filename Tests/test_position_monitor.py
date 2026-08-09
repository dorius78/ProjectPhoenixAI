"""
========================================
PROJECT PHOENIX AI
Position Monitor Tests
Versione 1.0
========================================
"""

from Core.position_monitor import PositionMonitor


def test_buy_position():

    monitor = PositionMonitor()

    position = {
        "symbol": "BTC-USD",
        "side": "BUY",
        "entry": 100000.0,
        "size": 0.01,
        "status": "OPEN",
        "max_profit": 0.0
    }

    result = monitor.update(
        position,
        101000.0
    )

    assert result["current_price"] == 101000.0
    assert result["current_profit"] == 10.0
    assert result["max_profit"] == 10.0


def test_sell_position():

    monitor = PositionMonitor()

    position = {
        "symbol": "BTC-USD",
        "side": "SELL",
        "entry": 100000.0,
        "size": 0.01,
        "status": "OPEN",
        "max_profit": 0.0
    }

    result = monitor.update(
        position,
        99000.0
    )

    assert result["current_price"] == 99000.0
    assert result["current_profit"] == 10.0
    assert result["max_profit"] == 10.0


def test_max_profit_is_preserved():

    monitor = PositionMonitor()

    position = {
        "symbol": "BTC-USD",
        "side": "BUY",
        "entry": 100000.0,
        "size": 0.01,
        "status": "OPEN",
        "max_profit": 0.0
    }

    monitor.update(
        position,
        102000.0
    )

    assert position["current_profit"] == 20.0
    assert position["max_profit"] == 20.0

    monitor.update(
        position,
        101000.0
    )

    assert position["current_profit"] == 10.0
    assert position["max_profit"] == 20.0