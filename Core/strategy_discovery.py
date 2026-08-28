"""
========================================
PROJECT PHOENIX AI
Strategy Discovery
E75
========================================
"""

from itertools import product

from Logs.logger import Logger


class StrategyDiscovery:

    def __init__(self):

        self.candidates = []

        Logger.success(
            "Strategy Discovery V1 inizializzato."
        )

    # =====================================
    # GENERAZIONE STRATEGIE
    # =====================================

    def generate_candidates(self, parameter_space):

        self.candidates = []

        if not parameter_space:
            return []

        keys = list(parameter_space.keys())

        values = [
            parameter_space[key]
            for key in keys
        ]

        for combination in product(*values):

            candidate = dict(
                zip(keys, combination)
            )

            self.candidates.append(
                candidate
            )

        Logger.info(
            f"Strategie candidate generate: "
            f"{len(self.candidates)}"
        )

        return self.candidates

    # =====================================
    # VALUTAZIONE
    # =====================================

    def evaluate_candidate(
        self,
        candidate,
        backtest_function
    ):

        if not callable(backtest_function):
            raise ValueError(
                "backtest_function non valida."
            )

        result = backtest_function(
            candidate
        )

        if not isinstance(result, dict):
            result = {
                "result": result
            }

        return {
            "strategy": candidate,
            "result": result
        }

    # =====================================
    # RANKING
    # =====================================

    def rank_candidates(
        self,
        results,
        metric="profit"
    ):

        if not results:
            return []

        def score(item):

            result = item.get(
                "result",
                {}
            )

            value = result.get(
                metric,
                0
            )

            try:
                return float(value)
            except (
                TypeError,
                ValueError
            ):
                return 0.0

        ranked = sorted(
            results,
            key=score,
            reverse=True
        )

        return ranked

    # =====================================
    # MIGLIORE STRATEGIA
    # =====================================

    def get_best(
        self,
        results,
        metric="profit"
    ):

        ranked = self.rank_candidates(
            results,
            metric
        )

        if not ranked:
            return None

        return ranked[0]

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        self.candidates.clear()

        Logger.info(
            "Strategy Discovery azzerato."
        )
