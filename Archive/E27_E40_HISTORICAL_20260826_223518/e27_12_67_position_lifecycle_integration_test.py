from Core.live_trading_engine import LiveTradingEngine


print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.67 POSITION LIFECYCLE INTEGRATION")
print("=" * 100)


# ============================================================
# FAKE POSITION CONTROLLER
# ============================================================

class FakePositionController:

    def __init__(self):
        self.position = None
        self.open_calls = 0
        self.reset_calls = 0

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
        self.reset_calls += 1
        self.position = None


# ============================================================
# FAKE EXECUTION
# ============================================================

class FakeExecution:

    def __init__(self):

        self.close_called = 0

        self.mt5 = FakeBridge()

    def close(self, position):

        self.close_called += 1

        return {
            "success": True,
            "executed": True,
            "dry_run": False,
            "message": "Posizione chiusa",
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
# FAKE MT5
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
# FAKE DATABASE
# ============================================================

class FakeDatabase:

    def __init__(self):
        self.saved = []

    def save_trade(self, trade):

        print("[DATABASE] save_trade()")

        self.saved.append(trade)


# ============================================================
# FAKE BACKTEST
# ============================================================

class FakeBacktest:

    def __init__(self):
        self.trades = []

    def add_trade(self, trade):

        print("[BACKTEST] add_trade()")

        self.trades.append(trade)


# ============================================================
# FAKE PORTFOLIO
# ============================================================

class FakePortfolio:

    def __init__(self):

        self.balance = 10000.0
        self.positions = {}
        self.removed = []

    def add(self, symbol, position):

        print(
            f"[PORTFOLIO] add({symbol})"
        )

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
# FAKE GUARD
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
# 1. OPEN
# ============================================================

print()
print("1. OPEN POSITION")
print("-" * 100)

order = {

    "success": True,

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


result_open = (
    engine._open_position_from_order(
        order
    )
)

print(
    "OPEN RESULT:",
    result_open
)

assert result_open is True


# ============================================================
# 2. POSITION ACTIVE
# ============================================================

print()
print("2. POSITION ACTIVE")
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
assert position["mt5_ticket"] == 55555555
assert position["mt5_order_ticket"] == 11111111
assert position["mt5_deal_ticket"] == 22222222
assert position["magic"] == 260813


# ============================================================
# 3. PORTFOLIO
# ============================================================

print()
print("3. PORTFOLIO OPEN")
print("-" * 100)

print(
    "POSITIONS:",
    engine.portfolio.positions
)

assert (
    "BTCUSD"
    in engine.portfolio.positions
)


# ============================================================
# 4. MT5 SYNC
# ============================================================

print()
print("4. MT5 SYNC")
print("-" * 100)

sync_result = (
    engine._sync_mt5_position()
)

print(
    "SYNC RESULT:",
    sync_result
)

assert sync_result is False

assert (
    engine.position_controller.open_calls
    == 1
)


# ============================================================
# 5. EXTERNAL CLOSE
# ============================================================

print()
print("5. EXTERNAL MT5 CLOSE")
print("-" * 100)

engine.execution.mt5.position_exists = False

close_result = (
    engine._sync_mt5_position()
)

print(
    "CLOSE RESULT:",
    close_result
)

assert close_result is True


# ============================================================
# 6. POSITION RESET
# ============================================================

print()
print("6. POSITION RESET")
print("-" * 100)

position_after = (
    engine.position_controller
    .get_position()
)

print(
    "POSITION:",
    position_after
)

assert position_after is None


# ============================================================
# 7. DATABASE
# ============================================================

print()
print("7. DATABASE")
print("-" * 100)

print(
    "SAVED:",
    len(engine.database.saved)
)

assert len(
    engine.database.saved
) == 1

trade = engine.database.saved[0]

print(
    "TRADE:",
    trade
)

assert trade["status"] == "CLOSED"
assert trade["mt5_ticket"] == 55555555
assert trade["mt5_symbol"] == "BTCUSD"
assert trade["magic"] == 260813


# ============================================================
# 8. BACKTEST
# ============================================================

print()
print("8. BACKTEST")
print("-" * 100)

print(
    "TRADES:",
    len(engine.backtest.trades)
)

assert len(
    engine.backtest.trades
) == 1


# ============================================================
# 9. PORTFOLIO CLOSE
# ============================================================

print()
print("9. PORTFOLIO CLOSE")
print("-" * 100)

print(
    "REMOVED:",
    engine.portfolio.removed
)

assert (
    engine.portfolio.removed
    == ["BTCUSD"]
)


# ============================================================
# 10. GUARD
# ============================================================

print()
print("10. TRADING GUARD")
print("-" * 100)

print(
    "TRADES:",
    engine.guard.trades
)

assert len(
    engine.guard.trades
) == 1


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
    == 0
)


# ============================================================
# 12. NO REOPEN
# ============================================================

print()
print("12. NO REOPEN")
print("-" * 100)

second_sync = (
    engine._sync_mt5_position()
)

print(
    "SECOND SYNC:",
    second_sync
)

assert second_sync is False

assert (
    engine.position_controller.open_calls
    == 1
)

assert (
    engine.position_controller
    .get_position()
    is None
)


# ============================================================
# FINAL SAFETY
# ============================================================

print()
print("13. FINAL SAFETY")
print("-" * 100)

print(
    "OPEN CALLS:",
    engine.position_controller.open_calls
)

print(
    "CLOSE CALLS:",
    engine.execution.close_called
)

print(
    "MT5 EXECUTE CALLS:",
    engine.execution.mt5.execute_called
)

print(
    "DATABASE TRADES:",
    len(engine.database.saved)
)

print(
    "BACKTEST TRADES:",
    len(engine.backtest.trades)
)

print(
    "GUARD TRADES:",
    len(engine.guard.trades)
)

assert engine.position_controller.open_calls == 1
assert engine.execution.close_called == 0
assert engine.execution.mt5.execute_called == 0
assert len(engine.database.saved) == 1
assert len(engine.backtest.trades) == 1
assert len(engine.guard.trades) == 1


# ============================================================
# RESULT
# ============================================================

print()
print("=" * 100)
print("E.27.12.67 PASS")
print("=" * 100)

print("OPEN: OK")
print("POSITION REGISTER: OK")
print("MT5 SYNC: OK")
print("MT5 METADATA: OK")
print("EXTERNAL CLOSE: OK")
print("DATABASE: OK")
print("BACKTEST: OK")
print("PORTFOLIO: OK")
print("TRADING GUARD: OK")
print("POSITION RESET: OK")
print("NO DOUBLE CLOSE: OK")
print("NO DUPLICATE OPEN: OK")
print("NO REOPEN: OK")
print("FULL LIFECYCLE: OK")

print()
print("NESSUN order_send REALE")
print("NESSUNA APERTURA MT5 REALE")
print("NESSUNA CHIUSURA MT5 REALE")

print("=" * 100)

