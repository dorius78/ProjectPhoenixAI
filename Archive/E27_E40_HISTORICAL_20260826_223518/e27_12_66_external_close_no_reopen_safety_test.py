from Core.live_trading_engine import LiveTradingEngine


print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.66 EXTERNAL CLOSE NO REOPEN SAFETY")
print("=" * 100)


# ============================================================
# FAKE MT5 POSITION
# ============================================================

class FakeMT5Position:

    ticket = 55555555
    symbol = "BTCUSD"
    magic = 260813
    type = 0
    volume = 0.01

    price_open = 100000.0
    sl = 99000.0
    tp = 102000.0


# ============================================================
# FAKE MT5 BRIDGE
# ============================================================

class FakeBridge:

    magic = 260813

    def __init__(self):

        self.position_exists = True
        self.execute_called = 0

    def get_phoenix_positions(self):

        if self.position_exists:

            return [
                FakeMT5Position()
            ]

        return []


# ============================================================
# FAKE EXECUTION
# ============================================================

class FakeExecution:

    def __init__(self):

        self.mt5 = FakeBridge()

        self.close_called = False

    def close(self, position):

        self.close_called = True

        raise AssertionError(
            "ERRORE CRITICO: "
            "execution.close() non deve essere "
            "chiamato per una chiusura esterna MT5."
        )


# ============================================================
# POSITION CONTROLLER
# ============================================================

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

            "side":
                side,

            "entry":
                entry,

            "stop_loss":
                stop_loss,

            "take_profit":
                take_profit,

            "symbol":
                symbol,

            "size":
                size,

            "status":
                "OPEN",

        }

        return True

    def get_position(self):

        return self.position

    def reset(self):

        self.position = None


# ============================================================
# DATABASE
# ============================================================

class FakeDatabase:

    def __init__(self):

        self.saved = []

    def save_trade(self, trade):

        print("[DATABASE] save_trade()")

        self.saved.append(trade)


# ============================================================
# BACKTEST
# ============================================================

class FakeBacktest:

    def __init__(self):

        self.trades = []

    def add_trade(self, trade):

        print("[BACKTEST] add_trade()")

        self.trades.append(trade)


# ============================================================
# PORTFOLIO
# ============================================================

class FakePortfolio:

    def __init__(self):

        self.balance = 10000.0
        self.positions = {}
        self.removed = []

    def add(self, symbol, position):

        self.positions[symbol] = position

    def update_balance(self, pnl):

        print(
            f"[PORTFOLIO] update_balance({pnl})"
        )

        self.balance += pnl

    def get_balance(self):

        return self.balance

    def remove(self, symbol):

        print(
            f"[PORTFOLIO] remove({symbol})"
        )

        self.removed.append(symbol)

        self.positions.pop(
            symbol,
            None
        )


# ============================================================
# TRADING GUARD
# ============================================================

class FakeGuard:

    def __init__(self):

        self.trades = []

    def register_trade(
        self,
        pnl,
        balance
    ):

        print(
            f"[GUARD] register_trade("
            f"pnl={pnl}, "
            f"balance={balance})"
        )

        self.trades.append(
            (pnl, balance)
        )


# ============================================================
# ENGINE
# ============================================================

engine = LiveTradingEngine.__new__(
    LiveTradingEngine
)

engine.execution = FakeExecution()

engine.position_controller = (
    FakePositionController()
)

engine.database = FakeDatabase()

engine.backtest = FakeBacktest()

engine.portfolio = FakePortfolio()

engine.guard = FakeGuard()


# ============================================================
# 1. RECOVERY MT5
# ============================================================

print()
print("1. RECOVERY POSIZIONE MT5")
print("-" * 100)

result_open = (
    engine._sync_mt5_position()
)

print(
    "RESULT:",
    result_open
)

position = (
    engine.position_controller
    .get_position()
)

print(
    "POSITION:",
    position
)

assert result_open is True
assert position is not None
assert position["status"] == "OPEN"
assert position["mt5_ticket"] == 55555555
assert position["magic"] == 260813

