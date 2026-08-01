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
from Core.risk_manager import RiskManager
from Core.trade_manager import TradeManager


class AnalysisEngine:

    def __init__(self):

        Logger.success("Analysis Engine V7 inizializzato.")

        self.indicator_manager = IndicatorManager()

        self.market_analyzer = MarketAnalyzer()

        self.phoenix_brain = PhoenixBrain()

        self.decision_engine = DecisionEngine()

        self.signal_manager = SignalManager()

        self.risk_manager = RiskManager()

        self.trade_manager = TradeManager()

    # =====================================
    # ANALISI COMPLETA
    # =====================================

    def analyze(self, data):

        Logger.section("ANALYSIS ENGINE")

        indicators = self.indicator_manager.get_indicators(
            data
        )

        analysis = self.market_analyzer.analyze(
            indicators
        )

        risk = self.risk_manager.evaluate(
            analysis
        )

        brain = self.phoenix_brain.think(
            analysis,
            risk
        )

        decision = self.decision_engine.analyze(
            brain["action"]
        )

        signal = self.signal_manager.generate_signal(
            decision,
            brain,
            risk
        )

        trade = self.trade_manager.generate_trade(

            indicators["price"],

            signal,

            indicators["atr"]

        )

        return {

            "indicators": indicators,

            "analysis": analysis,

            "brain": brain,

            "risk": risk,

            "decision": decision,

            "signal": signal,

            "trade": trade

        }