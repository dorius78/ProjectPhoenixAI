from Core.live_trading_engine import LiveTradingEngine


print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.62B OPEN POSITION + MT5 METADATA")
print("=" * 100)


class FakeBridge:

    magic = 260813


class FakeExecution:

    def __init__(self):

        self.mt5 = FakeBridge()


class FakePositionController:

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

        self.position = {

            "side": side,
            "entry": entry,
            "stop_loss": stop_loss,
            "take_profit": take_profit,
            "symbol": symbol,
            "size": size,
            "status": "OPEN",

        }

        return True

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

        print(
            f"[PORTFOLIO] add({symbol})"
        )

        self.positions[symbol] = position


engine = LiveTradingEngine.__new__(
    LiveTradingEngine
)

engine.execution = FakeExecution()

engine.position_controller = (
    FakePositionController()
)

engine.portfolio = FakePortfolio()


# ============================================================
# ORDINE COMPLETO
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


print()
print("1. APERTURA POSIZIONE")
print("-" * 100)

result = (
    engine._open_position_from_order(
        order
    )
)

print(
    "RESULT:",
    result
)


assert result is True


# ============================================================
# POSITION
# ============================================================

print()
print("2. POSITION CONTROLLER")
print("-" * 100)

position = (
    engine.position_controller
    .get_position()
)

print(
    "POSITION:",
    position
)

assert position is not None

assert position["status"] == "OPEN"

assert position["side"] == "BUY"

assert position["entry"] == 100000.0

assert position["stop_loss"] == 99000.0

assert position["take_profit"] == 102000.0

assert position["symbol"] == "BTCUSD"

assert position["size"] == 0.01


# ============================================================
# MT5 METADATA
# ============================================================

print()
print("3. MT5 METADATA")
print("-" * 100)

print(
    "MT5 TICKET:",
    position.get("mt5_ticket")
)

print(
    "ORDER TICKET:",
    position.get("mt5_order_ticket")
)

print(
    "DEAL TICKET:",
    position.get("mt5_deal_ticket")
)

print(
    "MT5 SYMBOL:",
    position.get("mt5_symbol")
)

print(
    "MAGIC:",
    position.get("magic")
)


assert (
    position["mt5_ticket"]
    == 55555555
)

assert (
    position["mt5_order_ticket"]
    == 11111111
)

assert (
    position["mt5_deal_ticket"]
    == 22222222
)

assert (
    position["mt5_symbol"]
    == "BTCUSD"
)

assert (
    position["magic"]
    == 260813
)


# ============================================================
# PORTFOLIO
# ============================================================

print()
print("4. PORTFOLIO")
print("-" * 100)

print(
    engine.portfolio.positions
)

assert (
    "BTCUSD"
    in engine.portfolio.positions
)


# ============================================================
# RESULT
# ============================================================

print()
print("=" * 100)
print("E.27.12.62B PASS")
print("=" * 100)

print("EXECUTION -> POSITION: OK")
print("POSITION CONTROLLER: OK")
print("MT5 TICKET: OK")
print("ORDER TICKET: OK")
print("DEAL TICKET: OK")
print("MT5 SYMBOL: OK")
print("MAGIC: OK")
print("PORTFOLIO: OK")

print()
print("NESSUN order_send REALE")
print("NESSUNA APERTURA MT5 REALE")
print("NESSUNA CHIUSURA MT5 REALE")

print("=" * 100)