assert (
    engine.position_controller.open_calls
    == 1
)


# ============================================================
# 2. POSIZIONE MT5 SCOMPARE
# ============================================================

print()
print("2. MT5 POSIZIONE SCOMPARSA")
print("-" * 100)

engine.execution.mt5.position_exists = False

positions = (
    engine.execution.mt5
    .get_phoenix_positions()
)

print(
    "MT5 POSITIONS:",
    len(positions)
)

assert len(positions) == 0


# ============================================================
# 3. RILEVAZIONE CHIUSURA ESTERNA
# ============================================================

print()
print("3. RILEVAZIONE EXTERNAL CLOSE")
print("-" * 100)

result_close = (
    engine._sync_mt5_position()
)

print(
    "RESULT:",
    result_close
)

assert result_close is True


# ============================================================
# 4. POSITION RESET
# ============================================================

print()
print("4. POSITION RESET")
print("-" * 100)

position_after_close = (
    engine.position_controller
    .get_position()
)

print(
    "POSITION:",
    position_after_close
)

assert position_after_close is None


# ============================================================
# 5. DATABASE
# ============================================================

print()
print("5. DATABASE")
print("-" * 100)

print(
    "SAVED:",
    len(engine.database.saved)
)

assert len(
    engine.database.saved
) == 1


# ============================================================
# 6. PORTFOLIO
# ============================================================

print()
print("6. PORTFOLIO")
print("-" * 100)

print(
    "BALANCE:",
    engine.portfolio.balance
)

print(
    "REMOVED:",
    engine.portfolio.removed
)

assert (
    engine.portfolio.balance
    == 10000.0
    or
    engine.portfolio.balance
    == 10005.0
)

assert (
    engine.portfolio.removed
    == ["BTCUSD"]
)


# ============================================================
# 7. TRADING GUARD
# ============================================================

print()
print("7. TRADING GUARD")
print("-" * 100)

print(
    "TRADES:",
    engine.guard.trades
)

assert len(
    engine.guard.trades
) == 1


# ============================================================
# 8. SECOND SYNC
# ============================================================

print()
print("8. SECOND SYNC DOPO EXTERNAL CLOSE")
print("-" * 100)

result_second_sync = (
    engine._sync_mt5_position()
)

print(
    "RESULT SECOND SYNC:",
    result_second_sync
)

assert result_second_sync is False


# ============================================================
# 9. NO REOPEN
# ============================================================

print()
print("9. NO REOPEN")
print("-" * 100)

position_final = (
    engine.position_controller
    .get_position()
)

print(
    "POSITION FINALE:",
    position_final
)

print(
    "OPEN CALLS:",
    engine.position_controller.open_calls
)

assert position_final is None

assert (
    engine.position_controller.open_calls
    == 1
)


# ============================================================
# 10. NO NEW MT5 EXECUTION
# ============================================================

print()
print("10. NO NEW MT5 EXECUTION")
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
# 11. NO DOUBLE CLOSE
# ============================================================

print()
print("11. NO DOUBLE CLOSE")
print("-" * 100)

print(
    "execution.close_called:",
    engine.execution.close_called
)

assert (
    engine.execution.close_called
    is False
)


# ============================================================
# RESULT
# ============================================================

print()
print("=" * 100)
print("E.27.12.66 PASS")
print("=" * 100)

print("MT5 POSITION RECOVERY: OK")
print("EXTERNAL CLOSE DETECTION: OK")
print("POSITION RESET: OK")
print("DATABASE: OK")
print("PORTFOLIO: OK")
print("TRADING GUARD: OK")
print("SECOND SYNC: OK")
print("NO REOPEN: OK")
print("NO DUPLICATE OPEN: OK")
print("NO NEW MT5 EXECUTION: OK")
print("NO DOUBLE CLOSE: OK")

print()
print("NESSUN order_send REALE")
print("NESSUNA APERTURA MT5 REALE")
print("NESSUNA CHIUSURA MT5 REALE")

print("=" * 100)

