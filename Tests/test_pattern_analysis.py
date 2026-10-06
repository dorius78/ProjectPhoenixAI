from Core.pattern_analysis import PatternAnalysis


def test_pattern_analysis():

    engine = PatternAnalysis()

    trades = [
        {
            "side": "BUY",
            "reason": "TAKE PROFIT",
            "regime": "TRENDING",
            "pnl": 100
        },
        {
            "side": "BUY",
            "reason": "TAKE PROFIT",
            "regime": "TRENDING",
            "pnl": 50
        },
        {
            "side": "SELL",
            "reason": "STOP LOSS",
            "regime": "SIDEWAYS",
            "pnl": -50
        }
    ]

    result = engine.analyze(trades)

    assert "patterns" in result
    assert len(result["patterns"]) == 2

    trending = result["patterns"]["('BUY', 'TAKE PROFIT', 'TRENDING')"]

    assert trending["trades"] == 2
    assert trending["profit"] == 150
    assert trending["wins"] == 2
    assert trending["losses"] == 0

    sideways = result["patterns"]["('SELL', 'STOP LOSS', 'SIDEWAYS')"]

    assert sideways["trades"] == 1
    assert sideways["profit"] == -50
    assert sideways["wins"] == 0
    assert sideways["losses"] == 1
