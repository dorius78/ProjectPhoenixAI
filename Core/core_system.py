"""
========================================
PROJECT PHOENIX AI
Core System
Versione 7.1
========================================
"""

from Logs.logger import Logger

from Data.market_data import MarketData
from Data.candle_manager import CandleManager

from Core.analysis_engine import AnalysisEngine
from Core.backtest_engine import BacktestEngine
from Core.position_controller import PositionController


class CoreSystem:

    def __init__(self):

        Logger.success("Core System V7 inizializzato.")

        self.market = MarketData()
        self.candles = CandleManager()

        self.analysis = AnalysisEngine()

        self.position_controller = PositionController()

        self.backtest = BacktestEngine()

    # =====================================
    # AVVIO SISTEMA
    # =====================================

    def start(self):

        Logger.section("PROJECT PHOENIX AI")

        Logger.info("Avvio Core System...")

        self.market.load_markets()

        data = self.candles.get_candles(

            "BTC-USD",

            period="5d",

            interval="1h"

        )

        if data is None or len(data) == 0:

            Logger.error("Nessun dato ricevuto.")

            return

        # ==========================
        # PREZZO ATTUALE
        # ==========================

        price = float(data["Close"].iloc[-1])

        # ==========================
        # ANALISI
        # ==========================

        result = self.analysis.analyze(
            data,
            price
        )

        Logger.section("RISULTATI")

        print()

        print("Decisione :", result["decision"])
        print("Segnale   :", result["signal"])

        print()

        print("Score     :", result["brain"]["score"])
        print("Confidence:", result["brain"]["confidence"])

        print()

        trade = result["trade"]

        if trade:

            print("Entry      :", trade["entry"])
            print("Stop Loss  :", trade["stop_loss"])
            print("Take Profit:", trade["take_profit"])

        # ==========================
        # REGISTRA TRADE
        # ==========================

        if trade and result["signal"] in ["BUY", "SELL"]:

            self.position_controller.open_position(

                result["signal"],

                trade["entry"],

                trade["stop_loss"],

                trade["take_profit"]

            )

            self.backtest.add_trade({

                "side": result["signal"],

                "entry": trade["entry"]

            })

        Logger.section("BACKTEST")

        stats = self.backtest.run()

        print()
        print(stats)

        Logger.success("Core System completato.")