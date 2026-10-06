from Core.market_research import MarketResearch
from Core.pattern_analysis import PatternAnalysis
from Core.market_regime_analysis import MarketRegimeAnalysis
from Core.research_aggregator import ResearchAggregator


def test_research_components_available():

    market_research = MarketResearch()
    pattern_analysis = PatternAnalysis()
    regime_analysis = MarketRegimeAnalysis()
    aggregator = ResearchAggregator()

    assert market_research is not None
    assert pattern_analysis is not None
    assert regime_analysis is not None
    assert aggregator is not None


def test_research_aggregator_combines_results():

    aggregator = ResearchAggregator()

    market_research = {
        "overview": {
            "trades": 10,
            "profit": 100.0
        }
    }

    pattern_analysis = {
        "patterns": {
            "('BUY', 'SIGNAL', 'TRENDING')": {
                "trades": 5,
                "profit": 80.0,
                "wins": 4,
                "losses": 1
            }
        }
    }

    market_regime_analysis = {
        "regimes": {
            "TRENDING": {
                "trades": 5,
                "profit": 80.0
            }
        },
        "best_regime": "TRENDING",
        "worst_regime": "SIDEWAYS"
    }

    result = aggregator.analyze(
        market_research,
        pattern_analysis,
        market_regime_analysis
    )

    assert result["market_research"] == market_research
    assert result["pattern_analysis"] == pattern_analysis
    assert result["market_regime_analysis"] == market_regime_analysis
