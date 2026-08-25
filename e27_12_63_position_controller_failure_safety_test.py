from Core.live_trading_engine import LiveTradingEngine


print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.63 POSITION CONTROLLER FAILURE SAFETY")
print("=" * 100)


class FakeBridge:

    magic = 260813


class FakeExecution:

    def __init__(self):
        self.mt5 = FakeBridge()


class FailingPositionController:

    def __init__(self):

        self.position = None

    def open_position(
        self,
        side,
        entry,
        stop_loss,
        take_profit,
        symbol,
        size
    ):

        print(
            "[POSITION CONTROLLER] "
            "SIMULAZIONE FALLIMENTO"
        )

        return False

    def get_position(self):

        return self.position


class FakePortfolio:

    def __init__(self):

        self.positions = {}

    def add(
        self,
        symbol,
        position
    ):

        raise AssertionError(
            "ERRORE: Portfolio.add() "
            "NON DEVE ESSERE CHIAMATO "
            "SE POSITION CONTROLLER FALLISCE"
        )


engine = LiveTradingEngine.__new__(
    LiveTradingEngine
)

engine.execution = FakeExecution()

engine.position_controller = (
    FailingPositionController()
)

engine.portfolio = FakePortfolio()


# ============================================================
# ORDINE MT5 GIA ESEGUITO
# ============================================================

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

        "executed": True,

        "success": True,

        "retcode": 10009,

        "order_ticket": 11111111,

        "deal_ticket": 22222222,

        "position_ticket": 55555555,

    }

}


# ============================================================
# TEST
# ============================================================

print()
print("1. POSITION CONTROLLER FAILURE")
print("-" * 100)

result = (
    engine._open_position_from_order(
        order
    )
)

print()
print(
    "RESULT:",
    result
)


# ============================================================
# VERIFICA RISULTATO
# ============================================================

print()
print("2. SAFETY CHECK")
print("-" * 100)

assert result is False


position = (
    engine.position_controller
    .get_position()
)

print(
    "POSITION:",
    position
)

assert position is None


print()
print("=" * 100)
print("E.27.12.63 PASS")
print("=" * 100)

print("POSITION CONTROLLER FAILURE: OK")
print("RESULT FALSE: OK")
print("POSITION NOT REGISTERED: OK")
print("PORTFOLIO NOT UPDATED: OK")
print("NO FALSE SUCCESS: OK")

print()
print("NESSUN order_send REALE")
print("NESSUNA APERTURA MT5 REALE")
print("NESSUNA CHIUSURA MT5 REALE")

print("=" * 100)

