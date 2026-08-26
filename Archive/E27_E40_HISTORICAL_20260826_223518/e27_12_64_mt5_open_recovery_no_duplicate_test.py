from Core.live_trading_engine import LiveTradingEngine


print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.64 MT5 OPEN RECOVERY / NO DUPLICATE OPEN")
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

    price_current = 100500.0

    profit = 5.0


# ============================================================
# FAKE MT5 BRIDGE
# ============================================================

class FakeBridge:

    magic = 260813

    def __init__(self):

        self.execute_called = False

    def get_phoenix_positions(self):

        return [
            FakeMT5Position()
        ]

    def execute(self, trade):

        self.execute_called = True

        raise AssertionError(
            "ERRORE CRITICO: "
            "Phoenix ha tentato una "
            "NUOVA APERTURA MT5."
        )


# ============================================================
# FAKE EXECUTION
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
# STATO INIZIALE
# ============================================================

print()
print("1. STATO PHOENIX INIZIALE")
print("-" * 100)

print(
    "POSITION:",
    engine.position_controller.get_position()
)

assert (
    engine.position_controller.get_position()
    is None
)


# ============================================================
# MT5 ESISTENTE
# ============================================================

print()
print("2. POSIZIONE GIA PRESENTE SU MT5")
print("-" * 100)

positions = (
    engine.execution.mt5
    .get_phoenix_positions()
)

print(
    "MT5 POSITIONS:",
    len(positions)
)

assert len(positions) == 1

print(
    "MT5 TICKET:",
    positions[0].ticket
)

print(
    "MT5 SYMBOL:",
    positions[0].symbol
)

assert positions[0].ticket == 55555555
assert positions[0].symbol == "BTCUSD"


# ============================================================
# RECOVERY
# ============================================================

print()
print("3. MT5 OPEN RECOVERY")
print("-" * 100)

result = (
    engine._sync_mt5_position()
)

print()
print(
    "SYNC RESULT:",
    result
)

assert result is True


# ============================================================
# POSITION RECUPERATA
# ============================================================

print()
print("4. POSITION PHOENIX RECUPERATA")
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

assert position["symbol"] == "BTCUSD"

assert position["side"] == "BUY"

assert position["entry"] == 100000.0

assert position["stop_loss"] == 99000.0

assert position["take_profit"] == 102000.0

assert position["size"] == 0.01


# ============================================================
# MT5 METADATA
# ============================================================

print()
print("5. MT5 METADATA")
print("-" * 100)

print(
    "MT5 TICKET:",
    position.get("mt5_ticket")
)

print(
    "MT5 SYMBOL:",
    position.get("mt5_symbol")
)

print(
    "MAGIC:",
    position.get("magic")
)

assert (
    position["mt5_ticket"]
    == 55555555
)

assert (
    position["mt5_symbol"]
    == "BTCUSD"
)

assert (
    position["magic"]
    == 260813
)


# ============================================================
# NO DUPLICATE OPEN
# ============================================================

print()
print("6. NO DUPLICATE OPEN")
print("-" * 100)

print(
    "EXECUTE CALLED:",
    engine.execution.mt5.execute_called
)

assert (
    engine.execution.mt5.execute_called
    is False
)


# ============================================================
# RISULTATO
# ============================================================

print()
print("=" * 100)
print("E.27.12.64 PASS")
print("=" * 100)

print("MT5 EXISTING POSITION: OK")
print("PHOENIX RECOVERY: OK")
print("POSITION CONTROLLER: OK")
print("MT5 TICKET: OK")
print("MT5 SYMBOL: OK")
print("MAGIC: OK")
print("NO DUPLICATE OPEN: OK")
print("NO NEW MT5 EXECUTION: OK")

print()
print("NESSUN order_send REALE")
print("NESSUNA APERTURA MT5 REALE")
print("NESSUNA CHIUSURA MT5 REALE")

print("=" * 100)

