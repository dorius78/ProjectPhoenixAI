"""
========================================
PROJECT PHOENIX AI
Core System Tests
Versione 1.0
========================================
"""

from Core.core_system import CoreSystem


def test_core_system():

    print("\n===================================")
    print("TEST CORE SYSTEM")
    print("===================================\n")

    # =====================================
    # INIZIALIZZAZIONE
    # =====================================

    core = CoreSystem()

    assert core is not None

    # =====================================
    # MODULI PRINCIPALI
    # =====================================

    assert core.market is not None
    assert core.candles is not None
    assert core.analysis is not None
    assert core.position_controller is not None
    assert core.portfolio is not None
    assert core.execution is not None
    assert core.backtest is not None
    assert core.database is not None
    assert core.performance is not None
    assert core.scanner is not None
    assert core.live_engine is not None

    # =====================================
    # VERIFICA SCANNER
    # =====================================

    symbols = core.scanner.get_symbols()

    assert symbols is not None
    assert len(symbols) > 0

    print("Scanner strumenti:", len(symbols))

    # =====================================
    # VERIFICA PORTFOLIO
    # =====================================

    balance = core.portfolio.get_balance()

    assert balance is not None
    assert balance >= 0

    print("Portfolio balance:", balance)

    # =====================================
    # VERIFICA DATABASE
    # =====================================

    count = core.database.count()

    assert count >= 0

    print("Trade database:", count)

    print("\nOK - Core System funzionante.")


if __name__ == "__main__":
    test_core_system()