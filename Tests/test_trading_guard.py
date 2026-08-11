"""
========================================
PROJECT PHOENIX AI
Trading Guard Tests
Versione 1.0
========================================
"""

from Core.trading_guard import TradingGuard


def test_initial_state():

    guard = TradingGuard(10000.0)

    assert guard.day_start_balance == 10000.0
    assert guard.daily_pnl == 0.0
    assert guard.consecutive_losses == 0


def test_can_trade_initially():

    guard = TradingGuard(10000.0)

    can_trade, reason = guard.can_trade(10000.0)

    assert can_trade is True
    assert reason is None


def test_register_profit():

    guard = TradingGuard(10000.0)

    guard.register_trade(
        100.0,
        10100.0
    )

    assert guard.daily_pnl == 100.0
    assert guard.consecutive_losses == 0


def test_register_loss():

    guard = TradingGuard(10000.0)

    guard.register_trade(
        -100.0,
        9900.0
    )

    assert guard.daily_pnl == -100.0
    assert guard.consecutive_losses == 1


def test_consecutive_losses():

    guard = TradingGuard(10000.0)

    guard.register_trade(
        -100.0,
        9900.0
    )

    guard.register_trade(
        -100.0,
        9800.0
    )

    assert guard.consecutive_losses == 2


def test_profit_resets_consecutive_losses():

    guard = TradingGuard(10000.0)

    guard.register_trade(
        -100.0,
        9900.0
    )

    guard.register_trade(
        -100.0,
        9800.0
    )

    guard.register_trade(
        300.0,
        10100.0
    )

    assert guard.consecutive_losses == 0
    assert guard.daily_pnl == 100.0


def test_daily_loss_limit():

    guard = TradingGuard(10000.0)

    guard.register_trade(
        -500.0,
        9500.0
    )

    can_trade, reason = guard.can_trade(9500.0)

    assert can_trade is False
    assert reason is not None
    assert "Limite perdita giornaliera" in reason


def test_consecutive_loss_limit():

    guard = TradingGuard(10000.0)

    guard.register_trade(
        -50.0,
        9950.0
    )

    guard.register_trade(
        -50.0,
        9900.0
    )

    guard.register_trade(
        -50.0,
        9850.0
    )

    guard.register_trade(
        -50.0,
        9800.0
    )

    can_trade, reason = guard.can_trade(9800.0)

    assert can_trade is False
    assert reason is not None
    assert "Troppe perdite consecutive" in reason


if __name__ == "__main__":

    test_initial_state()
    test_can_trade_initially()
    test_register_profit()
    test_register_loss()
    test_consecutive_losses()
    test_profit_resets_consecutive_losses()
    test_daily_loss_limit()
    test_consecutive_loss_limit()

    print("TEST TRADING GUARD: OK")