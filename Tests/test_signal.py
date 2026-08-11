from Core.signal_manager import SignalManager
from Config.settings import MIN_CONFIDENCE


def test_strong_buy_is_valid():
    manager = SignalManager()

    decision = {
        "action": "STRONG BUY",
        "score": 90,
        "confidence": 40,
        "reasons": ["Trend rialzista"]
    }

    result = manager.validate(decision)

    assert result["valid"] is True
    assert result["signal"] == "STRONG BUY"


def test_strong_sell_is_valid():
    manager = SignalManager()

    decision = {
        "action": "STRONG SELL",
        "score": 10,
        "confidence": 40,
        "reasons": ["Trend ribassista"]
    }

    result = manager.validate(decision)

    assert result["valid"] is True
    assert result["signal"] == "STRONG SELL"


def test_buy_requires_minimum_confidence():
    manager = SignalManager()

    decision = {
        "action": "BUY",
        "score": 70,
        "confidence": MIN_CONFIDENCE,
        "reasons": []
    }

    result = manager.validate(decision)

    assert result["valid"] is True
    assert result["signal"] == "BUY"


def test_buy_below_minimum_confidence_is_invalid():
    manager = SignalManager()

    decision = {
        "action": "BUY",
        "score": 70,
        "confidence": MIN_CONFIDENCE - 1,
        "reasons": []
    }

    result = manager.validate(decision)

    assert result["valid"] is False


def test_sell_requires_minimum_confidence():
    manager = SignalManager()

    decision = {
        "action": "SELL",
        "score": 30,
        "confidence": MIN_CONFIDENCE,
        "reasons": []
    }

    result = manager.validate(decision)

    assert result["valid"] is True
    assert result["signal"] == "SELL"


def test_sell_below_minimum_confidence_is_invalid():
    manager = SignalManager()

    decision = {
        "action": "SELL",
        "score": 30,
        "confidence": MIN_CONFIDENCE - 1,
        "reasons": []
    }

    result = manager.validate(decision)

    assert result["valid"] is False


def test_hold_is_invalid():
    manager = SignalManager()

    decision = {
        "action": "HOLD",
        "score": 50,
        "confidence": 50,
        "reasons": []
    }

    result = manager.validate(decision)

    assert result["valid"] is False
    assert result["signal"] == "HOLD"


def test_invalid_signal_is_invalid():
    manager = SignalManager()

    decision = {
        "action": "INVALID",
        "score": 50,
        "confidence": 100,
        "reasons": []
    }

    result = manager.validate(decision)

    assert result["valid"] is False


def test_generate_signal_blocks_trade_when_risk_is_not_allowed():
    manager = SignalManager()

    decision = {
        "action": "STRONG BUY",
        "score": 95,
        "confidence": 100,
        "reasons": []
    }

    brain = {
        "action": "STRONG BUY"
    }

    risk = {
        "allow_trade": False
    }

    result = manager.generate_signal(
        decision,
        brain,
        risk
    )

    assert result == "HOLD"


def test_generate_signal_allows_buy_when_risk_is_allowed():
    manager = SignalManager()

    decision = {
        "action": "BUY",
        "score": 70,
        "confidence": 80,
        "reasons": []
    }

    brain = {
        "action": "BUY"
    }

    risk = {
        "allow_trade": True
    }

    result = manager.generate_signal(
        decision,
        brain,
        risk
    )

    assert result == "BUY"


def test_generate_signal_allows_sell_when_risk_is_allowed():
    manager = SignalManager()

    decision = {
        "action": "SELL",
        "score": 30,
        "confidence": 80,
        "reasons": []
    }

    brain = {
        "action": "SELL"
    }

    risk = {
        "allow_trade": True
    }

    result = manager.generate_signal(
        decision,
        brain,
        risk
    )

    assert result == "SELL"


if __name__ == "__main__":
    test_strong_buy_is_valid()
    test_strong_sell_is_valid()
    test_buy_requires_minimum_confidence()
    test_buy_below_minimum_confidence_is_invalid()
    test_sell_requires_minimum_confidence()
    test_sell_below_minimum_confidence_is_invalid()
    test_hold_is_invalid()
    test_invalid_signal_is_invalid()
    test_generate_signal_blocks_trade_when_risk_is_not_allowed()
    test_generate_signal_allows_buy_when_risk_is_allowed()
    test_generate_signal_allows_sell_when_risk_is_allowed()

    print("TEST SIGNAL: OK")