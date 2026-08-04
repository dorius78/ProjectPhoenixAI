"""
========================================
PROJECT PHOENIX AI
Core System
Versione 16.0
========================================
"""

from Logs.logger import Logger

from Data.market_data import MarketData
from Data.candle_manager import CandleManager

from Core.analysis_engine import AnalysisEngine
from Core.backtest_engine import BacktestEngine
from Core.position_controller import PositionController
from Core.portfolio_manager import PortfolioManager
from Core.market_scanner import MarketScanner
from Core.live_trading_engine import LiveTradingEngine

from Execution.execution_engine import ExecutionEngine


class CoreSystem:

    def __init__(self):

        Logger.success("Core System V16 inizializzato.")

        self.market = MarketData()

        self.candles = CandleManager()

        self.analysis = AnalysisEngine()

        self.position_controller = PositionController()

        self.portfolio = PortfolioManager()

        self.execution = ExecutionEngine()

        self.backtest = BacktestEngine()

        self.scanner = MarketScanner()

        self.scanner.load_default()

        self.live_engine = LiveTradingEngine(

            self.candles,

            self.analysis,

            self.execution,

            self.position_controller,

            self.portfolio,

            self.backtest

        )

    # =====================================
    # AVVIO
    # =====================================

    def start(self):

        self.run_live()

    # =====================================
    # SCANNER MULTI MARKET
    # =====================================

    def run_live(self):

        Logger.section("PROJECT PHOENIX AI")

        Logger.info("Modalità LIVE SCANNER")

        self.market.load_markets()

        self.scanner.reset()

        symbols = self.scanner.get_symbols()

        Logger.info(

            f"Scanner: {len(symbols)} strumenti"

        )

        best_result = None

        for symbol in symbols:

            Logger.info(f"Analisi {symbol}")

            data = self.candles.get_candles(

                symbol,

                period="5d",

                interval="1h"

            )

            if data is None or len(data) == 0:

                continue

            current_price = float(

                data["Close"].iloc[-1]

            )

            result = self.analysis.analyze(

                data,

                current_price,

                symbol

            )

            decision = result["decision"]

            self.scanner.add_result(

                symbol,

                decision["action"],

                decision["score"],

                decision["confidence"]

            )

            if (

                best_result is None

                or decision["score"]

                > best_result["decision"]["score"]

            ):

                best_result = result

        self.scanner.report()

        if best_result is None:

            Logger.warning(

                "Nessun mercato disponibile."

            )

            return

        Logger.section(

            "MIGLIOR SEGNALE"

        )

        self.print_result(

            best_result

        )

        Logger.success(

            "Scanner completato."

        )

    # =====================================
    # LIVE CONTINUO
    # =====================================

    def run_live_trading(

        self,

        symbol="BTC-USD"

    ):

        Logger.section(

            "LIVE TRADING"

        )

        self.market.load_markets()

        self.live_engine.start(

            symbol=symbol,

            interval="1h",

            delay=30

        )

    # =====================================
    # BACKTEST
    # =====================================

    def run_backtest(self):

        Logger.info(

            "Backtest in sviluppo."

        )

    # =====================================
    # RISULTATI
    # =====================================

    def print_result(

        self,

        result

    ):

        Logger.section("RISULTATI")

        decision = result["decision"]

        signal = result["signal"]

        trade = result["trade"]

        print()

        print(

            "Decisione :",

            decision["action"]

        )

        print(

            "Segnale   :",

            signal["signal"]

        )

        print()

        print(

            "Score     :",

            decision["score"]

        )

        print(

            "Confidence:",

            decision["confidence"]

        )

        print()

        print(

            "Validazione:",

            "SI"

            if signal["valid"]

            else "NO"

        )

        print()

        if decision["reasons"]:

            print("Motivazioni:")

            for reason in decision["reasons"]:

                print(" -", reason)

            print()

        if trade:

            print("Symbol     :", trade["symbol"])

            print("Entry      :", trade["entry"])

            print("Stop Loss  :", trade["stop_loss"])

            print("Take Profit:", trade["take_profit"])

            print()

    # =====================================
    # BACKTEST REPORT
    # =====================================

    def print_backtest(self):

        Logger.section("BACKTEST")

        stats = self.backtest.run()

        print()

        for key, value in stats.items():

            print(f"{key:15}: {value}")