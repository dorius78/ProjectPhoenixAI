from Core.live_trading_engine import LiveTradingEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.55 CLOSE TICKET PROPAGATION TEST")
print("=" * 100)


class FakeExecution:

    def __init__(self):

        self.mt5 = object()
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
                None,

            "reason":
                "TAKE PROFIT",

            "mt5_ticket":
                55555555,

            "order_ticket":
                11111111,

            "deal_ticket":
                22222222,

            "position_ticket":
                55555555,

            "mt5_symbol":
                "BTCUSD",

            "magic":
                260813,

            "position":
                position,

        }


class FakeDatabase:

    def __init__(self):
        self.saved = []

    def save_trade(self, trade):

        print()
        print("[DATABASE] save_trade()")

        self.saved.append(trade)


class FakeBacktest:

    def __init__(self):
        self.trades = []

    def add_trade(self, trade):

        print("[BACKTEST] add_trade()")

        self.trades.append(trade)


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


class FakePositionController:

    def __init__(self):
        self.position = {
            "side": "BUY",
            "entry": 100000.0,
            "stop_loss": 99000.0,
            "take_profit": 102000.0,
            "symbol": "BTCUSD",
            "size": 0.01,
            "status": "OPEN",
            "mt5_ticket": 55555555,
            "mt5_symbol": "BTCUSD",
            "magic": 260813,
            "current_price": 100500.0,
            "current_profit": 5.0,
        }

    def get_position(self):
        return self.position

    def has_position(self):
        return self.position is not None


engine = LiveTradingEngine.__new__(
    LiveTradingEngine
)

engine.execution = FakeExecution()

engine.database = FakeDatabase()

engine.backtest = FakeBacktest()

engine.portfolio = FakePortfolio()

engine.guard = FakeGuard()

engine.position_controller = (
    FakePositionController()
)

position = (
    engine.position_controller.get_position()
)


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
print("1. PROCESS CHIUSURA")
print("-" * 100)

result = (
    engine._process_closed_position(
        closed
    )
)

print()
print("RESULT:", result)

assert result is True


print()
print("2. DATABASE")
print("-" * 100)

assert len(
    engine.database.saved
) == 1

trade = (
    engine.database.saved[0]
)

print(
    "TRADE:",
    trade
)


print()
print("3. VERIFICA TICKET")
print("-" * 100)

print(
    "MT5 TICKET:",
    trade.get("mt5_ticket")
)

print(
    "ORDER TICKET:",
    trade.get("mt5_order_ticket")
)

print(
    "DEAL TICKET:",
    trade.get("mt5_deal_ticket")
)

print(
    "POSITION TICKET:",
    trade.get("mt5_ticket")
)


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


print()
print("4. SERVIZI")
print("-" * 100)

assert len(
    engine.backtest.trades
) == 1

assert (
    engine.portfolio.balance
    == 10005.0
)

assert (
    engine.portfolio.removed
    == ["BTCUSD"]
)

assert len(
    engine.guard.trades
) == 1


print()
print("=" * 100)
print("E.27.12.55 PASS")
print("=" * 100)

print("CLOSE CONTRACT: OK")
print("MT5 TICKET: OK")
print("ORDER TICKET: OK")
print("DEAL TICKET: OK")
print("MT5 SYMBOL: OK")
print("MAGIC: OK")
print("DATABASE: OK")
print("BACKTEST: OK")
print("PORTFOLIO: OK")
print("TRADING GUARD: OK")

print()
print("NESSUN order_send REALE")
print("NESSUNA APERTURA MT5")
print("NESSUNA CHIUSURA MT5")

print("=" * 100)

