from Core.core_system import CoreSystem


def test_core_exposes_learning_data():

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

    assert result["learning"]["learned"] is True

    learned = core.get_learned_strategies()
    history = core.get_learning_history()

    assert len(learned) == 1
    assert learned[0]["strategy"] == strategy

    assert len(history) == 1
    assert history[0]["strategy"] == strategy
    assert history[0]["decision"] == "LEARNED"
