from Core.learning_engine import LearningEngine


def valid_validation():
    return {
        "valid": True,
        "decision": "VALID",
        "reasons": []
    }


def test_learning_engine_returns_learned_strategies():
    engine = LearningEngine()

    strategy = {
        "name": "strategy_a",
        "parameters": {
            "STOP_LOSS_ATR": 1.5
        }
    }

    engine.learn(strategy, valid_validation())

    result = engine.get_learned_strategies()

    assert len(result) == 1
    assert result[0]["strategy"] == strategy


def test_learning_engine_returns_empty_list_when_nothing_learned():
    engine = LearningEngine()

    result = engine.get_learned_strategies()

    assert result == []


def test_learning_engine_returns_copy_of_learned_strategies():
    engine = LearningEngine()

    strategy = {
        "name": "strategy_b"
    }

    engine.learn(strategy, valid_validation())

    result = engine.get_learned_strategies()
    result.clear()

    assert len(engine.learned_strategies) == 1


def test_learning_engine_does_not_return_rejected_strategies():
    engine = LearningEngine()

    engine.learn(
        {"name": "strategy_c"},
        {
            "valid": False,
            "decision": "INVALID",
            "reasons": ["Drawdown troppo alto"]
        }
    )

    assert engine.get_learned_strategies() == []
