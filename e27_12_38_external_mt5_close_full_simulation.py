from Core.live_trading_engine import LiveTradingEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.38 EXTERNAL MT5 CLOSE FULL SIMULATION")
print("=" * 100)


# ============================================================
# POSIZIONE MT5 SIMULATA
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
# BRIDGE MT5 SIMULATO
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
# EXECUTION SIMULATA
# ============================================================

class FakeExecution:

    def __init__(self):
        self.mt5 = FakeBridge()


# ============================================================
# POSITION CONTROLLER
# ============================================================

class FakePositionController:

    def __init__(self):
        self.position = None
        self.reset_called = False

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

            "current_price": entry,
            "current_profit": 0.0,

            "initial_stop_loss": stop_loss,

            "trade_id": None

        }

        return True

    def get_position(self):
        return self.position

    def reset(self):

        self.reset_called = True
        self.position = None


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


# ============================================================
# PROCESS CLOSED POSITION SIMULATO
# ============================================================

processed_trades = []


def fake_process_closed_position(
    closed
):

    processed_trades.append(
        closed
    )

    print()
    print("PROCESS CLOSED POSITION CHIAMATO")
    print("-" * 100)
    print(closed)

    return True


engine._process_closed_position = (
    fake_process_closed_position
)


# ============================================================
# 1. MT5 POSIZIONE PRESENTE
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

position_before = (
    engine.position_controller.get_position()
)

print(
    "POSITION:",
    position_before
)

assert result_open is True
assert position_before is not None

assert (
    position_before["mt5_ticket"]
    == 55555555
)

assert (
    position_before["mt5_symbol"]
    == "BTCUSD"
)

assert (
    position_before["magic"]
    == 260813
)


# ============================================================
# 2. MT5 CHIUDE ESTERNAMENTE
# ============================================================

print()
print("2. CHIUSURA ESTERNA MT5 SIMULATA")
print("-" * 100)

engine.execution.mt5.position_exists = False

print(
    "POSIZIONI MT5:",
    len(
        engine.execution.mt5
        .get_phoenix_positions()
    )
)

assert (
    len(
        engine.execution.mt5
        .get_phoenix_positions()
    )
    == 0
)


# ============================================================
# 3. NUOVA SINCRONIZZAZIONE
# ============================================================

print()
print("3. RILEVAZIONE CHIUSURA ESTERNA")
print("-" * 100)

result_close = (
    engine._sync_mt5_position()
)

print(
    "RESULT:",
    result_close
)


# ============================================================
# 4. VERIFICA POSITION CONTROLLER
# ============================================================

print()
print("4. POSITION CONTROLLER")
print("-" * 100)

position_after = (
    engine.position_controller.get_position()
)

print(
    "POSITION:",
    position_after
)

assert position_after is None

assert (
    engine.position_controller.reset_called
    is True
)


# ============================================================
# 5. VERIFICA TRADE CLOSED
# ============================================================

print()
print("5. TRADE CLOSED")
print("-" * 100)

assert len(
    processed_trades
) == 1

closed = processed_trades[0]

print(
    "CLOSED:",
    closed
)

assert (
    closed["status"]
    == "CLOSED"
)

assert (
    closed["close_reason"]
    == "MT5 EXTERNAL CLOSE"
)

assert (
    closed["mt5_ticket"]
    == 55555555
)

assert (
    closed["symbol"]
    == "BTCUSD"
)

assert (
    closed["side"]
    == "BUY"
)

assert (
    closed["entry"]
    == 100000.0
)

assert (
    closed["current_price"]
    == 100500.0
)

assert (
    closed["current_profit"]
    == 5.0
)


# ============================================================
# RISULTATO
# ============================================================

print()
print("=" * 100)
print("E.27.12.38 PASS")
print("=" * 100)

print("MT5 -> PHOENIX SYNC: OK")
print("EXTERNAL CLOSE DETECTION: OK")
print("CLOSED TRADE: OK")
print("CLOSE REASON: OK")
print("MT5 TICKET: OK")
print("POSITION RESET: OK")
print("PROCESS CLOSED POSITION: OK")

print()
print("NESSUN order_send")
print("NESSUNA apertura MT5")
print("NESSUNA chiusura MT5")

print("=" * 100)

