from Core.learning_engine import LearningEngine


def valid_validation():
    return {
        "valid": True,
        "decision": "VALID",
        "reasons": []
    }


def test_learning_engine_returns_history():
    engine = LearningEngine()

    strategy = {"name": "strategy_a"}

    engine.learn(strategy, valid_validation())

    result = engine.get_learning_history()

    assert len(result) == 1
    assert result[0]["strategy"] == strategy
    assert result[0]["decision"] == "LEARNED"


def test_learning_engine_returns_empty_history_initially():
    engine = LearningEngine()

    assert engine.get_learning_history() == []


def test_learning_engine_returns_history_copy():
    engine = LearningEngine()

    engine.learn(
        {"name": "strategy_b"},
        valid_validation()
    )

    result = engine.get_learning_history()
    result.clear()

    assert len(engine.learning_history) == 1


def test_learning_engine_history_includes_rejected_attempts():
    engine = LearningEngine()

    engine.learn(
        {"name": "strategy_c"},
        {
            "valid": False,
            "decision": "INVALID",
            "reasons": ["Drawdown troppo alto"]
        }
    )

    result = engine.get_learning_history()

    assert len(result) == 1
    assert result[0]["decision"] == "REJECTED"
