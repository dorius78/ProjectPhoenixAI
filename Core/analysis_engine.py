"""
========================================
PROJECT PHOENIX AI
Analysis Engine
Versione 3.2
========================================
"""

from Logs.logger import Logger

from Data.Indicators.indicator_manager import IndicatorManager

from Core.market_analyzer import MarketAnalyzer
from Core.phoenix_brain import PhoenixBrain
from Core.decision_engine import DecisionEngine
from Core.risk_manager import RiskManager
from Core.phoenix_score import PhoenixScore
from Core.signal_manager import SignalManager
from Core.trade_manager import TradeManager


class AnalysisEngine:

    def __init__(self):

        Logger.success("Analysis Engine inizializzato.")

        self.indicator_manager = IndicatorManager()

        self.market_analyzer = MarketAnalyzer()
        self.phoenix_brain = PhoenixBrain()
        self.decision_engine = DecisionEngine()
        self.risk_manager = RiskManager()
        self.phoenix_score = PhoenixScore()
        self.signal_manager = SignalManager()
        self.trade_manager = TradeManager()

    def analyze(self, data, price):

        Logger.section("ANALYSIS ENGINE")

        # ==========================
        # INDICATORI
        # ==========================

        ema20 = self.indicator_manager.calculate_ema(data, 20)
        sma20 = self.indicator_manager.calculate_sma(data, 20)
        rsi14 = self.indicator_manager.calculate_rsi(data, 14)

        macd, signal, histogram = (
            self.indicator_manager.calculate_macd(data)
        )

        atr14 = self.indicator_manager.calculate_atr(data, 14)

        adx14 = self.indicator_manager.calculate_adx(data, 14)

        # ==========================
        # MARKET ANALYZER
        # ==========================

        analysis = self.market_analyzer.analyze(
            data,
            ema20,
            sma20,
            rsi14,
            macd,
            signal,
            adx14
        )

        # ==========================
        # RISK MANAGER
        # ==========================

        risk = self.risk_manager.evaluate(
            analysis
        )

        # ==========================
        # PHOENIX BRAIN
        # ==========================

        brain = self.phoenix_brain.think(
            analysis,
            risk
        )

        # ==========================
        # DECISION ENGINE
        # ==========================

        decision = self.decision_engine.analyze(
            brain["action"]
        )

        # ==========================
        # PHOENIX SCORE
        # ==========================

        phoenix_score = self.phoenix_score.calculate(
            analysis
        )

        # ==========================
        # SIGNAL MANAGER
        # ==========================

        final_signal = self.signal_manager.generate_signal(
            decision,
            brain,
            risk
        )

        # ==========================
        # TRADE MANAGER
        # ==========================

        trade = self.trade_manager.generate_trade(
            price,
            final_signal,
            atr14.iloc[-1]
        )

        # ==========================
        # RISULTATO
        # ==========================

        return {

            "ema20": ema20,
            "sma20": sma20,
            "rsi14": rsi14,

            "macd": macd,
            "signal": signal,
            "histogram": histogram,

            "atr14": atr14,
            "adx14": adx14,

            "analysis": analysis,

            "brain": brain,

            "decision": decision,

            "final_signal": final_signal,

            "risk": risk,

            "phoenix_score": phoenix_score,

            "trade": trade

        }