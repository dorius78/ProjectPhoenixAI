from Core.live_trading_engine import LiveTradingEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.42 EXTERNAL CLOSE FULL PIPELINE TEST")
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
            return [FakeMT5Position()]

        return []


# ============================================================
# EXECUTION SIMULATA
# ============================================================

class FakeExecution:

    def __init__(self):
        self.mt5 = FakeBridge()
        self.close_called = False

    def close(self, position):

        self.close_called = True

        raise AssertionError(
            "ERRORE: execution.close() "
            "NON DEVE ESSERE CHIAMATO "
            "PER MT5 EXTERNAL CLOSE"
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
            "close_reason": None
        }

        return True

    def get_position(self):
        return self.position

    def reset(self):
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
# 1. SYNC POSIZIONE
# ============================================================

print()
print("1. SINCRONIZZAZIONE POSIZIONE MT5")
print("-" * 100)

result_open = (
    engine._sync_mt5_position()
)

print("RESULT:", result_open)

position = (
    engine.position_controller.get_position()
)

print("POSITION:", position)

assert result_open is True
assert position is not None
assert position["mt5_ticket"] == 55555555


# ============================================================
# 2. SIMULAZIONE CHIUSURA ESTERNA
# ============================================================

print()
print("2. CHIUSURA ESTERNA MT5")
print("-" * 100)

engine.execution.mt5.position_exists = False

print(
    "MT5 POSITIONS:",
    len(
        engine.execution.mt5
        .get_phoenix_positions()
    )
)

assert len(
    engine.execution.mt5
    .get_phoenix_positions()
) == 0


# ============================================================
# 3. SYNC CHIUSURA
# ============================================================

print()
print("3. RILEVAZIONE CHIUSURA")
print("-" * 100)

result_close = (
    engine._sync_mt5_position()
)

print("RESULT:", result_close)

closed = (
    engine.position_controller.get_position()
)

print("POSITION:", closed)


# ============================================================
# 4. VERIFICA
# ============================================================

assert result_close is True

assert closed is None

assert (
    engine.execution.close_called
    is False
)


# ============================================================
# RISULTATO
# ============================================================

print()
print("=" * 100)
print("E.27.12.42 PASS")
print("=" * 100)

print("MT5 -> PHOENIX SYNC: OK")
print("EXTERNAL CLOSE DETECTION: OK")
print("POSITION RESET: OK")
print("execution.close() BYPASS: OK")
print("NO DOUBLE CLOSE: OK")

print()
print("NESSUN order_send")
print("NESSUNA APERTURA MT5")
print("NESSUNA CHIUSURA MT5")

print("=" * 100)

