from Core.live_trading_engine import LiveTradingEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.46 EXTERNAL CLOSE MT5 METADATA FULL TEST")
print("=" * 100)


# ============================================================
# MT5 POSITION
# ============================================================

class FakeMT5Position:

    symbol = "BTCUSD"
    type = 0
    volume = 0.01
    price_open = 100000.0
    price_current = 100500.0
    sl = 99000.0
    tp = 102000.0
    ticket = 55555555
    magic = 260813
    profit = 5.0


# ============================================================
# MT5 BRIDGE
# ============================================================

class FakeBridge:

    magic = 260813

    def __init__(self):
        self.position_exists = True

    def get_phoenix_positions(self):

        if self.position_exists:
            return [
                FakeMT5Position()
            ]

        return []


# ============================================================
# EXECUTION
# ============================================================

class FakeExecution:

    def __init__(self):

        self.mt5 = FakeBridge()

        self.close_called = False

    def close(self, position):

        self.close_called = True

        raise AssertionError(
            "ERRORE: execution.close() "
            "non deve essere chiamato "
            "per MT5 EXTERNAL CLOSE"
        )


# ============================================================
# POSITION CONTROLLER
# ============================================================

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

            "size": size,

            "status": "OPEN",

            "open_time": None,

            "close_time": None,

            "close_reason": None,

            "current_price": None,

            "current_profit": None,

            "initial_stop_loss": stop_loss,

            "trade_id": None

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

        self.saved.append(
            dict(trade)
        )


# ============================================================
# BACKTEST
# ============================================================

class FakeBacktest:

    def __init__(self):

        self.trades = []

    def add_trade(self, trade):

        print("[BACKTEST] add_trade()")

        self.trades.append(
            dict(trade)
        )


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
# GUARD
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
# 1. MT5 -> PHOENIX
# ============================================================

print()
print("1. SINCRONIZZAZIONE POSIZIONE MT5")
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

assert position["mt5_ticket"] == 55555555
assert position["mt5_symbol"] == "BTCUSD"
assert position["magic"] == 260813


# ============================================================
# 2. CHIUSURA ESTERNA
# ============================================================

print()
print("2. CHIUSURA ESTERNA MT5")
print("-" * 100)

engine.execution.mt5.position_exists = False

assert len(
    engine.execution.mt5
    .get_phoenix_positions()
) == 0

print(
    "MT5 POSITIONS: 0"
)


# ============================================================
# 3. PROCESS CLOSED
# ============================================================

print()
print("3. PROCESS CLOSED POSITION")
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
print("4. POSITION CONTROLLER")
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
# 5. DATABASE
# ============================================================

print()
print("5. DATABASE TRADE")
print("-" * 100)

assert len(
    engine.database.saved
) == 1

trade = engine.database.saved[0]

print(
    "TRADE:",
    trade
)

assert trade["status"] == "CLOSED"

assert trade["symbol"] == "BTCUSD"

assert trade["side"] == "BUY"

assert trade["pnl"] == 5.0

assert trade["reason"] == (
    "MT5 EXTERNAL CLOSE"
)

assert trade["mt5_ticket"] == 55555555

assert trade["mt5_symbol"] == "BTCUSD"

assert trade["magic"] == 260813


# ============================================================
# 6. ORDER / DEAL METADATA
# ============================================================

print()
print("6. MT5 ORDER / DEAL METADATA")
print("-" * 100)

print(
    "mt5_order_ticket:",
    trade["mt5_order_ticket"]
)

print(
    "mt5_deal_ticket:",
    trade["mt5_deal_ticket"]
)

assert (
    "mt5_order_ticket"
    in trade
)

assert (
    "mt5_deal_ticket"
    in trade
)


# ============================================================
# 7. BACKTEST
# ============================================================

print()
print("7. BACKTEST")
print("-" * 100)

assert len(
    engine.backtest.trades
) == 1

print(
    engine.backtest.trades[0]
)


# ============================================================
# 8. PORTFOLIO
# ============================================================

print()
print("8. PORTFOLIO")
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
# 9. GUARD
# ============================================================

print()
print("9. TRADING GUARD")
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


# ============================================================
# 10. NO DOUBLE CLOSE
# ============================================================

print()
print("10. NO DOUBLE CLOSE")
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
# FINAL
# ============================================================

print()
print("=" * 100)
print("E.27.12.46 PASS")
print("=" * 100)

print("MT5 -> PHOENIX SYNC: OK")
print("EXTERNAL CLOSE: OK")
print("CLOSED TRADE: OK")
print("MT5 TICKET: OK")
print("MT5 SYMBOL: OK")
print("MAGIC: OK")
print("ORDER TICKET FIELD: OK")
print("DEAL TICKET FIELD: OK")
print("DATABASE: OK")
print("BACKTEST: OK")
print("PORTFOLIO: OK")
print("TRADING GUARD: OK")
print("POSITION RESET: OK")
print("NO DOUBLE CLOSE: OK")

print()
print("NESSUN order_send")
print("NESSUNA APERTURA MT5")
print("NESSUNA CHIUSURA MT5")

print("=" * 100)

