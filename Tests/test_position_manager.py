"""
========================================
PROJECT PHOENIX AI
Position Manager Tests
Versione 1.0
========================================
"""

from Core.position_manager import PositionManager


def test_initial_state():

    manager = PositionManager()

    assert manager.get_position() is None
    assert manager.has_position() is False


def test_open_position():

    manager = PositionManager()

    result = manager.open_position(
        symbol="BTC-USD",
        side="BUY",
        entry=100000,
        size=0.01
    )

    assert result is True
    assert manager.has_position() is True

    position = manager.get_position()

    assert position["symbol"] == "BTC-USD"
    assert position["side"] == "BUY"
    assert position["entry"] == 100000.0
    assert position["size"] == 0.01
    assert position["status"] == "OPEN"


def test_prevent_multiple_positions():

    manager = PositionManager()

    first = manager.open_position(
        symbol="BTC-USD",
        side="BUY",
        entry=100000,
        size=0.01
    )

    second = manager.open_position(
        symbol="ETH-USD",
        side="SELL",
        entry=3000,
        size=0.10
    )

    assert first is True
    assert second is False

    position = manager.get_position()

    assert position["symbol"] == "BTC-USD"


def test_close_position():

    manager = PositionManager()

    manager.open_position(
        symbol="BTC-USD",
        side="BUY",
        entry=100000,
        size=0.01
    )

    closed = manager.close_position()

    assert closed is not None
    assert closed["status"] == "CLOSED"

    assert manager.get_position() is None
    assert manager.has_position() is False


def test_reset():

    manager = PositionManager()

    manager.open_position(
        symbol="BTC-USD",
        side="BUY",
        entry=100000,
        size=0.01
    )

    assert manager.has_position() is True

    manager.reset()

    assert manager.get_position() is None
    assert manager.has_position() is False