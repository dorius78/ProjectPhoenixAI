from Core.core_system import CoreSystem
from Database.database_manager import DatabaseManager


def test_core_run_research_aggregates_backtest_database():

    core = CoreSystem()

    database = DatabaseManager(":memory:")
    core.backtest_database = database

    database.save_trade({
        "symbol": "BTC-USD",
        "side": "BUY",
        "entry": 100.0,
        "exit": 110.0,
        "stop_loss": 95.0,
        "initial_stop_loss": 95.0,
        "take_profit": 110.0,
        "size": 1.0,
        "pnl": 10.0,
        "status": "CLOSED",
        "reason": "SIGNAL",
        "open_time": "2026-01-01 10:00:00",
        "close_time": "2026-01-01 11:00:00",
        "duration": 3600.0,
        "result": "WIN",
        "risk_reward": 2.0,
        "regime": "TRENDING"
    })

    result = core.run_research()

    assert "market_research" in result
    assert "pattern_analysis" in result
    assert "market_regime_analysis" in result

    assert result["market_research"]["overview"]["trades"] == 1

    database.connection.close()
