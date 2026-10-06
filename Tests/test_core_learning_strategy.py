from Core.core_system import CoreSystem


def test_core_system_learns_validated_strategy():
    core = CoreSystem()

    strategy = {
        "name": "strategy_a",
        "ema_fast": 10,
        "ema_slow": 30
    }

    result = core.learn_strategy_result(
        strategy,
        {
            "net_profit": 100,
            "win_rate": 0.60,
            "profit_factor": 1.50,
            "max_drawdown": 20,
            "total_trades": 50
        },
        {
            "min_net_profit": 0,
            "min_win_rate": 0.50,
            "min_profit_factor": 1.0,
            "max_drawdown": 30,
            "min_trades": 20
        }
    )

    assert result["validation"]["valid"] is True
    assert result["learning"]["learned"] is True
    assert result["learning"]["decision"] == "LEARNED"


def test_core_system_rejects_invalid_strategy():
    core = CoreSystem()

    result = core.learn_strategy_result(
        {"name": "bad_strategy"},
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

    assert result["validation"]["valid"] is False
    assert result["learning"]["learned"] is False
    assert result["learning"]["decision"] == "REJECTED"
