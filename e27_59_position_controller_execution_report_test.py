from Core.position_controller import PositionController
from Execution.execution_report import ExecutionReport

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.59 POSITION CONTROLLER -> EXECUTION REPORT TEST")
print("=" * 100)

controller = PositionController()
report = ExecutionReport()

print()
print("1. APERTURA BUY")
print("=" * 100)

opened = controller.open_position(
    side="BUY",
    entry=100000,
    stop_loss=99000,
    take_profit=102000,
    symbol="BTC-USD",
    size=0.1
)

print("OPENED =", opened)
print("POSITION =", controller.get_position())

print()
print("2. CHIUSURA TAKE PROFIT")
print("=" * 100)

closed = controller.close_position(
    reason="TAKE PROFIT",
    current_price=102000
)

print("CLOSED =")
print(closed)

print()
print("3. EXECUTION REPORT")
print("=" * 100)

execution_report = report.build(
    closed
)

print("REPORT =")
print(execution_report)

print()
print("4. CONTRACT CHECK")
print("=" * 100)

required_position_fields = [
    "symbol",
    "side",
    "entry",
    "current_price",
    "stop_loss",
    "take_profit",
    "current_profit",
    "status",
    "close_reason",
    "open_time",
    "close_time"
]

required_report_fields = [
    "success",
    "symbol",
    "side",
    "entry",
    "exit",
    "stop_loss",
    "take_profit",
    "pnl",
    "status",
    "reason",
    "open_time",
    "close_time"
]

position_ok = (
    closed is not None
    and all(
        key in closed
        for key in required_position_fields
    )
)

report_ok = (
    execution_report is not None
    and all(
        key in execution_report
        for key in required_report_fields
    )
)

pnl_ok = (
    closed is not None
    and execution_report is not None
    and closed["current_profit"] == execution_report["pnl"]
)

status_ok = (
    closed is not None
    and closed["status"] == "CLOSED"
    and execution_report is not None
    and execution_report["status"] == "CLOSED"
)

print("POSITION CONTRACT =", "PASS" if position_ok else "FAIL")
print("REPORT CONTRACT   =", "PASS" if report_ok else "FAIL")
print("PNL CONSISTENCY    =", "PASS" if pnl_ok else "FAIL")
print("STATUS CONSISTENCY =", "PASS" if status_ok else "FAIL")

print()
print("=" * 100)

if all([
    position_ok,
    report_ok,
    pnl_ok,
    status_ok
]):
    print("E.27.59 POSITION -> REPORT: PASS")
else:
    print("E.27.59 POSITION -> REPORT: ATTENTION")

print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA LIVE")
print("NESSUNA CHIUSURA LIVE")
print("=" * 100)

