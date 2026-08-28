import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

"""
========================================
PROJECT PHOENIX AI
Backtest Engine Tests
Versione 1.0
========================================
"""

from Core.backtest_engine import BacktestEngine


def test_backtest_engine():

    print("\n===================================")
    print("TEST BACKTEST ENGINE")
    print("===================================\n")

    engine = BacktestEngine()

    assert engine is not None

    # Impostiamo il numero di candele analizzate
    engine.set_total_bars(100)

    # =====================================
    # TRADE BUY VINCENTE
    # =====================================

    engine.add_trade({
        "symbol": "BTC-USD",
        "side": "BUY",
        "pnl": 200.0
    })

    # =====================================
    # TRADE SELL PERDENTE
    # =====================================

    engine.add_trade({
        "symbol": "BTC-USD",
        "side": "SELL",
        "pnl": -100.0
    })

    # =====================================
    # TRADE BUY VINCENTE
    # =====================================

    engine.add_trade({
        "symbol": "BTC-USD",
        "side": "BUY",
        "pnl": 300.0
    })

    report = engine.run()

    # =====================================
    # VERIFICHE
    # =====================================

    assert report["total_trades"] == 3
    assert report["closed_trades"] == 3

    assert report["buy"] == 2
    assert report["sell"] == 1

    assert report["wins"] == 2
    assert report["losses"] == 1

    assert report["win_rate"] == 66.67

    assert report["gross_profit"] == 500.0
    assert report["gross_loss"] == 100.0

    assert report["net_profit"] == 400.0

    assert report["capital"] == 10400.0

    assert report["roi"] == 4.0

    assert report["profit_factor"] == 5.0

    assert report["max_drawdown"] == 100.0

    assert report["activity"] == 3.0

    assert report["market_bias"] == "LONG"

    # =====================================
    # ULTIMO TRADE
    # =====================================

    last = engine.last_trade()

    assert last is not None
    assert last["pnl"] == 300.0

    print("OK - Backtest Engine funzionante.")


if __name__ == "__main__":
    test_backtest_engine()