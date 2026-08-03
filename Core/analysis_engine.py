"""
========================================
PROJECT PHOENIX AI
Analysis Engine
Versione 9.0
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

        Logger.success("Analysis Engine V9 inizializzato.")

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

    def analyze(

        self,

        data,

        price,

        symbol="BTC-USD"

    ):

        Logger.section("ANALYSIS ENGINE")

        indicators = self.indicator_manager.get_indicators(data)

        analysis = self.market_analyzer.analyze(indicators)

        # =====================================
        # SMART MONEY
        # =====================================

        analysis.update(

            self.smart_money.detect_bos(data)

        )

        analysis["choch"] = self.smart_money.detect_choch(data)

        analysis["fvg"] = self.smart_money.detect_fvg(data)

        analysis["order_block"] = self.smart_money.detect_order_block(data)

        analysis["liquidity"] = self.smart_money.detect_liquidity(data)

        # =====================================
        # RISK
        # =====================================

        risk = self.risk_manager.evaluate(analysis)

        # =====================================
        # AI BRAIN
        # =====================================

        brain = self.phoenix_brain.think(

            analysis,

            risk

        )

        # =====================================
        # SIGNAL
        # =====================================

        signal = self.signal_manager.validate(brain)

        # =====================================
        # TRADE
        # =====================================

        trade = None

        if signal["valid"]:

            trade = self.trade_manager.generate_trade(

                symbol=symbol,

                price=price,

                signal=signal["signal"],

                atr=indicators["atr"]

            )

        # =====================================
        # OUTPUT
        # =====================================

        return {

            "analysis": analysis,

            "indicators": indicators,

            "risk": risk,

            "decision": brain,

            "signal": signal,

            "trade": trade

        }