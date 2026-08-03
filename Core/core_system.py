"""
========================================
PROJECT PHOENIX AI
Core System
Versione 12.0
========================================
"""

from Logs.logger import Logger

from Data.market_data import MarketData
from Data.candle_manager import CandleManager

from Core.analysis_engine import AnalysisEngine
from Core.backtest_engine import BacktestEngine
from Core.position_controller import PositionController
from Core.portfolio_manager import PortfolioManager

from Execution.execution_engine import ExecutionEngine


class CoreSystem:

    def __init__(self):

        Logger.success("Core System V12 inizializzato.")

        self.market = MarketData()

        self.candles = CandleManager()

        self.analysis = AnalysisEngine()

        self.position_controller = PositionController()

        self.portfolio = PortfolioManager()

        self.execution = ExecutionEngine()

        self.backtest = BacktestEngine()

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

        symbol = "BTC-USD"

        data = self.candles.get_candles(

            symbol,

            period="5d",

            interval="1h"

        )

        if data is None or len(data) == 0:

            Logger.error("Nessun dato ricevuto.")

            return

        current_price = float(

            data["Close"].iloc[-1]

        )

        result = self.analysis.analyze(

            data,

            current_price,

            symbol

        )

        self.print_result(result)

        signal = result["signal"]

        trade = result["trade"]

        if trade is not None and signal["valid"]:

            order = self.execution.execute(trade)

            if order is not None and order["success"]:

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

                    self.backtest.add_trade({

                        "side": order["side"],

                        "entry": order["entry"],

                        "pnl": 0.0

                    })

        self.print_backtest()

        self.portfolio.report()

        Logger.success("Core System completato.")

    # =====================================
    # BACKTEST
    # =====================================

    def run_backtest(self):

        Logger.section("PROJECT PHOENIX AI")

        Logger.info("Modalità BACKTEST")

        self.market.load_markets()

        data = self.candles.get_backtest_data(

            "BTC-USD",

            period="1y",

            interval="1h"

        )

        stats = self.backtest.simulate(

            data,

            self.analysis,

            self.position_controller

        )

        print()

        for key, value in stats.items():

            print(f"{key:15}: {value}")

    # =====================================
    # RISULTATI
    # =====================================

    def print_result(self, result):

        Logger.section("RISULTATI")

        decision = result["decision"]

        signal = result["signal"]

        trade = result["trade"]

        print()

        print("Decisione :", decision["signal"])

        print("Segnale   :", signal["signal"])

        print()

        print("Score     :", decision["score"])

        print("Confidence:", decision["confidence"])

        print()

        print(

            "Validazione :",

            "SI" if signal["valid"] else "NO"

        )

        print()

        if decision["reasons"]:

            print("Motivazioni:")

            for reason in decision["reasons"]:

                print(" -", reason)

            print()

        if trade:

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