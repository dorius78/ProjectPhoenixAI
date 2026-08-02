"""
========================================
PROJECT PHOENIX AI
Analysis Engine
Versione 7.0
========================================
"""

from Logs.logger import Logger

from Data.Indicators.indicator_manager import IndicatorManager

from Core.market_analyzer import MarketAnalyzer
from Core.phoenix_brain import PhoenixBrain
from Core.decision_engine import DecisionEngine
from Core.signal_manager import SignalManager
from Core.trade_manager import TradeManager


class AnalysisEngine:

    def __init__(self):

        Logger.success("Analysis Engine V7 inizializzato.")

        self.indicator_manager = IndicatorManager()
        self.market_analyzer = MarketAnalyzer()
        self.phoenix_brain = PhoenixBrain()
        self.decision_engine = DecisionEngine()
        self.signal_manager = SignalManager()
        self.trade_manager = TradeManager()

    def analyze(self, data, price):

        Logger.section("ANALYSIS ENGINE")

        indicators = self.indicator_manager.get_indicators(data)

        analysis = self.market_analyzer.analyze(indicators)

        brain = self.phoenix_brain.think(
            analysis,
            {
                "risk_level": "MEDIO",
                "risk_score": 50,
                "allow_trade": True
            }
        )

        decision = self.decision_engine.analyze(
            brain["action"]
        )

        signal = self.signal_manager.generate_signal(
            decision,
            brain,
            {
                "risk_level": "MEDIO",
                "risk_score": 50,
                "allow_trade": True
            }
        )

        trade = self.trade_manager.generate_trade(
            price,
            signal,
            indicators["atr"]
        )

        return {

            "indicators": indicators,
            "analysis": analysis,
            "brain": brain,

            "risk": {
                "risk_level": "MEDIO",
                "risk_score": 50,
                "allow_trade": True
            },

            "decision": decision,
            "final_signal": signal,
            "signal": signal,
            "trade": trade
        }