from Core.live_trading_engine import LiveTradingEngine


print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.68 NORMAL CLOSE RESULT LIFECYCLE")
print("=" * 100)


# ============================================================
# POSITION CONTROLLER
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

            "mt5_ticket": 55555555,
            "mt5_order_ticket": 11111111,
            "mt5_deal_ticket": 22222222,
            "mt5_symbol": symbol,
            "magic": 260813,

            "current_price": 100500.0,
            "current_profit": 5.0,
        }

        return True

    def get_position(self):

        return self.position

    def reset(self):

        self.reset_calls += 1
        self.position = None


# ============================================================
# FAKE MT5
# ============================================================

class FakeBridge:

    magic = 260813

    def __init__(self):

        self.execute_called = 0
        self.close_position_called = 0

    def get_phoenix_positions(self):

        return []

    def execute(self, trade, dry_run=False):

        self.execute_called += 1

        raise AssertionError(
            "ERRORE: nuova apertura MT5 inattesa."
        )


# ============================================================
# FAKE EXECUTION
# ============================================================

class FakeExecution:

    def __init__(self):

        self.mt5 = FakeBridge()

        self.close_called = 0

        self.close_result = {

            "success": True,
            "executed": True,
            "dry_run": False,

            "message":
                "Posizione chiusa",

            "retcode":
                10009,

            "order_ticket":
                11111111,

            "deal_ticket":
                22222222,

            "position_ticket":
                55555555,

            "mt5": {

                "success":
                    True,

                "executed":
                    True,

                "retcode":
                    10009,

                "order_ticket":
                    11111111,

                "deal_ticket":
                    22222222,

                "position_ticket":
                    55555555,
            }
        }

    def close(self, position):

        self.close_called += 1

        print(
            "[EXECUTION] close() chiamato"
        )

        return self.close_result


# ============================================================
# DATABASE
# ============================================================

class FakeDatabase:

    def __init__(self):

        self.saved = []

    def has_trade(self, trade_id):

        if trade_id is None:

            return False

        for trade in self.saved:

            if str(
                trade.get(
                    "trade_id"
                )
            ) == str(trade_id):

                return True

        return False

    def save_trade(self, trade):

        print(
            "[DATABASE] save_trade()"
        )

        self.saved.append(trade)


# ============================================================
# BACKTEST
# ============================================================

class FakeBacktest:

    def __init__(self):

        self.trades = []

    def add_trade(self, trade):

        print(
            "[BACKTEST] add_trade()"
        )

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
# 1. OPEN POSITION
# ============================================================

print()
print("1. OPEN POSITION")
print("-" * 100)

order = {

    "success":
        True,

    "side":
        "BUY",

    "entry":
        100000.0,

    "stop_loss":
        99000.0,

    "take_profit":
        102000.0,

    "symbol":
        "BTCUSD",

    "size":
        0.01,

    "mt5": {

        "success":
            True,

        "executed":
            True,

        "retcode":
            10009,

        "order_ticket":
            11111111,

        "deal_ticket":
            22222222,

        "position_ticket":
            55555555,
    }
}


open_result = (
    engine._open_position_from_order(
        order
    )
)

print(
    "OPEN RESULT:",
    open_result
)

assert open_result is True

position = (
    engine.position_controller
    .get_position()
)

assert position is not None
assert position["status"] == "OPEN"


# ============================================================
# 2. NORMAL CLOSE
# ============================================================

print()
print("2. NORMAL CLOSE")
print("-" * 100)

closed = dict(position)

closed.update({

    "status":
        "CLOSED",

    "close_reason":
        "TAKE PROFIT",

    "current_price":
        100500.0,

    "current_profit":
        5.0,

    "initial_stop_loss":
        99000.0,

    "trade_id":
        "55555555",
})


close_result = (
    engine._process_closed_position(
        closed
    )
)

print(
    "CLOSE RESULT:",
    close_result
)

assert close_result is True


# ============================================================
# 3. EXECUTION
# ============================================================

print()
print("3. EXECUTION")
print("-" * 100)

print(
    "close_called:",
    engine.execution.close_called
)

assert (
    engine.execution.close_called
    == 1
)


# ============================================================
# 4. DATABASE
# ============================================================

print()
print("4. DATABASE")
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
assert trade["reason"] == "TAKE PROFIT"

assert (
    trade["mt5_ticket"]
    == 55555555
)

assert (
    trade["mt5_order_ticket"]
    == 11111111
)

assert (
    trade["mt5_deal_ticket"]
    == 22222222
)

assert (
    trade["mt5_symbol"]
    == "BTCUSD"
)

assert (
    trade["magic"]
    == 260813
)

assert (
    trade["pnl"]
    == 5.0
)


# ============================================================
# 5. BACKTEST
# ============================================================

print()
print("5. BACKTEST")
print("-" * 100)

print(
    "TRADES:",
    len(engine.backtest.trades)
)

assert len(
    engine.backtest.trades
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
    == 10005.0
)

assert (
    engine.portfolio.removed
    == ["BTCUSD"]
)


# ============================================================
# 7. GUARD
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

assert (
    engine.guard.trades[0]
    == (5.0, 10005.0)
)


# ============================================================
# 8. POSITION RESET
# ============================================================

print()
print("8. POSITION RESET")
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
# 9. NO DUPLICATE CLOSE
# ============================================================

print()
print("9. NO DUPLICATE CLOSE")
print("-" * 100)

second_close = (
    engine._process_closed_position(
        closed
    )
)

print(
    "SECOND CLOSE RESULT:",
    second_close
)

print(
    "DATABASE:",
    len(engine.database.saved)
)

print(
    "BACKTEST:",
    len(engine.backtest.trades)
)

print(
    "GUARD:",
    len(engine.guard.trades)
)

assert len(
    engine.database.saved
) == 1

assert len(
    engine.backtest.trades
) == 1

assert len(
    engine.guard.trades
) == 1


# ============================================================
# RESULT
# ============================================================

print()
print("=" * 100)
print("E.27.12.68 PASS")
print("=" * 100)

print("NORMAL CLOSE: OK")
print("EXECUTION CONTRACT: OK")
print("DATABASE: OK")
print("BACKTEST: OK")
print("PORTFOLIO: OK")
print("TRADING GUARD: OK")
print("POSITION RESET: OK")
print("MT5 TICKET: OK")
print("ORDER TICKET: OK")
print("DEAL TICKET: OK")
print("NO DUPLICATE CLOSE: OK")
print("FULL NORMAL CLOSE LIFECYCLE: OK")

print()
print("NESSUN order_send REALE")
print("NESSUNA APERTURA MT5 REALE")
print("NESSUNA CHIUSURA MT5 REALE")

print("=" * 100)

