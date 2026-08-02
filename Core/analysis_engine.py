"""
========================================
PROJECT PHOENIX AI
Analysis Engine
Versione 8.1
========================================
"""

from Logs.logger import Logger

from Data.Indicators.indicator_manager import IndicatorManager

from Core.market_analyzer import MarketAnalyzer
from Core.smart_money import SmartMoney
from Core.phoenix_brain import PhoenixBrain
from Core.signal_manager import SignalManager
from Core.risk_manager import RiskManager
from Core.trade_manager import TradeManager


class AnalysisEngine:

    def __init__(self):

        Logger.success("Analysis Engine V8 inizializzato.")

        self.indicator_manager = IndicatorManager()

        self.market_analyzer = MarketAnalyzer()

        self.smart_money = SmartMoney()

        self.phoenix_brain = PhoenixBrain()

        self.signal_manager = SignalManager()

        self.risk_manager = RiskManager()

        self.trade_manager = TradeManager()

    # =====================================
    # ANALISI COMPLETA
    # =====================================

    def analyze(self, data, price):

        Logger.section("ANALYSIS ENGINE")

        # ==========================
        # INDICATORI
        # ==========================

        indicators = self.indicator_manager.get_indicators(data)

        # ==========================
        # ANALISI MERCATO
        # ==========================

        analysis = self.market_analyzer.analyze(indicators)

        # ==========================
        # SMART MONEY
        # ==========================

        analysis.update(

            self.smart_money.detect_bos(data)

        )

        analysis["choch"] = self.smart_money.detect_choch(data)

        analysis["fvg"] = self.smart_money.detect_fvg(data)

        analysis["order_block"] = self.smart_money.detect_order_block(data)

        analysis["liquidity"] = self.smart_money.detect_liquidity(data)

        # ==========================
        # RISK
        # ==========================

        risk = self.risk_manager.evaluate(analysis)

        # ==========================
        # PHOENIX BRAIN
        # ==========================

        brain = self.phoenix_brain.think(

            analysis,

            risk

        )

        # ==========================
        # DECISION
        # ==========================

        decision = {

            "signal": brain["action"],

            "score": brain["score"],

            "confidence": brain["confidence"],

            "reasons": brain["reasons"]

        }

        # ==========================
        # VALIDAZIONE
        # ==========================

        signal = self.signal_manager.validate(

            decision

        )

        # ==========================
        # TRADE
        # ==========================

        trade = self.trade_manager.generate_trade(

            symbol="BTC-USD",

            decision=signal,

            current_price=price,

            atr=indicators["atr"]

        )

        # ==========================
        # OUTPUT
        # ==========================

        return {

            "indicators": indicators,

            "analysis": analysis,

            "brain": brain,

            "risk": risk,

            "decision": decision,

            "signal": signal,

            "trade": trade

        }