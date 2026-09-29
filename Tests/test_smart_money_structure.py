import pandas as pd

from Core.smart_money_structure import SmartMoneyStructure


def test_swing_becomes_available_only_after_confirmation():
    data = pd.DataFrame({
        "Open":  [100, 101, 102, 103, 104, 105, 106],
        "High":  [101, 103, 110, 105, 106, 108, 109],
        "Low":   [99, 100, 101, 102, 103, 104, 105],
        "Close": [100, 102, 109, 104, 105, 107, 108],
        "Volume": [1000] * 7,
    })

    structure = SmartMoneyStructure()

    before_confirmation = data.iloc[:4]
    highs_before, lows_before = structure._find_swings(
        before_confirmation,
        strength=2
    )

    assert highs_before == []
    assert lows_before == []

    after_confirmation = data.iloc[:5]
    highs_after, lows_after = structure._find_swings(
        after_confirmation,
        strength=2
    )

    assert highs_after == [
        {"index": 2, "price": 110.0}
    ]
    assert lows_after == []
