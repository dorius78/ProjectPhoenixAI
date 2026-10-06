from Core.learning_engine import LearningEngine


def valid_validation():
    return {
        "valid": True,
        "decision": "VALID",
        "reasons": []
    }


def test_learning_engine_stores_approved_strategy():
    engine = LearningEngine()

    strategy = {
        "name": "strategy_a",
        "parameters": {
            "STOP_LOSS_ATR": 1.5
        }
    }

    result = engine.learn(strategy, valid_validation())

    assert result["learned"] is True
    assert result["decision"] == "LEARNED"
    assert len(engine.learned_strategies) == 1
    assert engine.learned_strategies[0] == strategy


def test_learning_engine_does_not_store_rejected_strategy():
    engine = LearningEngine()

    strategy = {
        "name": "strategy_b"
    }

    validation = {
        "valid": False,
        "decision": "INVALID",
        "reasons": ["net_profit insufficiente"]
    }

    result = engine.learn(strategy, validation)

    assert result["learned"] is False
    assert result["decision"] == "REJECTED"
    assert engine.learned_strategies == []


def test_learning_engine_does_not_duplicate_strategy():
    engine = LearningEngine()

    strategy = {
        "name": "strategy_c",
        "parameters": {
            "STOP_LOSS_ATR": 1.5
        }
    }

    engine.learn(strategy, valid_validation())
    engine.learn(strategy, valid_validation())

    assert len(engine.learned_strategies) == 1


def test_learning_engine_reset_clears_learned_strategies():
    engine = LearningEngine()

    strategy = {
        "name": "strategy_d"
    }

    engine.learn(strategy, valid_validation())
    engine.reset()

    assert engine.learned_strategies == []
