from Core.position_controller import PositionController


def test_initial_state():

    controller = PositionController()

    assert controller.get_position() is None
    assert controller.has_position() is False


def test_open_position():

    controller = PositionController()

    result = controller.open_position(
        side="BUY",
        entry=100000.0,
        stop_loss=99000.0,
        take_profit=102000.0,
        symbol="BTC-USD",
        size=0.01
    )

    assert result is True
    assert controller.has_position() is True

    position = controller.get_position()

    assert position["symbol"] == "BTC-USD"
    assert position["side"] == "BUY"
    assert position["entry"] == 100000.0
    assert position["stop_loss"] == 99000.0
    assert position["take_profit"] == 102000.0
    assert position["size"] == 0.01
    assert position["status"] == "OPEN"


def test_prevent_multiple_positions():

    controller = PositionController()

    first = controller.open_position(
        side="BUY",
        entry=100000.0,
        stop_loss=99000.0,
        take_profit=102000.0,
        symbol="BTC-USD",
        size=0.01
    )

    second = controller.open_position(
        side="SELL",
        entry=3000.0,
        stop_loss=3100.0,
        take_profit=2800.0,
        symbol="ETH-USD",
        size=0.10
    )

    assert first is True
    assert second is False

    position = controller.get_position()

    assert position["symbol"] == "BTC-USD"


def test_update_keeps_position_open():

    controller = PositionController()

    controller.open_position(
        side="BUY",
        entry=100000.0,
        stop_loss=99000.0,
        take_profit=102000.0,
        symbol="BTC-USD",
        size=0.01
    )

    result = controller.update(100500.0)

    assert result is not None
    assert result["status"] == "OPEN"
    assert result["current_price"] == 100500.0
    assert result["current_profit"] == 5.0


def test_update_triggers_stop_loss():

    controller = PositionController()

    controller.open_position(
        side="BUY",
        entry=100000.0,
        stop_loss=99000.0,
        take_profit=102000.0,
        symbol="BTC-USD",
        size=0.01
    )

    result = controller.update(98900.0)

    assert result is not None
    assert result["status"] == "CLOSED"
    assert result["close_reason"] == "STOP LOSS"
    assert result["current_price"] == 99000.0
    assert result["current_profit"] == -10.0

    assert controller.get_position() is None
    assert controller.has_position() is False


def test_update_triggers_take_profit():

    controller = PositionController()

    controller.open_position(
        side="BUY",
        entry=100000.0,
        stop_loss=99000.0,
        take_profit=102000.0,
        symbol="BTC-USD",
        size=0.01
    )

    result = controller.update(102100.0)

    assert result is not None
    assert result["status"] == "CLOSED"
    assert result["close_reason"] == "TAKE PROFIT"
    assert result["current_price"] == 102000.0
    assert result["current_profit"] == 20.0

    assert controller.get_position() is None
    assert controller.has_position() is False


def test_manual_close():

    controller = PositionController()

    controller.open_position(
        side="BUY",
        entry=100000.0,
        stop_loss=99000.0,
        take_profit=102000.0,
        symbol="BTC-USD",
        size=0.01
    )

    result = controller.close_position(
        reason="MANUALE",
        current_price=101000.0
    )

    assert result is not None
    assert result["status"] == "CLOSED"
    assert result["close_reason"] == "MANUALE"
    assert result["current_price"] == 101000.0
    assert result["current_profit"] == 10.0

    assert controller.get_position() is None
    assert controller.has_position() is False


def test_reset():

    controller = PositionController()

    controller.open_position(
        side="BUY",
        entry=100000.0,
        stop_loss=99000.0,
        take_profit=102000.0,
        symbol="BTC-USD",
        size=0.01
    )

    assert controller.has_position() is True

    controller.reset()

    assert controller.get_position() is None
    assert controller.has_position() is False


if __name__ == "__main__":

    test_initial_state()
    test_open_position()
    test_prevent_multiple_positions()
    test_update_keeps_position_open()
    test_update_triggers_stop_loss()
    test_update_triggers_take_profit()
    test_manual_close()
    test_reset()

    print("TEST POSITION CONTROLLER: OK")