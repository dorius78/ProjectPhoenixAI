from types import SimpleNamespace

import pandas as pd

from Core.core_system import CoreSystem
from Core.backtest_engine import BacktestEngine
from Core.portfolio_manager import PortfolioManager
from Core.position_controller import PositionController
from Database.database_manager import DatabaseManager
from Execution.execution_engine import ExecutionEngine


def test_core_backtest_closes_and_persists_trade_with_regime():
    # Dataset sintetico: la candela 101 raggiunge il Take Profit.
    data = pd.DataFrame(
        {
            "Open": [100.0] * 102,
            "High": [101.0] * 102,
            "Low": [99.0] * 102,
            "Close": [100.0] * 102,
            "Volume": [1000] * 102,
        },
        index=pd.date_range("2026-01-01", periods=102, freq="h"),
    )

    data.iloc[101, data.columns.get_loc("High")] = 111.0
    data.iloc[101, data.columns.get_loc("Low")] = 104.0
    data.iloc[101, data.columns.get_loc("Close")] = 105.0

    trade = {
        "symbol": "BTC-USD",
        "signal": "BUY",
        "side": "BUY",
        "entry": 100.0,
        "stop_loss": 90.0,
        "take_profit": 110.0,
        "risk_reward": 1.0,
        "size": 1.0,
        "atr": 1.0,
    }

    class ControlledAnalysis:
        def __init__(self):
            self.calls = 0

        def analyze(self, window, price, symbol, account_balance):
            self.calls += 1

            if self.calls == 1:
                return {
                    "signal": {"valid": True, "signal": "BUY"},
                    "trade": dict(trade),
                    "regime": {
                        "regime": "TRENDING",
                        "confidence": 0.8,
                    },
                    "analysis": {},
                    "indicators": {},
                    "risk": {},
                    "decision": {},
                    "supervision": {},
                }

            return {
                "signal": {"valid": False, "signal": "HOLD"},
                "trade": None,
                "regime": {"regime": "TRENDING"},
            }

    # Costruisce il sistema senza inizializzare i database reali.
    core = CoreSystem.__new__(CoreSystem)
    database = DatabaseManager(":memory:")

    core.candles = SimpleNamespace(
        get_backtest_data=lambda symbol, period, interval: data
    )
    core.analysis = ControlledAnalysis()
    core.position_controller = PositionController()
    core.portfolio = PortfolioManager()
    core.backtest = BacktestEngine()
    core.execution = ExecutionEngine()
    core.backtest_database = database
    core.print_backtest = lambda: core.backtest.run()

    try:
        stats = core.run_backtest(
            symbol="BTC-USD",
            period="test",
            interval="1h",
        )

        # Una sola operazione deve essere stata chiusa e registrata.
        assert database.count() == 1
        assert core.backtest.closed_trades == 1
        assert len(core.backtest.history) == 1

        saved_trade = core.backtest.history[0]
        assert saved_trade["status"] == "CLOSED"
        assert saved_trade["reason"] == "TAKE PROFIT"
        assert saved_trade["pnl"] > 0
        assert saved_trade["regime"]["regime"] == "TRENDING"

        # Controlla anche il regime realmente persistito in SQLite.
        cursor = database.connection.cursor()
        columns = [
            item[1]
            for item in cursor.execute("PRAGMA table_info(trades)").fetchall()
        ]
        assert "regime" in columns

        row = cursor.execute(
            "SELECT pnl, status, reason, regime FROM trades"
        ).fetchone()

        assert row is not None
        assert row[0] > 0
        assert row[1] == "CLOSED"
        assert row[2] == "TAKE PROFIT"
        assert row[3] == "TRENDING"

        assert stats is not None
        assert core.position_controller.has_position() is False

    finally:
        database.connection.close()
