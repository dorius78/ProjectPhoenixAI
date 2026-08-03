"""
========================================
PROJECT PHOENIX AI
Core System
Versione 14.1
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

from Execution.execution_engine import ExecutionEngine


class CoreSystem:

    def __init__(self):

        Logger.success("Core System V14.1 inizializzato.")

        self.market = MarketData()

        self.candles = CandleManager()

        self.analysis = AnalysisEngine()

        self.position_controller = PositionController()

        self.portfolio = PortfolioManager()

        self.execution = ExecutionEngine()

        self.backtest = BacktestEngine()

        self.scanner = MarketScanner()

        self.scanner.load_default()

    # =====================================
    # AVVIO
    # =====================================

    def start(self):

        self.run_live()

    # =====================================
    # LIVE
    # =====================================

    def run_live(self):

        Logger.section("PROJECT PHOENIX AI")

        Logger.info("Modalità LIVE")

        self.market.load_markets()

        self.scanner.reset()

        symbols = self.scanner.get_symbols()

        Logger.info(f"Scanner: {len(symbols)} strumenti")

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

            signal = result["signal"]

            trade = result["trade"]

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

                "Nessun mercato analizzato."

            )

            return

        Logger.section(

            "MIGLIOR SEGNALE"

        )

        self.print_result(best_result)

        signal = best_result["signal"]

        trade = best_result["trade"]

        if (

            trade is not None

            and signal["valid"]

        ):

            order = self.execution.execute(trade)

            if order["success"]:

                opened = self.position_controller.open_position(

                    side=order["side"],

                    entry=order["entry"],

                    stop_loss=order["stop_loss"],

                    take_profit=order["take_profit"],

                    symbol=order["symbol"]

                )

                if opened:

                    self.portfolio.add(

                        order["symbol"],

                        self.position_controller.get_position()

                    )

        self.print_backtest()

        self.portfolio.report()

        Logger.success("Core System completato.")

    # =====================================
    # BACKTEST
    # =====================================

    def run_backtest(self):

        Logger.info("Backtest in sviluppo.")

    # =====================================
    # RISULTATI
    # =====================================

    def print_result(self, result):

        Logger.section("RISULTATI")

        decision = result["decision"]

        signal = result["signal"]

        trade = result["trade"]

        print()

        print("Decisione :", decision["action"])

        print("Segnale   :", signal["signal"])

        print()

        print("Score     :", decision["score"])

        print("Confidence:", decision["confidence"])

        print()

        print(

            "Validazione:",

            "SI" if signal["valid"] else "NO"

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