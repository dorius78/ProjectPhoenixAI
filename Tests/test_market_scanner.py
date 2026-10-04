import os
import sys

ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from Core.market_scanner import MarketScanner


def test_market_scanner_watchlist():

    scanner = MarketScanner()

    scanner.load_default()

    assert len(scanner.get_symbols()) == 12
    assert "BTC-USD" in scanner.get_symbols()
    assert "EURUSD=X" in scanner.get_symbols()


def test_market_scanner_sort():

    scanner = MarketScanner()

    scanner.add_result("BTC-USD", "BUY", 40, 70)
    scanner.add_result("EURUSD=X", "SELL", 80, 75)
    scanner.add_result("ETH-USD", "HOLD", 20, 60)

    scanner.sort()

    assert scanner.results[0]["symbol"] == "EURUSD=X"
    assert scanner.results[1]["symbol"] == "BTC-USD"
    assert scanner.results[2]["symbol"] == "ETH-USD"


def test_market_scanner_best_opportunity():

    scanner = MarketScanner()

    scanner.add_result("BTC-USD", "BUY", 40, 70)
    scanner.add_result("EURUSD=X", "SELL", 80, 75)
    scanner.add_result("ETH-USD", "HOLD", 100, 90)

    scanner._is_mt5_market_active = lambda symbol: True

    best = scanner.get_best_opportunity()

    assert best is not None
    assert best["symbol"] == "EURUSD=X"
    assert best["decision"] == "SELL"
    assert best["score"] == 80


def test_market_scanner_reset():

    scanner = MarketScanner()

    scanner.add_result("BTC-USD", "BUY", 50, 70)

    assert len(scanner.results) == 1

    scanner.reset()

    assert scanner.results == []


if __name__ == "__main__":

    test_market_scanner_watchlist()
    test_market_scanner_sort()
    test_market_scanner_best_opportunity()
    test_market_scanner_reset()

    print("TEST MARKET SCANNER: OK")
