import pandas as pd

from Core.analysis_engine import AnalysisEngine
from Core.trade_manager import TradeManager
from Core.position_controller import PositionController
from Execution.execution_engine import ExecutionEngine


def create_test_data():
    return pd.DataFrame({
        "Open": list(range(100, 156)),
        "High": list(range(101, 157)),
        "Low": list(range(99, 155)),
        "Close": list(range(100, 156)),
        "Volume": [1000] * 56
    })


def test_end_to_end_trade_lifecycle():

    # =========================================================
    # 1. ANALYSIS
    # =========================================================

    analysis_engine = AnalysisEngine()

    data = create_test_data()

    analysis = analysis_engine.analyze(
        data=data,
        price=155,
        symbol="BTC-USD",
        account_balance=10000
    )

    assert isinstance(analysis, dict)
    assert "signal" in analysis
    assert "risk" in analysis
    assert "trade" in analysis

    # =========================================================
    # 2. CONTROLLED TRADE DECISION
    # =========================================================

    trade_manager = TradeManager()

    trade = trade_manager.generate_trade(
        symbol="BTC-USD",
        price=100000.0,
        signal="BUY",
        atr=1000.0,
        account_balance=10000.0
    )

    assert trade is not None
    assert trade["side"] == "BUY"
    assert trade["symbol"] == "BTC-USD"

    # =========================================================
    # 3. PAPER EXECUTION
    # =========================================================

    execution = ExecutionEngine()

    order = execution.execute(trade)

    assert order["success"] is True
    assert order["executed"] is True
    assert order["mt5"] is None
    assert order["status"] == "OPEN"

    # =========================================================
    # 4. POSITION OPEN
    # =========================================================

    controller = PositionController()

    opened = controller.open_position(
        side=trade["side"],
        entry=trade["entry"],
        stop_loss=trade["stop_loss"],
        take_profit=trade["take_profit"],
        symbol=trade["symbol"],
        size=trade["size"]
    )

    assert opened is True
    assert controller.has_position() is True

    # =========================================================
    # 5. BREAK EVEN
    # =========================================================

    entry = float(trade["entry"])

    position = controller.update(
        current_price=entry * 1.001
    )

    assert position is not None
    assert position["status"] == "OPEN"

    position = controller.get_position()

    assert position["break_even"] is True
    assert position["stop_loss"] == position["entry"]

    # =========================================================
    # 6. TAKE PROFIT / CLOSE
    # =========================================================

    closed = controller.update(
        current_price=float(trade["take_profit"])
    )

    assert closed is not None
    assert closed["status"] == "CLOSED"
    assert closed["close_reason"] == "TAKE PROFIT"
    assert closed["current_profit"] > 0

    assert controller.has_position() is False
    assert controller.get_position() is None

    # =========================================================
    # 7. EXECUTION CLOSE REPORT
    # =========================================================

    report = execution.close(closed)

    assert report["success"] is True
    assert report["symbol"] == "BTC-USD"
    assert report["side"] == "BUY"
    assert report["status"] == "CLOSED"
    assert report["reason"] == "TAKE PROFIT"
    assert report["pnl"] > 0


if __name__ == "__main__":
    test_end_to_end_trade_lifecycle()
    print("TEST END-TO-END: OK")
