"""
========================================
PROJECT PHOENIX AI
Research Aggregator
Versione 1.0
========================================
"""

from Logs.logger import Logger


class ResearchAggregator:

    def __init__(self):
        Logger.success(
            "Research Aggregator V1 inizializzato."
        )

    def analyze(
        self,
        market_research=None,
        pattern_analysis=None,
        market_regime_analysis=None
    ):
        return {
            "market_research": (
                market_research
                if isinstance(market_research, dict)
                else {}
            ),
            "pattern_analysis": (
                pattern_analysis
                if isinstance(pattern_analysis, dict)
                else {}
            ),
            "market_regime_analysis": (
                market_regime_analysis
                if isinstance(market_regime_analysis, dict)
                else {}
            )
        }
