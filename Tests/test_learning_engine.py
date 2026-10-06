from Core.learning_engine import LearningEngine


def valid_validation():
    return {
        "valid": True,
        "decision": "VALID",
        "reasons": []
    }


def test_learning_engine_records_learning_history():
    engine = LearningEngine()

    strategy = {
        "name": "strategy_a",
        "parameters": {
            "STOP_LOSS_ATR": 1.5
        }
    }

    result = engine.learn(strategy, valid_validation())

    assert result["learned"] is True
    assert len(engine.learning_history) == 1
    assert engine.learning_history[0]["strategy"] == strategy
    assert engine.learning_history[0]["decision"] == "LEARNED"


def test_learning_engine_records_rejected_attempt():
    engine = LearningEngine()

    strategy = {
        "name": "strategy_b"
    }

    validation = {
        "valid": False,
        "decision": "INVALID",
        "reasons": ["Drawdown troppo alto"]
    }

    result = engine.learn(strategy, validation)

    assert result["learned"] is False
    assert len(engine.learning_history) == 1
    assert engine.learning_history[0]["decision"] == "REJECTED"


def test_learning_engine_history_tracks_multiple_attempts():
    engine = LearningEngine()

    engine.learn(
        {"name": "strategy_c"},
        valid_validation()
    )

    engine.learn(
        {"name": "strategy_d"},
        {
            "valid": False,
            "decision": "INVALID",
            "reasons": ["Profitto insufficiente"]
        }
    )

    assert len(engine.learning_history) == 2


def test_learning_engine_reset_clears_history():
    engine = LearningEngine()

    engine.learn(
        {"name": "strategy_e"},
        valid_validation()
    )

    engine.reset()

    assert engine.learning_history == []
