from Core.core_system import CoreSystem


def test_process_strategy_discovery_results():
    core = CoreSystem()

    results = [
        {
            "strategy": {"name": "good_strategy"},
            "result": {
                "net_profit": 500,
                "win_rate": 60,
                "profit_factor": 1.5,
                "max_drawdown": 200,
                "total_trades": 50
            }
        },
        {
            "strategy": {"name": "bad_strategy"},
            "result": {
                "net_profit": -100,
                "win_rate": 30,
                "profit_factor": 0.7,
                "max_drawdown": 600,
                "total_trades": 5
            }
        }
    ]

    criteria = {
        "min_net_profit": 100,
        "min_win_rate": 50,
        "min_profit_factor": 1.2,
        "max_drawdown": 500,
        "min_trades": 30
    }

    processed = core.process_strategy_discovery_results(
        results,
        criteria
    )

    assert len(processed["results"]) == 2
    assert len(processed["validated"]) == 2
    assert processed["validated"][0]["validation"]["valid"] is True
    assert processed["validated"][1]["validation"]["valid"] is False

    assert len(processed["learned"]) == 1
    assert processed["learned"][0]["strategy"]["name"] == "good_strategy"
    assert processed["learned"][0]["learning"]["learned"] is True
