from Core.live_trading_engine import LiveTradingEngine


print("=" * 100)
print("PROJECT PHOENIX AI - E.27.12.61 OPEN RESULT PROPAGATION TEST")
print("=" * 100)


# ============================================================
# FAKE MT5 RESULT
# ============================================================

class FakeMT5Result:

    retcode = 10009
    order = 11111111
    deal = 22222222


# ============================================================
# FAKE MT5 BRIDGE
# ============================================================

class FakeBridge:

    def __init__(self):

        self.execute_called = False

    def execute(
        self,
        trade,
        dry_run=True
    ):

        self.execute_called = True

        print()
        print("[MT5 BRIDGE] execute() chiamato")
        print("TRADE:", trade)
        print("DRY RUN:", dry_run)

        return {

            "executed":
                True,

            "success":
                True,

            "dry_run":
                False,

            "message":
                "Ordine inviato a MT5",

            "retcode":
                10009,

            "order_ticket":
                11111111,

            "deal_ticket":
                22222222,

            "position_ticket":
                55555555,

            "result":
                FakeMT5Result(),

            "risk_gate":
                True,

        }


# ============================================================
# FAKE VALIDATOR
# ============================================================

class FakeValidator:

    def validate(
        self,
        trade
    ):

        return (
            True,
            "OK"
        )


# ============================================================
# FAKE BUILDER
# ============================================================

class FakeBuilder:

    def build(
        self,
        trade
    ):

        return {

            "symbol":
                "BTCUSD",

            "side":
                "BUY",

            "entry":
                100000.0,

            "stop_loss":
                99000.0,

            "take_profit":
                102000.0,

            "size":
                0.01,

            "signal":
                "BUY",

        }


# ============================================================
# ENGINE
# ============================================================

engine = LiveTradingEngine.__new__(
    LiveTradingEngine
)

engine.validator = FakeValidator()

engine.builder = FakeBuilder()

engine.mt5 = FakeBridge()

engine.mt5_enabled = True

engine.mt5_dry_run = False

engine.symbol = "BTCUSD"


# ============================================================
# TEST TRADE
# ============================================================

trade = {

    "symbol":
        "BTCUSD",

    "side":
        "BUY",

    "entry":
        100000.0,

    "stop_loss":
        99000.0,

    "take_profit":
        102000.0,

    "size":
        0.01,

}


# ============================================================
# 1. EXECUTE
# ============================================================

print()
print("1. EXECUTION ENGINE")
print("-" * 100)

result = engine.execution.execute(
    trade
) if hasattr(
    engine,
    "execution"
) else None


# ============================================================
# FALLBACK: TEST DIRETTO EXECUTION ENGINE
# ============================================================

if result is None:

    from Execution.execution_engine import ExecutionEngine

    execution = ExecutionEngine.__new__(
        ExecutionEngine
    )

    execution.validator = FakeValidator()

    execution.builder = FakeBuilder()

    execution.mt5 = FakeBridge()

    execution.mt5_enabled = True

    execution.mt5_dry_run = False

    execution.symbol = "BTCUSD"

    result = execution.execute(
        trade
    )


print()
print("RESULT:")
print(result)


# ============================================================
# 2. CONTRATTO PRINCIPALE
# ============================================================

print()
print("2. CONTRATTO PRINCIPALE")
print("-" * 100)

assert result["success"] is True

assert result["executed"] is True

assert result["dry_run"] is False

assert result["message"] == (
    "Ordine inviato a MT5"
)

assert result["mt5"] is not None


# ============================================================
# 3. CONTRATTO MT5
# ============================================================

print()
print("3. MT5 RESULT")
print("-" * 100)

mt5_result = result["mt5"]

print(
    "EXECUTED:",
    mt5_result.get("executed")
)

print(
    "SUCCESS:",
    mt5_result.get("success")
)

print(
    "RETCODE:",
    mt5_result.get("retcode")
)

print(
    "ORDER TICKET:",
    mt5_result.get(
        "order_ticket"
    )
)

print(
    "DEAL TICKET:",
    mt5_result.get(
        "deal_ticket"
    )
)

print(
    "POSITION TICKET:",
    mt5_result.get(
        "position_ticket"
    )
)


# ============================================================
# 4. ASSERT
# ============================================================

assert (
    mt5_result["executed"]
    is True
)

assert (
    mt5_result["success"]
    is True
)

assert (
    mt5_result["retcode"]
    == 10009
)

assert (
    mt5_result["order_ticket"]
    == 11111111
)

assert (
    mt5_result["deal_ticket"]
    == 22222222
)

assert (
    mt5_result["position_ticket"]
    == 55555555
)


# ============================================================
# 5. BRIDGE CALLED
# ============================================================

print()
print("4. BRIDGE")
print("-" * 100)

print(
    "EXECUTE CALLED:",
    execution.mt5.execute_called
)

assert (
    execution.mt5.execute_called
    is True
)


# ============================================================
# RESULT
# ============================================================

print()
print("=" * 100)
print("E.27.12.61 PASS")
print("=" * 100)

print("EXECUTION -> MT5: OK")
print("SUCCESS: OK")
print("EXECUTED: OK")
print("RETCODE: OK")
print("ORDER TICKET: OK")
print("DEAL TICKET: OK")
print("POSITION TICKET: OK")
print("RESULT PROPAGATION: OK")

print()
print("NESSUN order_send REALE")
print("NESSUNA APERTURA MT5 REALE")
print("NESSUNA CHIUSURA MT5 REALE")

print("=" * 100)

