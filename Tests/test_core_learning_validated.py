from Core.core_system import CoreSystem


def test_learn_validated_strategies_only_learns_valid():

    core = CoreSystem()

    validated_results = [
        {
            "strategy": {"name": "good_strategy"},
            "result": {"net_profit": 500},
            "validation": {
                "valid": True,
                "decision": "VALID",
                "reasons": []
            }
        },
        {
            "strategy": {"name": "bad_strategy"},
            "result": {"net_profit": -100},
            "validation": {
                "valid": False,
                "decision": "INVALID",
                "reasons": ["net_profit insufficiente"]
            }
        }
    ]

    learned = core.learn_validated_strategies(validated_results)

    assert len(learned) == 1
    assert learned[0]["strategy"]["name"] == "good_strategy"
    assert learned[0]["learning"]["learned"] is True
    assert learned[0]["learning"]["decision"] == "LEARNED"

    assert len(core.learning_engine.get_learned_strategies()) == 1
    assert core.learning_engine.get_learned_strategies()[0]["strategy"]["name"] == "good_strategy"
