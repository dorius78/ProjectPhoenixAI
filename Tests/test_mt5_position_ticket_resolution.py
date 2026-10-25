from types import SimpleNamespace
import Execution.mt5_broker as broker_module

class FakeMT5:
    def __init__(self, deals, positions):
        self.deals, self.positions = deals, positions
    def history_deals_get(self, ticket=None):
        return [d for d in self.deals if ticket is None or d.ticket == ticket]
    def positions_get(self):
        return self.positions

def setup(monkeypatch, deals, positions):
    monkeypatch.setattr(broker_module, "mt5", FakeMT5(deals, positions))
    broker = broker_module.MT5Broker.__new__(broker_module.MT5Broker)
    broker.magic = 260813
    return broker

def test_resolves_verified_position_ticket(monkeypatch):
    deal = SimpleNamespace(ticket=7002, position_id=8003, magic=260813, symbol="EURUSD")
    pos = SimpleNamespace(ticket=8003, identifier=8003, magic=260813, symbol="EURUSD")
    assert setup(monkeypatch, [deal], [pos])._resolve_position_ticket(7002, "EURUSD") == 8003

def test_rejects_foreign_magic_and_symbol(monkeypatch):
    deal = SimpleNamespace(ticket=7002, position_id=8003, magic=999, symbol="EURUSD")
    pos = SimpleNamespace(ticket=8003, identifier=8003, magic=260813, symbol="EURUSD")
    assert setup(monkeypatch, [deal], [pos])._resolve_position_ticket(7002, "EURUSD") == 0
    deal.magic = 260813
    pos.symbol = "GBPUSD"
    assert setup(monkeypatch, [deal], [pos])._resolve_position_ticket(7002, "EURUSD") == 0

def test_rejects_ambiguous_position_match(monkeypatch):
    deal = SimpleNamespace(ticket=7002, position_id=8003, magic=260813, symbol="EURUSD")
    p1 = SimpleNamespace(ticket=8003, identifier=8003, magic=260813, symbol="EURUSD")
    p2 = SimpleNamespace(ticket=8004, identifier=8003, magic=260813, symbol="EURUSD")
    assert setup(monkeypatch, [deal], [p1, p2])._resolve_position_ticket(7002, "EURUSD") == 0
