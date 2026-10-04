from Core.market_research import MarketResearch


def test_market_research():

    research = MarketResearch()

    # =====================================
    # DATABASE DI TEST
    # =====================================

    from Database.database_manager import DatabaseManager

    database = DatabaseManager(":memory:")

    database.save_trade({
        "symbol": "BTC-USD",
        "side": "BUY",
        "entry": 100,
        "exit": 110,
        "stop_loss": 95,
        "take_profit": 110,
        "pnl": 100,
        "status": "CLOSED",
        "reason": "TAKE PROFIT",
        "open_time": "2026-01-01 10:00:00",
        "close_time": "2026-01-01 12:00:00",
        "duration": 7200,
        "result": "WIN",
        "risk_reward": 2.0,
        "initial_stop_loss": 95,
        "size": 1,
        "regime": "TRENDING"
    })

    database.save_trade({
        "symbol": "BTC-USD",
        "side": "SELL",
        "entry": 100,
        "exit": 105,
        "stop_loss": 105,
        "take_profit": 90,
        "pnl": -50,
        "status": "CLOSED",
        "reason": "STOP LOSS",
        "open_time": "2026-01-02 10:00:00",
        "close_time": "2026-01-02 11:00:00",
        "duration": 3600,
        "result": "LOSS",
        "risk_reward": 1.5,
        "initial_stop_loss": 105,
        "size": 1,
        "regime": "SIDEWAYS"
    })

    # =====================================
    # MARKET RESEARCH
    # =====================================

    result = research.analyze(database)

    assert "overview" in result
    assert "symbols" in result
    assert "sides" in result
    assert "reasons" in result
    assert "regimes" in result

    # =====================================
    # OVERVIEW
    # =====================================

    assert result["overview"]["trades"] == 2
    assert result["overview"]["profit"] == 50

    # =====================================
    # SYMBOL
    # =====================================

    assert "BTC-USD" in result["symbols"]

    assert result["symbols"]["BTC-USD"]["trades"] == 2

    # =====================================
    # SIDE
    # =====================================

    assert result["sides"]["BUY"]["trades"] == 1
    assert result["sides"]["SELL"]["trades"] == 1

    # =====================================
    # REASON
    # =====================================

    assert "TAKE PROFIT" in result["reasons"]
    assert "STOP LOSS" in result["reasons"]

    # =====================================
    # REGIME
    # =====================================

    assert "TRENDING" in result["regimes"]
    assert "SIDEWAYS" in result["regimes"]


if __name__ == "__main__":
    test_market_research()
def test_market_research_details():

    from Core.market_research import MarketResearch
    from Database.database_manager import DatabaseManager

    research = MarketResearch()
    database = DatabaseManager(":memory:")

    database.save_trade({
        "symbol": "BTC-USD",
        "side": "BUY",
        "entry": 100,
        "exit": 110,
        "stop_loss": 95,
        "take_profit": 110,
        "pnl": 100,
        "status": "CLOSED",
        "reason": "TAKE PROFIT",
        "open_time": "2026-01-01 10:00:00",
        "close_time": "2026-01-01 12:00:00",
        "duration": 7200,
        "result": "WIN",
        "risk_reward": 2.0,
        "initial_stop_loss": 95,
        "size": 1,
        "regime": "TRENDING"
    })

    database.save_trade({
        "symbol": "BTC-USD",
        "side": "SELL",
        "entry": 100,
        "exit": 105,
        "stop_loss": 105,
        "take_profit": 90,
        "pnl": -50,
        "status": "CLOSED",
        "reason": "STOP LOSS",
        "open_time": "2026-01-02 10:00:00",
        "close_time": "2026-01-02 11:00:00",
        "duration": 3600,
        "result": "LOSS",
        "risk_reward": 1.5,
        "initial_stop_loss": 105,
        "size": 1,
        "regime": "SIDEWAYS"
    })

    result = research.analyze(database)

    # =====================================
    # SYMBOL
    # =====================================

    assert result["symbols"]["BTC-USD"]["profit"] == 50
    assert result["symbols"]["BTC-USD"]["wins"] == 1
    assert result["symbols"]["BTC-USD"]["losses"] == 1

    # =====================================
    # SIDE
    # =====================================

    assert result["sides"]["BUY"]["profit"] == 100
    assert result["sides"]["BUY"]["wins"] == 1

    assert result["sides"]["SELL"]["profit"] == -50
    assert result["sides"]["SELL"]["losses"] == 1

    # =====================================
    # REASON
    # =====================================

    assert result["reasons"]["TAKE PROFIT"]["profit"] == 100
    assert result["reasons"]["STOP LOSS"]["profit"] == -50

    # =====================================
    # REGIME
    # =====================================

    assert result["regimes"]["TRENDING"]["profit"] == 100
    assert result["regimes"]["SIDEWAYS"]["profit"] == -50


if __name__ == "__main__":
    test_market_research_details()
