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
from Core.market_regime_detector import MarketRegimeDetector
from Core.supervisor import Supervisor


class AnalysisEngine:

    def __init__(self):

        Logger.success(
            "Analysis Engine V9 inizializzato."
        )

        self.indicator_manager = IndicatorManager()

        self.market_analyzer = MarketAnalyzer()

        self.smart_money = SmartMoney()

        self.phoenix_brain = PhoenixBrain()

        self.signal_manager = SignalManager()

        self.risk_manager = RiskManager()

        self.trade_manager = TradeManager()
        self.regime_detector = MarketRegimeDetector()
        self.supervisor = Supervisor()

    # =====================================
    # ANALISI COMPLETA
    # =====================================

    def analyze(

        self,

        data,

        price,

        symbol="BTC-USD",

        account_balance=10000.0

    ):

        Logger.section("ANALYSIS ENGINE")

        indicators = self.indicator_manager.get_indicators(
            data
        )

        analysis = self.market_analyzer.analyze(
            indicators
        )

        # =====================================
        # SMART MONEY
        # =====================================

        analysis.update(
            self.smart_money.detect_bos(data)
        )

        choch = self.smart_money.detect_choch(data)

        analysis["choch_bullish"] = (
            choch["direction"] == "BULLISH"
        )

        analysis["choch_bearish"] = (
            choch["direction"] == "BEARISH"
        )

        fvg = self.smart_money.detect_fvg(data)

        analysis["fvg_bullish"] = (
            fvg["direction"] == "BULLISH"
        )

        analysis["fvg_bearish"] = (
            fvg["direction"] == "BEARISH"
        )

        order_block = (
            self.smart_money.detect_order_block(data)
        )

        analysis["order_block_bullish"] = (
            order_block["direction"] == "BULLISH"
        )

        analysis["order_block_bearish"] = (
            order_block["direction"] == "BEARISH"
        )

        liquidity = (
            self.smart_money.detect_liquidity(data)
        )

        analysis["liquidity_bullish"] = (
            liquidity["direction"] == "BULLISH"
        )

        analysis["liquidity_bearish"] = (
            liquidity["direction"] == "BEARISH"
        )

        # =====================================
        # MARKET REGIME
        # =====================================

        regime = self.regime_detector.detect(
            indicators,
            analysis
        )

        # =====================================
        # RISK
        # =====================================

        risk = self.risk_manager.evaluate(
            analysis,
            regime
        )

        # =====================================
        # AI BRAIN
        # =====================================

        brain = self.phoenix_brain.think(

            analysis,

            risk,

            regime

        )

        # =====================================
        # SUPERVISOR / DEVIL'S ADVOCATE
        # =====================================

        supervision = self.supervisor.evaluate(
            brain,
            risk,
            regime,
            analysis
        )

        # =====================================
        # SIGNAL
        # =====================================

        signal = self.signal_manager.validate(
            brain
        )

        # =====================================
        # SUPERVISOR VETO
        # =====================================

        if not supervision.get(
            "allowed",
            False
        ):
            signal["valid"] = False

        # =====================================
        # RISK GATE
        # =====================================
        #
        # Il Risk Manager ha la precedenza
        # sulla validazione del segnale.
        #
        # Anche STRONG BUY e STRONG SELL
        # NON possono aprire un trade quando
        # il rischio non consente di operare.

        if not risk.get(
            "allow_trade",
            False
        ):

            signal["valid"] = False

        # =====================================
        # TRADE
        # =====================================

        trade = None

        if signal["valid"]:

            trade = self.trade_manager.generate_trade(

                symbol=symbol,

                price=price,

                signal=signal["signal"],

                atr=indicators["atr"],

                account_balance=account_balance

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

            "trade": trade,
            "regime": regime,
            "supervision": supervision

        }