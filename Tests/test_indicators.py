"""
PROJECT PHOENIX AI
Test Indicator Manager
"""

from Data.Indicators.indicator_manager import IndicatorManager


def test_indicator_manager():

    print("\n===================================")
    print("TEST INDICATOR MANAGER")
    print("===================================\n")

    manager = IndicatorManager()

    assert manager is not None

    print("OK - Indicator Manager inizializzato.")


if __name__ == "__main__":

    test_indicator_manager()