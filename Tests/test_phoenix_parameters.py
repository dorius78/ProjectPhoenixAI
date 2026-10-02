from Config import settings


def test_phoenix_brain_parameter_set():
    assert settings.PHOENIX_WEIGHT_TREND == 20
    assert settings.PHOENIX_WEIGHT_EMA == 10
    assert settings.PHOENIX_WEIGHT_MACD == 10
    assert settings.PHOENIX_WEIGHT_RSI == 15
    assert settings.PHOENIX_WEIGHT_ADX == 10
    assert settings.PHOENIX_WEIGHT_VOLUME == 10
    assert settings.PHOENIX_WEIGHT_BOS == 15
    assert settings.PHOENIX_WEIGHT_CHOCH == 10
    assert settings.PHOENIX_WEIGHT_FVG == 8
    assert settings.PHOENIX_WEIGHT_ORDER_BLOCK == 10
    assert settings.PHOENIX_WEIGHT_LIQUIDITY == 8

    assert settings.PHOENIX_CONFLICT_THRESHOLD == 15
    assert settings.PHOENIX_MIN_ADVANTAGE == 15
    assert settings.PHOENIX_MIN_CONFIDENCE == 30
    assert settings.PHOENIX_STRONG_ADVANTAGE == 35
    assert settings.PHOENIX_STRONG_CONFIDENCE == 65

    assert settings.PHOENIX_CONFIDENCE_NO_CONFLICT_BONUS == 10
    assert settings.PHOENIX_CONFIDENCE_CONFLICT_PENALTY == 10
    assert settings.PHOENIX_CONFIDENCE_RISK_MEDIUM_PENALTY == 10
    assert settings.PHOENIX_CONFIDENCE_RISK_HIGH_PENALTY == 20
