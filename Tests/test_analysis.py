import pandas as pd

from Core.analysis_engine import AnalysisEngine


def create_test_data():
    return pd.DataFrame({
        "Open": list(range(100, 156)),
        "High": list(range(101, 157)),
        "Low": list(range(99, 155)),
        "Close": list(range(100, 156)),
        "Volume": [1000] * 56
    })


def test_analysis_engine_output_structure():
    engine = AnalysisEngine()

    data = create_test_data()

    result = engine.analyze(
        data=data,
        price=155,
        symbol="BTC-USD",
        account_balance=10000
    )

    assert isinstance(result, dict)

    assert "analysis" in result
    assert "indicators" in result
    assert "risk" in result
    assert "decision" in result
    assert "signal" in result
    assert "trade" in result


def test_risk_gate_is_present():
    engine = AnalysisEngine()

    data = create_test_data()

    result = engine.analyze(
        data=data,
        price=155,
        symbol="BTC-USD",
        account_balance=10000
    )

    assert "risk" in result

    risk = result["risk"]

    assert "allow_trade" in risk
    assert "risk_level" in risk
    assert "risk_score" in risk


def test_risk_gate_blocks_trade():
    engine = AnalysisEngine()

    engine.risk_manager.evaluate = lambda analysis: {
        "risk_level": "ALTO",
        "risk_score": 0,
        "allow_trade": False
    }

    engine.phoenix_brain.think = lambda analysis, risk: {
        "action": "STRONG BUY",
        "score": 95,
        "confidence": 100,
        "strength": 95,
        "risk": risk["risk_level"],
        "reasons": [],
        "warnings": []
    }

    data = create_test_data()

    result = engine.analyze(
        data=data,
        price=155,
        symbol="BTC-USD",
        account_balance=10000
    )

    assert result["risk"]["allow_trade"] is False
    assert result["decision"]["action"] == "STRONG BUY"

    assert result["signal"]["signal"] == "STRONG BUY"

    assert result["signal"]["valid"] is False

    assert result["trade"] is None


if __name__ == "__main__":
    test_analysis_engine_output_structure()
    test_risk_gate_is_present()
    test_risk_gate_blocks_trade()

    print("TEST ANALYSIS: OK")