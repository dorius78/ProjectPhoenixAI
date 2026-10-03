from Core.strategy_discovery import StrategyDiscovery


def test_strategy_discovery():

    discovery = StrategyDiscovery()

    # =====================================
    # GENERAZIONE CANDIDATI
    # =====================================

    parameter_space = {
        "rsi": [30, 40],
        "rr": [1.5, 2.0]
    }

    candidates = discovery.generate_candidates(
        parameter_space
    )

    assert len(candidates) == 4

    assert {
        "rsi": 30,
        "rr": 1.5
    } in candidates

    assert {
        "rsi": 40,
        "rr": 2.0
    } in candidates

    # =====================================
    # VALUTAZIONE
    # =====================================

    def fake_backtest(candidate):

        return {
            "profit": candidate["rsi"] + candidate["rr"]
        }

    result = discovery.evaluate_candidate(
        candidates[0],
        fake_backtest
    )

    assert "strategy" in result
    assert "result" in result
    assert "profit" in result["result"]

    # =====================================
    # RANKING
    # =====================================

    results = [
        discovery.evaluate_candidate(
            candidate,
            fake_backtest
        )
        for candidate in candidates
    ]

    ranked = discovery.rank_candidates(
        results,
        metric="profit"
    )

    assert len(ranked) == 4

    assert ranked[0]["result"]["profit"] >= \
           ranked[-1]["result"]["profit"]

    # =====================================
    # BEST
    # =====================================

    best = discovery.get_best(
        results,
        metric="profit"
    )

    assert best is not None

    assert best["result"]["profit"] == \
           max(
               item["result"]["profit"]
               for item in results
           )

    # =====================================
    # RESET
    # =====================================

    discovery.reset()

    assert discovery.candidates == []


if __name__ == "__main__":
    test_strategy_discovery()

def test_strategy_discovery_parameter_restore():

    from Config import settings

    discovery = StrategyDiscovery()

    original = settings.PHOENIX_MIN_CONFIDENCE

    discovery.apply_parameters(
        {
            "PHOENIX_MIN_CONFIDENCE": 99
        }
    )

    assert settings.PHOENIX_MIN_CONFIDENCE == 99

    discovery.restore_parameters(
        {
            "PHOENIX_MIN_CONFIDENCE": original
        }
    )

    assert settings.PHOENIX_MIN_CONFIDENCE == original
