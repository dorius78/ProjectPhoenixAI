from Core.learning_engine import LearningEngine


def valid_validation():
    return {
        "valid": True,
        "decision": "VALID",
        "reasons": []
    }


def test_learning_engine_stores_strategy_and_validation():
    engine = LearningEngine()

    strategy = {
        "name": "strategy_a",
        "parameters": {
            "STOP_LOSS_ATR": 1.5
        }
    }

    validation = valid_validation()

    result = engine.learn(strategy, validation)

    assert result["learned"] is True
    assert len(engine.learned_strategies) == 1
    assert engine.learned_strategies[0]["strategy"] == strategy
    assert engine.learned_strategies[0]["validation"] == validation


def test_learning_engine_stores_validation_reasons():
    engine = LearningEngine()

    strategy = {
        "name": "strategy_b"
    }

    validation = {
        "valid": True,
        "decision": "VALID",
        "reasons": ["Robustez confermata"]
    }

    engine.learn(strategy, validation)

    learned = engine.learned_strategies[0]

    assert learned["validation"]["reasons"] == [
        "Robustez confermata"
    ]


def test_learning_engine_does_not_duplicate_strategy():
    engine = LearningEngine()

    strategy = {
        "name": "strategy_c",
        "parameters": {
            "STOP_LOSS_ATR": 1.5
        }
    }

    validation = valid_validation()

    engine.learn(strategy, validation)
    engine.learn(strategy, validation)

    assert len(engine.learned_strategies) == 1


def test_learning_engine_rejects_invalid_validation():
    engine = LearningEngine()

    strategy = {
        "name": "strategy_d"
    }

    validation = {
        "valid": False,
        "decision": "INVALID",
        "reasons": ["Drawdown troppo alto"]
    }

    result = engine.learn(strategy, validation)

    assert result["learned"] is False
    assert engine.learned_strategies == []
