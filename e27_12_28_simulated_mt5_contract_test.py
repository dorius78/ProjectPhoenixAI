from Core.live_trading_engine import LiveTradingEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.28 SIMULATED MT5 CONTRACT TEST")
print("=" * 100)

class FakePositionController:

    def __init__(self):
        self.position = None

    def has_position(self):
        return self.position is not None

    def open_position(
        self,
        side,
        entry,
        stop_loss,
        take_profit,
        symbol,
        size
    ):

        self.position = {
            "side": side,
            "entry": entry,
            "stop_loss": stop_loss,
            "take_profit": take_profit,
            "symbol": symbol,
            "size": size
        }

        return True

    def get_position(self):
        return self.position


class FakePortfolio:

    def __init__(self):
        self.items = []

    def add(self, symbol, position):
        self.items.append(
            (symbol, position)
        )


class FakeExecution:

    def __init__(self):
        self.mt5 = type(
            "FakeBridge",
            (),
            {
                "magic": 260813
            }
        )()


engine = LiveTradingEngine.__new__(
    LiveTradingEngine
)

engine.position_controller = (
    FakePositionController()
)

engine.portfolio = (
    FakePortfolio()
)

engine.execution = (
    FakeExecution()
)

order = {

    "success": True,

    "executed": True,

    "dry_run": False,

    "side": "BUY",

    "entry": 100000.0,

    "stop_loss": 99000.0,

    "take_profit": 102000.0,

    "symbol": "BTCUSD",

    "size": 0.01,

    "mt5": {

        "success": True,

        "executed": True,

        "dry_run": False,

        "order_ticket": 12345678,

        "deal_ticket": 87654321,

        "position_ticket": 55555555,

        "retcode": 10009
    }
}

print()
print("ESECUZIONE TEST SIMULATA")
print("-" * 100)

result = engine._open_position_from_order(
    order
)

print("RESULT:", result)

position = (
    engine.position_controller.get_position()
)

print()
print("POSITION")
print("-" * 100)
print(position)

print()
print("PORTFOLIO")
print("-" * 100)
print(engine.portfolio.items)

assert result is True
assert position is not None

assert position["mt5_ticket"] == 55555555
assert position["mt5_order_ticket"] == 12345678
assert position["mt5_deal_ticket"] == 87654321
assert position["mt5_symbol"] == "BTCUSD"
assert position["magic"] == 260813

assert len(
    engine.portfolio.items
) == 1

print()
print("=" * 100)
print("E.27.12.28 PASS")
print("EXECUTION -> POSITION -> PORTFOLIO: OK")
print("MT5 TICKET: OK")
print("ORDER TICKET: OK")
print("DEAL TICKET: OK")
print("MAGIC: OK")
print("NESSUN order_send")
print("NESSUNA APERTURA MT5")
print("NESSUNA CHIUSURA MT5")
print("=" * 100)

