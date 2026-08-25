from Core.live_trading_engine import LiveTradingEngine

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.30 SIMULATED MT5 -> PHOENIX SYNC")
print("=" * 100)


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


class FakeBridge:

    magic = 260813

    def get_phoenix_positions(self):
        return [
            FakeMT5Position()
        ]


class FakeExecution:

    def __init__(self):
        self.mt5 = FakeBridge()


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


engine = LiveTradingEngine.__new__(
    LiveTradingEngine
)

engine.execution = FakeExecution()

engine.position_controller = (
    FakePositionController()
)


print()
print("1. POSIZIONE MT5 SIMULATA")
print("-" * 100)

mt5_position = (
    engine.execution.mt5
    .get_phoenix_positions()[0]
)

print(
    "TICKET:",
    mt5_position.ticket
)

print(
    "SYMBOL:",
    mt5_position.symbol
)

print(
    "TYPE:",
    mt5_position.type
)

print(
    "VOLUME:",
    mt5_position.volume
)

print(
    "ENTRY:",
    mt5_position.price_open
)

print(
    "SL:",
    mt5_position.sl
)

print(
    "TP:",
    mt5_position.tp
)

print(
    "MAGIC:",
    mt5_position.magic
)


print()
print("2. SINCRONIZZAZIONE")
print("-" * 100)

result = (
    engine._sync_mt5_position()
)

print(
    "SYNC RESULT:",
    result
)


print()
print("3. POSITION CONTROLLER")
print("-" * 100)

position = (
    engine.position_controller.get_position()
)

print(position)


assert result is True
assert position is not None

assert position["side"] == "BUY"
assert position["entry"] == 100000.0
assert position["stop_loss"] == 99000.0
assert position["take_profit"] == 102000.0
assert position["symbol"] == "BTCUSD"
assert position["size"] == 0.01

assert position["mt5_ticket"] == 55555555
assert position["mt5_symbol"] == "BTCUSD"
assert position["magic"] == 260813
assert position["current_price"] == 100500.0
assert position["current_profit"] == 5.0


print()
print("=" * 100)
print("E.27.12.30 PASS")
print("MT5 -> PHOENIX SYNC: OK")
print("TICKET: OK")
print("SYMBOL: OK")
print("MAGIC: OK")
print("ENTRY: OK")
print("SIZE: OK")
print("CURRENT PRICE: OK")
print("CURRENT PROFIT: OK")
print("NESSUN order_send")
print("NESSUNA APERTURA MT5")
print("NESSUNA CHIUSURA MT5")
print("=" * 100)

