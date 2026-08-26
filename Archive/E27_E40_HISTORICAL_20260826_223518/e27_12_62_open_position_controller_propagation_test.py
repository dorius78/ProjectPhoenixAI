from Core.live_trading_engine import LiveTradingEngine


print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.62 OPEN POSITION CONTROLLER PROPAGATION")
print("=" * 100)


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

        print()
        print("[POSITION CONTROLLER] open_position()")

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


class FakeExecution:

    def __init__(self):

        self.mt5 = None


engine = LiveTradingEngine.__new__(
    LiveTradingEngine
)

engine.position_controller = (
    FakePositionController()
)

engine.execution = FakeExecution()


order = {

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

}


execution_result = {

    "success":
        True,

    "executed":
        True,

    "dry_run":
        False,

    "message":
        "Ordine inviato a MT5",

    "mt5":
        {

            "executed":
                True,

            "success":
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


print()
print("1. ORDINE ESEGUITO")
print("-" * 100)

print(
    "ORDER:",
    order
)

print(
    "EXECUTION RESULT:",
    execution_result
)


print()
print("2. APERTURA POSITION CONTROLLER")
print("-" * 100)


result = (
    engine._open_position_from_order(
        order,
        execution_result
    )
)


print()
print("RESULT:",
      result)


print()
print("3. POSITION")
print("-" * 100)


position = (
    engine.position_controller
    .get_position()
)

print(
    "POSITION:",
    position
)


assert result is True

assert position is not None

assert position["side"] == "BUY"

assert position["entry"] == 100000.0

assert position["stop_loss"] == 99000.0

assert position["take_profit"] == 102000.0

assert position["symbol"] == "BTCUSD"

assert position["size"] == 0.01


print()
print("=" * 100)
print("E.27.12.62 PASS")
print("=" * 100)

print("EXECUTION -> POSITION: OK")
print("SIDE: OK")
print("ENTRY: OK")
print("STOP LOSS: OK")
print("TAKE PROFIT: OK")
print("SYMBOL: OK")
print("SIZE: OK")
print("POSITION OPEN: OK")

print()
print("NESSUN order_send REALE")
print("NESSUNA APERTURA MT5 REALE")
print("NESSUNA CHIUSURA MT5 REALE")

print("=" * 100)

