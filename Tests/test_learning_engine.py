from Core.learning_engine import LearningEngine


def test_learning_engine_approves_valid_strategy():
    engine = LearningEngine()

    validation = {
        "valid": True,
        "decision": "VALID",
        "reasons": []
    }

    result = engine.approve(
        {"name": "strategy_a"},
        validation
    )

    assert result["approved"] is True
    assert result["decision"] == "APPROVED"


def test_learning_engine_rejects_invalid_strategy():
    engine = LearningEngine()

    validation = {
        "valid": False,
        "decision": "INVALID",
        "reasons": ["net_profit insufficiente"]
    }

    result = engine.approve(
        {"name": "strategy_b"},
        validation
    )

    assert result["approved"] is False
    assert result["decision"] == "REJECTED"


def test_learning_engine_does_not_approve_without_validation():
    engine = LearningEngine()

    result = engine.approve(
        {"name": "strategy_c"},
        None
    )

    assert result["approved"] is False
    assert result["decision"] == "REJECTED"


def test_learning_engine_does_not_modify_strategy():
    engine = LearningEngine()

    strategy = {
        "name": "strategy_d",
        "parameters": {
            "STOP_LOSS_ATR": 1.5
        }
    }

    validation = {
        "valid": True,
        "decision": "VALID",
        "reasons": []
    }

    original = strategy.copy()

    engine.approve(strategy, validation)

    assert strategy == original
