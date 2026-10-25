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

def test_market_research_duration_and_risk_reward():

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
    # DURATA
    # =====================================

    assert "duration" in result

    assert result["duration"]["trades"] == 2
    assert result["duration"]["average"] == 5400
    assert result["duration"]["minimum"] == 3600
    assert result["duration"]["maximum"] == 7200

    # =====================================
    # RISK / REWARD
    # =====================================

    assert "risk_reward" in result

    assert result["risk_reward"]["trades"] == 2
    assert result["risk_reward"]["average"] == 1.75
    assert result["risk_reward"]["minimum"] == 1.5
    assert result["risk_reward"]["maximum"] == 2.0


if __name__ == "__main__":
    test_market_research_duration_and_risk_reward()

def test_market_research_hourly():

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
        "open_time": "2026-01-01 10:30:00",
        "close_time": "2026-01-01 12:00:00",
        "duration": 5400,
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
        "open_time": "2026-01-01 15:45:00",
        "close_time": "2026-01-01 16:30:00",
        "duration": 2700,
        "result": "LOSS",
        "risk_reward": 1.5,
        "initial_stop_loss": 105,
        "size": 1,
        "regime": "SIDEWAYS"
    })

    result = research.analyze(database)

    # =====================================
    # FASCIA ORARIA
    # =====================================

    assert "hours" in result

    assert result["hours"]["10"]["trades"] == 1
    assert result["hours"]["10"]["profit"] == 100
    assert result["hours"]["10"]["wins"] == 1

    assert result["hours"]["15"]["trades"] == 1
    assert result["hours"]["15"]["profit"] == -50
    assert result["hours"]["15"]["losses"] == 1


if __name__ == "__main__":
    test_market_research_hourly()

def test_market_research_historical_schema_column_order():
    import sqlite3
    from Core.market_research import MarketResearch

    class HistoricalSchemaDatabase:
        def __init__(self):
            self.connection = sqlite3.connect(":memory:")
            self.cursor = self.connection.cursor()

            self.cursor.execute("""
                CREATE TABLE trades (
                    id INTEGER PRIMARY KEY,
                    symbol TEXT,
                    side TEXT,
                    entry REAL,
                    exit REAL,
                    stop_loss REAL,
                    take_profit REAL,
                    pnl REAL,
                    status TEXT,
                    reason TEXT,
                    open_time TEXT,
                    close_time TEXT,
                    duration REAL,
                    result TEXT,
                    risk_reward REAL,
                    initial_stop_loss REAL,
                    size REAL,
                    regime TEXT
                )
            """)

            self.cursor.executemany("""
                INSERT INTO trades VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
            """, [
                (
                    1, "BTC-USD", "BUY", 100, 110, 95, 110,
                    125, "CLOSED", "TAKE PROFIT",
                    "2026-01-01 10:00:00", "2026-01-01 12:00:00",
                    7200, "WIN", 2.5, 95, 1, "TRENDING"
                ),
                (
                    2, "BTC-USD", "SELL", 100, 105, 105, 90,
                    -25, "CLOSED", "STOP LOSS",
                    "2026-01-02 15:00:00", "2026-01-02 16:00:00",
                    3600, "LOSS", 1.5, 105, 1, None
                )
            ])
            self.connection.commit()

        def load_trades(self):
            self.cursor.execute("SELECT * FROM trades ORDER BY id DESC")
            return self.cursor.fetchall()

        def close(self):
            self.connection.close()

    database = HistoricalSchemaDatabase()

    try:
        result = MarketResearch().analyze(database)

        assert result["overview"]["trades"] == 2
        assert result["overview"]["profit"] == 100

        assert result["duration"]["average"] == 5400
        assert result["risk_reward"]["average"] == 2.0

        assert result["reasons"]["TAKE PROFIT"]["profit"] == 125
        assert result["reasons"]["STOP LOSS"]["profit"] == -25

        assert result["hours"]["10"]["profit"] == 125
        assert result["hours"]["15"]["profit"] == -25

        assert result["regimes"]["TRENDING"]["profit"] == 125
        assert None not in result["regimes"]
        assert "NONE" not in result["regimes"]

    finally:
        database.close()
