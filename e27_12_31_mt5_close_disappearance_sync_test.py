from Core.live_trading_engine import LiveTradingEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.31 MT5 CLOSE / DISAPPEARANCE SYNC TEST")
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
# BRIDGE SIMULATO
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


class FakeExecution:

    def __init__(self):
        self.mt5 = FakeBridge()


# ============================================================
# POSITION CONTROLLER SIMULATO
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
            "size": size
        }

        return True

    def get_position(self):
        return self.position


# ============================================================
# CREAZIONE ENGINE
# ============================================================

engine = LiveTradingEngine.__new__(
    LiveTradingEngine
)

engine.execution = FakeExecution()

engine.position_controller = (
    FakePositionController()
)


# ============================================================
# 1. SINCRONIZZAZIONE POSIZIONE MT5
# ============================================================

print()
print("1. APERTURA MT5 SIMULATA")
print("-" * 100)

result_open = (
    engine._sync_mt5_position()
)

print(
    "SYNC RESULT:",
    result_open
)

position = (
    engine.position_controller.get_position()
)

print(
    "POSITION:",
    position
)

assert result_open is True
assert position is not None
assert position["mt5_ticket"] == 55555555
assert position["symbol"] == "BTCUSD"


# ============================================================
# 2. LA POSIZIONE MT5 SCOMPARE
# ============================================================

print()
print("2. POSIZIONE MT5 CHIUSA SIMULATAMENTE")
print("-" * 100)

engine.execution.mt5.position_exists = False

positions_after_close = (
    engine.execution.mt5
    .get_phoenix_positions()
)

print(
    "POSIZIONI MT5 PHOENIX:",
    len(positions_after_close)
)

assert len(
    positions_after_close
) == 0


# ============================================================
# 3. NUOVA SINCRONIZZAZIONE
# ============================================================

print()
print("3. NUOVA SINCRONIZZAZIONE")
print("-" * 100)

result_close_sync = (
    engine._sync_mt5_position()
)

print(
    "SYNC RESULT:",
    result_close_sync
)

position_after = (
    engine.position_controller.get_position()
)

print(
    "POSITION CONTROLLER:",
    position_after
)


# ============================================================
# 4. AUDIT
# ============================================================

print()
print("=" * 100)
print("E.27.12.31 AUDIT")
print("=" * 100)

print(
    "ATTENZIONE: questo test verifica il comportamento "
    "della sincronizzazione quando una posizione MT5 "
    "scompare."
)

print()
print(
    "RISULTATO SYNC INIZIALE:",
    result_open
)

print(
    "RISULTATO SYNC DOPO CHIUSURA:",
    result_close_sync
)

print(
    "POSITION DOPO CHIUSURA:",
    position_after
)

print()
print("NESSUN order_send")
print("NESSUNA APERTURA MT5")
print("NESSUNA CHIUSURA MT5")
print("=" * 100)

