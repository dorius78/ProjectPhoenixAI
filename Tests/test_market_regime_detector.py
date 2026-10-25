from Core.market_regime_detector import MarketRegimeDetector


def test_detect_supports_new_bollinger_keys():
    result = MarketRegimeDetector().detect({
        "atr": 1.0,
        "adx": 10.0,
        "bb_upper": 101.0,
        "bb_lower": 99.0,
        "price": 1000.0,
    })

    assert result["regime"] == "LOW_VOLATILITY"
    assert result["bollinger_width"] == 2.0
    assert result["volatility_ratio"] == 0.001


def test_detect_supports_legacy_bollinger_keys():
    result = MarketRegimeDetector().detect({
        "atr": 1.0,
        "adx": 10.0,
        "bollinger_upper": 101.0,
        "bollinger_lower": 99.0,
        "price": 1000.0,
    })

    assert result["regime"] == "LOW_VOLATILITY"
    assert result["bollinger_width"] == 2.0


def test_new_bollinger_keys_take_priority_over_legacy_keys():
    result = MarketRegimeDetector().detect({
        "atr": 1.0,
        "adx": 10.0,
        "bb_upper": 101.0,
        "bb_lower": 99.0,
        "bollinger_upper": 120.0,
        "bollinger_lower": 80.0,
        "price": 1000.0,
    })

    assert result["bollinger_width"] == 2.0


def test_detect_returns_unknown_when_price_is_missing():
    result = MarketRegimeDetector().detect({
        "atr": 1.0,
        "adx": 10.0,
        "bb_upper": 101.0,
        "bb_lower": 99.0,
    })

    assert result["regime"] == "UNKNOWN"
    assert result["confidence"] == 0.0
