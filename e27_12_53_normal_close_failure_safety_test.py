from Core.live_trading_engine import LiveTradingEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.53 NORMAL CLOSE FAILURE SAFETY TEST")
print("=" * 100)


class FakeExecution:

    def __init__(self):
        self.close_called = False

    def close(self, position):

        self.close_called = True

        print()
        print("[EXECUTION] close() chiamato")
        print("[EXECUTION] SIMULAZIONE MT5 CLOSE FAILURE")

        return {

            "success": False,

            "executed": False,

            "dry_run": False,

            "message":
                "MT5 close rifiutato",

            "retcode":
                10016,

            "order_ticket":
                0,

            "deal_ticket":
                0,

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

        }


class FakeDatabase:

    def __init__(self):
        self.saved = []

    def save_trade(self, trade):

        print("[DATABASE] ERRORE: save_trade() NON DOVREBBE ESSERE CHIAMATO")

        self.saved.append(trade)


class FakeBacktest:

    def __init__(self):
        self.trades = []

    def add_trade(self, trade):

        print("[BACKTEST] ERRORE: add_trade() NON DOVREBBE ESSERE CHIAMATO")

        self.trades.append(trade)


class FakePortfolio:

    def __init__(self):

        self.balance = 10000.0
        self.removed = []

    def update_balance(self, pnl):

        print("[PORTFOLIO] ERRORE: update_balance() NON DOVREBBE ESSERE CHIAMATO")

        self.balance += pnl

    def get_balance(self):

        return self.balance

    def remove(self, symbol):

        print("[PORTFOLIO] ERRORE: remove() NON DOVREBBE ESSERE CHIAMATO")

        self.removed.append(symbol)


class FakeGuard:

    def __init__(self):
        self.trades = []

    def register_trade(self, pnl, balance):

        print("[GUARD] ERRORE: register_trade() NON DOVREBBE ESSERE CHIAMATO")

        self.trades.append((pnl, balance))


class FakePositionController:

    def __init__(self):

        self.position = {

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

            "status":
                "OPEN",

            "mt5_ticket":
                55555555,

            "mt5_symbol":
                "BTCUSD",

            "magic":
                260813,

            "current_price":
                100500.0,

            "current_profit":
                5.0,

        }

    def get_position(self):
        return self.position


engine = LiveTradingEngine.__new__(
    LiveTradingEngine
)

engine.execution = FakeExecution()

engine.database = FakeDatabase()

engine.backtest = FakeBacktest()

engine.portfolio = FakePortfolio()

engine.guard = FakeGuard()

engine.position_controller = FakePositionController()


closed = {

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

    "close_reason":
        "TAKE PROFIT",

    "current_price":
        100500.0,

    "current_profit":
        5.0,

    "mt5_ticket":
        55555555,

    "mt5_symbol":
        "BTCUSD",

    "magic":
        260813,

    "trade_id":
        "55555555",

}


print()
print("1. CHIUSURA MT5 FALLITA")
print("-" * 100)

result = (
    engine._process_closed_position(
        closed
    )
)

print()
print("RESULT:", result)


print()
print("2. DATABASE")
print("-" * 100)

print(
    "SAVED:",
    len(engine.database.saved)
)

assert len(
    engine.database.saved
) == 0


print()
print("3. BACKTEST")
print("-" * 100)

print(
    "TRADES:",
    len(engine.backtest.trades)
)

assert len(
    engine.backtest.trades
) == 0


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

assert (
    engine.portfolio.balance
    == 10000.0
)

assert (
    engine.portfolio.removed
    == []
)


print()
print("5. TRADING GUARD")
print("-" * 100)

print(
    "TRADES:",
    engine.guard.trades
)

assert (
    engine.guard.trades
    == []
)


print()
print("6. POSITION")
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

assert (
    position["status"]
    == "OPEN"
)


print()
print("=" * 100)
print("E.27.12.53 PASS")
print("=" * 100)

print("MT5 CLOSE FAILURE: OK")
print("DATABASE PROTECTED: OK")
print("BACKTEST PROTECTED: OK")
print("PORTFOLIO PROTECTED: OK")
print("TRADING GUARD PROTECTED: OK")
print("POSITION PRESERVED: OK")
print("NO FALSE CLOSED TRADE: OK")

print()
print("NESSUN order_send REALE")
print("NESSUNA APERTURA MT5")
print("NESSUNA CHIUSURA MT5")

print("=" * 100)

