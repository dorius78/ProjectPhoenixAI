from Core.live_trading_engine import LiveTradingEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.52 NORMAL CLOSE FULL PIPELINE TEST")
print("=" * 100)


# ============================================================
# FAKE MT5 RESULT
# ============================================================

class FakeResult:

    retcode = 10009
    order = 11111111
    deal = 22222222
    position = 55555555


# ============================================================
# FAKE EXECUTION
# ============================================================

class FakeExecution:

    def __init__(self):

        self.close_called = False

    def close(self, position):

        self.close_called = True

        print()
        print("[EXECUTION] close() chiamato")

        return {

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

            "symbol":
                "BTCUSD",

            "side":
                "BUY",

            "entry":
                100000.0,

            "exit":
                100500.0,

            "pnl":
                5.0,

            "close_time":
                position["close_time"],

            "reason":
                "TAKE PROFIT",

        }


# ============================================================
# POSITION CONTROLLER
# ============================================================

class FakePositionController:

    def __init__(self):

        self.position = None

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

        print()
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
        self.removed = []

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
# POSIZIONE DA CHIUDERE
# ============================================================

position = {

    "side":
        "BUY",

    "entry":
        100000.0,

    "stop_loss":
        99000.0,

    "take_profit":
        102000.0,

    "initial_stop_loss":
        99000.0,

    "symbol":
        "BTCUSD",

    "size":
        0.01,

    "status":
        "CLOSED",

    "open_time":
        None,

    "close_time":
        None,

    "close_reason":
        "TAKE PROFIT",

    "current_price":
        100500.0,

    "current_profit":
        5.0,

    "trade_id":
        "55555555",

    "mt5_ticket":
        55555555,

    "mt5_symbol":
        "BTCUSD",

    "magic":
        260813,
}


# ============================================================
# FAKE EXECUTION CON DIPENDENZA ALLA POSITION
# ============================================================

FakeExecution.close = (
    lambda self, closed:
        self._close_impl(closed)
)


def close_impl(
    self,
    closed
):

    self.close_called = True

    print()
    print("[EXECUTION] close() chiamato")

    return {

        "success":
            True,

        "executed":
            True,

        "dry_run":
            False,

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

        "symbol":
            closed["symbol"],

        "side":
            closed["side"],

        "entry":
            closed["entry"],

        "exit":
            closed["current_price"],

        "pnl":
            closed["current_profit"],

        "close_time":
            closed["close_time"],

        "reason":
            closed["close_reason"],

    }


FakeExecution._close_impl = close_impl


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
# TEST
# ============================================================

print()
print("1. PROCESS CHIUSURA NORMALE")
print("-" * 100)

result = (
    engine._process_closed_position(
        position
    )
)

print()
print("RESULT:", result)


# ============================================================
# DATABASE
# ============================================================

print()
print("2. DATABASE")
print("-" * 100)

print(
    "SAVED:",
    len(engine.database.saved)
)

trade = engine.database.saved[0]

print(
    "TRADE:",
    trade
)


# ============================================================
# ASSERT DATABASE
# ============================================================

assert result is True

assert len(
    engine.database.saved
) == 1

assert trade["status"] == "CLOSED"

assert trade["symbol"] == "BTCUSD"

assert trade["side"] == "BUY"

assert trade["entry"] == 100000.0

assert trade["exit"] == 100500.0

assert trade["pnl"] == 5.0

assert trade["reason"] == "TAKE PROFIT"

assert trade["mt5_ticket"] == 55555555

assert trade["mt5_order_ticket"] == 11111111

assert trade["mt5_deal_ticket"] == 22222222

assert trade["mt5_symbol"] == "BTCUSD"

assert trade["magic"] == 260813


# ============================================================
# BACKTEST
# ============================================================

print()
print("3. BACKTEST")
print("-" * 100)

assert len(
    engine.backtest.trades
) == 1


# ============================================================
# PORTFOLIO
# ============================================================

print()
print("4. PORTFOLIO")
print("-" * 100)

print(
    "BALANCE:",
    engine.portfolio.balance
)

print(
    "REMOVED:",
    engine.portfolio.removed
)

assert engine.portfolio.balance == 10005.0

assert (
    engine.portfolio.removed
    == ["BTCUSD"]
)


# ============================================================
# TRADING GUARD
# ============================================================

print()
print("5. TRADING GUARD")
print("-" * 100)

print(
    engine.guard.trades
)

assert len(
    engine.guard.trades
) == 1

assert (
    engine.guard.trades[0][0]
    == 5.0
)

assert (
    engine.guard.trades[0][1]
    == 10005.0
)


# ============================================================
# EXECUTION
# ============================================================

print()
print("6. EXECUTION")
print("-" * 100)

print(
    "close_called:",
    engine.execution.close_called
)

assert (
    engine.execution.close_called
    is True
)


# ============================================================
# RESULT
# ============================================================

print()
print("=" * 100)
print("E.27.12.52 PASS")
print("=" * 100)

print("NORMAL CLOSE: OK")
print("EXECUTION: OK")
print("DATABASE: OK")
print("BACKTEST: OK")
print("PORTFOLIO: OK")
print("TRADING GUARD: OK")
print("MT5 TICKET: OK")
print("ORDER TICKET: OK")
print("DEAL TICKET: OK")
print("POSITION TICKET: OK")

print()
print("NESSUN order_send REALE")
print("NESSUNA APERTURA MT5")
print("NESSUNA CHIUSURA MT5")

print("=" * 100)

