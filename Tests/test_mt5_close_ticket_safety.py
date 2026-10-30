from types import SimpleNamespace

import pytest

from Execution import mt5_broker as broker_module


class FakeMT5:
    ORDER_TYPE_BUY = 0
    ORDER_TYPE_SELL = 1
    TRADE_ACTION_DEAL = 1
    ORDER_TIME_GTC = 0
    ORDER_FILLING_IOC = 1
    TRADE_RETCODE_DONE = 10009

    def __init__(self, positions):
        self.positions = positions
        self.sent_requests = []

    def positions_get(self, symbol=None):
        return tuple(
            p for p in self.positions
            if symbol is None or p.symbol == symbol
        )

    def symbol_info_tick(self, symbol):
        return SimpleNamespace(bid=99.0, ask=101.0)

    def order_send(self, request):
        self.sent_requests.append(request)
        return SimpleNamespace(
            retcode=self.TRADE_RETCODE_DONE,
            comment="OK",
            order=12345,
            deal=67890,
            price=99.0,
        )


def make_position(ticket, magic, symbol="BTCUSD"):
    return SimpleNamespace(
        ticket=ticket,
        magic=magic,
        symbol=symbol,
        type=FakeMT5.ORDER_TYPE_BUY,
        volume=0.1,
        profit=5.0,
    )


def make_broker(monkeypatch, positions):
    fake = FakeMT5(positions)
    monkeypatch.setattr(broker_module, "mt5", fake)
    broker = broker_module.MT5Broker.__new__(
        broker_module.MT5Broker
    )
    broker.magic = 260813
    broker.connected = True
    broker.symbol_map = {"BTC-USD": "BTCUSD"}
    return broker, fake


def closed_position(ticket=None):
    data = {
        "symbol": "BTC-USD",
        "mt5_symbol": "BTCUSD",
        "side": "BUY",
        "entry": 100.0,
        "current_price": 99.0,
        "current_profit": 0.0,
        "close_reason": "TEST",
    }
    if ticket is not None:
        data["mt5_ticket"] = ticket
    return data


def test_close_uses_exact_phoenix_ticket(monkeypatch):
    other = make_position(111, 999999)
    phoenix = make_position(222, 260813)
    broker, fake = make_broker(monkeypatch, [other, phoenix])
    monkeypatch.setattr(broker_module, "MODE", "TEST")

    result = broker.close(closed_position(222))

    assert len(fake.sent_requests) == 1
    assert fake.sent_requests[0]["position"] == 222
    assert result is not None


@pytest.mark.parametrize("ticket", [None, 999])
def test_close_rejects_missing_or_unknown_ticket(monkeypatch, ticket):
    phoenix = make_position(222, 260813)
    broker, fake = make_broker(monkeypatch, [phoenix])

    result = broker.close(closed_position(ticket))

    assert fake.sent_requests == []
    assert result is not None
    assert result.get("success") is False


def test_close_rejects_foreign_magic(monkeypatch):
    foreign = make_position(222, 999999)
    broker, fake = make_broker(monkeypatch, [foreign])

    result = broker.close(closed_position(222))

    assert fake.sent_requests == []
    assert result is not None
    assert result.get("success") is False


def test_close_rejects_symbol_mismatch(monkeypatch):
    wrong_symbol = make_position(222, 260813, symbol="EURUSD")
    broker, fake = make_broker(monkeypatch, [wrong_symbol])

    result = broker.close(closed_position(222))

    assert fake.sent_requests == []
    assert result is not None
    assert result.get("success") is False

def test_close_is_blocked_in_demo_mode(monkeypatch):
    broker, fake = make_broker(monkeypatch, [])
    monkeypatch.setattr(broker_module, "MODE", "DEMO")

    result = broker.close(closed_position(222))

    assert result["success"] is False
    assert result["executed"] is False
    assert result["dry_run"] is True
    assert fake.sent_requests == []

def test_execute_is_blocked_in_demo_mode(monkeypatch):
    broker, fake = make_broker(monkeypatch, [])
    monkeypatch.setattr(broker_module, "MODE", "DEMO")

    result = broker.execute({})

    assert result["success"] is False
    assert result["executed"] is False
    assert result["dry_run"] is True
    assert "DEMO SAFETY GATE" in result["reason"]
    assert fake.sent_requests == []
