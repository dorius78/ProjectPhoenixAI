from Core.live_trading_engine import LiveTradingEngine


print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.65 DOUBLE SYNC SAFETY")
print("=" * 100)


class FakeMT5Position:

    ticket = 55555555
    symbol = "BTCUSD"
    magic = 260813

    type = 0

    volume = 0.01

    price_open = 100000.0

    sl = 99000.0

    tp = 102000.0

    price_current = 100500.0

    profit = 5.0


class FakeBridge:

    magic = 260813

    def __init__(self):

        self.execute_called = 0

        self.get_positions_called = 0

    def get_phoenix_positions(self):

        self.get_positions_called += 1

        return [
            FakeMT5Position()
        ]

    def execute(self, trade):

        self.execute_called += 1

        raise AssertionError(
            "ERRORE CRITICO: "
            "nuova apertura MT5 durante sync."
        )


class FakeExecution:

    def __init__(self):

        self.mt5 = FakeBridge()


class FakePositionController:

    def __init__(self):

        self.position = None

        self.open_calls = 0

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

        self.open_calls += 1

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

    def reset(self):

        self.position = None


engine = LiveTradingEngine.__new__(
    LiveTradingEngine
)

engine.execution = FakeExecution()

engine.position_controller = (
    FakePositionController()
)


# ============================================================
# SYNC #1
# ============================================================

print()
print("1. SYNC #1")
print("-" * 100)

result_1 = (
    engine._sync_mt5_position()
)

print(
    "RESULT #1:",
    result_1
)

assert result_1 is True

position_1 = (
    engine.position_controller
    .get_position()
)

print(
    "POSITION #1:",
    position_1
)

assert position_1 is not None

assert (
    position_1["mt5_ticket"]
    == 55555555
)


# ============================================================
# STATO DOPO SYNC #1
# ============================================================

print()
print("2. STATO DOPO SYNC #1")
print("-" * 100)

print(
    "OPEN CALLS:",
    engine.position_controller.open_calls
)

assert (
    engine.position_controller.open_calls
    == 1
)


# ============================================================
# SYNC #2
# ============================================================

print()
print("3. SYNC #2")
print("-" * 100)

result_2 = (
    engine._sync_mt5_position()
)

print(
    "RESULT #2:",
    result_2
)

assert result_2 is False


# ============================================================
# POSITION
# ============================================================

print()
print("4. POSITION FINALE")
print("-" * 100)

position_2 = (
    engine.position_controller
    .get_position()
)

print(
    "POSITION #2:",
    position_2
)

assert position_2 is not None

assert (
    position_2["mt5_ticket"]
    == 55555555
)


# ============================================================
# NO DUPLICATE POSITION
# ============================================================

print()
print("5. NO DUPLICATE POSITION")
print("-" * 100)

print(
    "OPEN CALLS:",
    engine.position_controller.open_calls
)

assert (
    engine.position_controller.open_calls
    == 1
)


# ============================================================
# NO DUPLICATE MT5 EXECUTION
# ============================================================

print()
print("6. NO DUPLICATE MT5 EXECUTION")
print("-" * 100)

print(
    "EXECUTE CALLS:",
    engine.execution.mt5.execute_called
)

assert (
    engine.execution.mt5.execute_called
    == 0
)


# ============================================================
# RESULT
# ============================================================

print()
print("=" * 100)
print("E.27.12.65 PASS")
print("=" * 100)

print("SYNC #1: OK")
print("SYNC #2: OK")
print("POSITION PRESERVED: OK")
print("ONE POSITION ONLY: OK")
print("NO DUPLICATE OPEN: OK")
print("NO DUPLICATE MT5 EXECUTION: OK")

print()
print("NESSUN order_send REALE")
print("NESSUNA APERTURA MT5 REALE")
print("NESSUNA CHIUSURA MT5 REALE")

print("=" * 100)

