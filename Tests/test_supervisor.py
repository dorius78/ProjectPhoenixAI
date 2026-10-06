from Core.supervisor import Supervisor


def create_valid_decision():
    return {
        "action": "BUY",
        "confidence": 80
    }


def create_valid_risk():
    return {
        "allow_trade": True
    }


def create_valid_regime():
    return {
        "regime": "TRENDING"
    }


def create_valid_analysis():
    return {}


def test_supervisor_allows_valid_decision():

    supervisor = Supervisor()

    result = supervisor.evaluate(
        create_valid_decision(),
        create_valid_risk(),
        create_valid_regime(),
        create_valid_analysis()
    )

    assert result["decision"] == "ALLOW"
    assert result["allowed"] is True


def test_supervisor_blocks_hold():

    supervisor = Supervisor()

    decision = {
        "action": "HOLD",
        "confidence": 80
    }

    result = supervisor.evaluate(
        decision,
        create_valid_risk(),
        create_valid_regime(),
        create_valid_analysis()
    )

    assert result["decision"] == "BLOCK"
    assert result["allowed"] is False


def test_supervisor_blocks_risk():

    supervisor = Supervisor()

    risk = {
        "allow_trade": False
    }

    result = supervisor.evaluate(
        create_valid_decision(),
        risk,
        create_valid_regime(),
        create_valid_analysis()
    )

    assert result["decision"] == "BLOCK"
    assert result["allowed"] is False


def test_supervisor_blocks_sideways():

    supervisor = Supervisor()

    regime = {
        "regime": "SIDEWAYS"
    }

    result = supervisor.evaluate(
        create_valid_decision(),
        create_valid_risk(),
        regime,
        create_valid_analysis()
    )

    assert result["decision"] == "BLOCK"
    assert result["allowed"] is False


def test_supervisor_blocks_low_confidence():

    supervisor = Supervisor()

    decision = {
        "action": "BUY",
        "confidence": 20
    }

    result = supervisor.evaluate(
        decision,
        create_valid_risk(),
        create_valid_regime(),
        create_valid_analysis()
    )

    assert result["decision"] == "BLOCK"
    assert result["allowed"] is False
from Core.supervisor import Supervisor


def test_supervisor_blocks_conflicting_buy():

    supervisor = Supervisor()

    decision = {
        "action": "BUY",
        "confidence": 70,
        "bullish_score": 50,
        "bearish_score": 40,
        "net_advantage": 10,
        "conflict": True
    }

    result = supervisor.evaluate(
        decision,
        {"allow_trade": True},
        {"regime": "TRENDING"},
        {}
    )

    assert result["decision"] == "BLOCK"
    assert result["allowed"] is False
    assert any(
        "conflitto" in reason.lower()
        for reason in result["reasons"]
    )
