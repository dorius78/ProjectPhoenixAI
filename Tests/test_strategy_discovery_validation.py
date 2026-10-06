from Core.core_system import CoreSystem

def test_core_system_strategy_validator_accepts_discovery_result():
    core = CoreSystem()

    result = {
        "net_profit": 100,
        "win_rate": 0.60,
        "profit_factor": 1.50,
        "max_drawdown": 20,
        "total_trades": 50
    }

    validation = core.strategy_validator.validate(
        result,
        {
            "min_net_profit": 0,
            "min_win_rate": 0.50,
            "min_profit_factor": 1.0,
            "max_drawdown": 30,
            "min_trades": 20
        }
    )

    assert validation["valid"] is True
    assert validation["decision"] == "VALID"


def test_core_system_strategy_validator_rejects_bad_discovery_result():
    core = CoreSystem()

    result = {
        "net_profit": -100,
        "win_rate": 0.30,
        "profit_factor": 0.70,
        "max_drawdown": 50,
        "total_trades": 5
    }

    validation = core.strategy_validator.validate(
        result,
        {
            "min_net_profit": 0,
            "min_win_rate": 0.50,
            "min_profit_factor": 1.0,
            "max_drawdown": 30,
            "min_trades": 20
        }
    )

    assert validation["valid"] is False
    assert validation["decision"] == "INVALID"
