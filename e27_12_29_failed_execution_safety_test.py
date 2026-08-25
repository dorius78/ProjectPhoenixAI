from Core.live_trading_engine import LiveTradingEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.29 FAILED EXECUTION SAFETY TEST")
print("=" * 100)


class FakePositionController:

    def __init__(self):
        self.position = None

    def has_position(self):
        return self.position is not None

    def open_position(self, **kwargs):
        self.position = kwargs
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


# =========================================
# ORDINE FALLITO
# =========================================

order = {

    "success": False,

    "executed": False,

    "dry_run": False,

    "message":
        "MT5 ordine rifiutato",

    "side": "BUY",

    "entry": 100000.0,

    "stop_loss": 99000.0,

    "take_profit": 102000.0,

    "symbol": "BTCUSD",

    "size": 0.01,

    "mt5": {

        "success": False,

        "executed": False,

        "dry_run": False,

        "retcode": 10016,

        "order_ticket": 0,

        "deal_ticket": 0,

        "position_ticket": 0
    }
}


print()
print("ESECUZIONE FALLITA SIMULATA")
print("-" * 100)

result = (
    engine._open_position_from_order(
        order
    )
)

print("RESULT:", result)

position = (
    engine.position_controller.get_position()
)

print()
print("POSITION CONTROLLER")
print("-" * 100)
print(position)

print()
print("PORTFOLIO")
print("-" * 100)
print(engine.portfolio.items)


assert result is False

assert position is None

assert len(
    engine.portfolio.items
) == 0


print()
print("=" * 100)
print("E.27.12.29 PASS")
print("ORDINE NON ESEGUITO -> NESSUNA POSIZIONE")
print("POSITION CONTROLLER: PROTETTO")
print("PORTFOLIO: PROTETTO")
print("NESSUN order_send")
print("NESSUNA APERTURA MT5")
print("NESSUNA CHIUSURA MT5")
print("=" * 100)

