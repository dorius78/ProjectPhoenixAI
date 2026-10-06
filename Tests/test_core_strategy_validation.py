from Core.core_system import CoreSystem

def test_core_system_validate_strategy_result():
    core = CoreSystem()

    strategy_result = {
        "net_profit": 100,
        "win_rate": 0.60,
        "profit_factor": 1.50,
        "max_drawdown": 20,
        "total_trades": 50
    }

    result = core.validate_strategy_result(
        strategy_result,
        {
            "min_net_profit": 0,
            "min_win_rate": 0.50,
            "min_profit_factor": 1.0,
            "max_drawdown": 30,
            "min_trades": 20
        }
    )

    assert result["valid"] is True
    assert result["decision"] == "VALID"


def test_core_system_validate_strategy_result_rejects_invalid():
    core = CoreSystem()

    result = core.validate_strategy_result(
        {
            "net_profit": -100,
            "win_rate": 0.30,
            "profit_factor": 0.70,
            "max_drawdown": 50,
            "total_trades": 5
        },
        {
            "min_net_profit": 0,
            "min_win_rate": 0.50,
            "min_profit_factor": 1.0,
            "max_drawdown": 30,
            "min_trades": 20
        }
    )

    assert result["valid"] is False
    assert result["decision"] == "INVALID"
