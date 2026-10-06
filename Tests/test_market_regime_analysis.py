from Core.market_regime_analysis import MarketRegimeAnalysis


def test_market_regime_analysis():

    engine = MarketRegimeAnalysis()

    trades = [
        {
            "regime": "TRENDING",
            "pnl": 100,
            "duration": 7200,
            "risk_reward": 2.0
        },
        {
            "regime": "TRENDING",
            "pnl": 50,
            "duration": 3600,
            "risk_reward": 1.5
        },
        {
            "regime": "SIDEWAYS",
            "pnl": -50,
            "duration": 1800,
            "risk_reward": 1.0
        }
    ]

    result = engine.analyze(trades)

    assert "regimes" in result
    assert "TRENDING" in result["regimes"]
    assert "SIDEWAYS" in result["regimes"]

    trending = result["regimes"]["TRENDING"]

    assert trending["trades"] == 2
    assert trending["profit"] == 150
    assert trending["wins"] == 2
    assert trending["losses"] == 0
    assert trending["win_rate"] == 100.0
    assert trending["average_pnl"] == 75.0
    assert trending["average_duration"] == 5400.0
    assert trending["average_risk_reward"] == 1.75

    sideways = result["regimes"]["SIDEWAYS"]

    assert sideways["trades"] == 1
    assert sideways["profit"] == -50
    assert sideways["wins"] == 0
    assert sideways["losses"] == 1

    assert result["best_regime"] == "TRENDING"
    assert result["worst_regime"] == "SIDEWAYS"
