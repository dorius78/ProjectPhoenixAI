"""
========================================
PROJECT PHOENIX AI
Core System
Versione 8.0
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

        Logger.success("Core System V8 inizializzato.")

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

        price = float(data["Close"].iloc[-1])

        result = self.analysis.analyze(

            data,

            price

        )

        Logger.section("RISULTATI")

        print()

        decision = result["decision"]

        signal = result["signal"]

        print("Decisione :", decision["signal"])

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

        trade = result["trade"]

        if trade:

            print("Entry      :", trade["entry"])

            print("Stop Loss  :", trade["stop_loss"])

            print("Take Profit:", trade["take_profit"])

            print()

        # =====================================
        # APERTURA POSIZIONE
        # =====================================

        if (

            trade is not None

            and signal["valid"]

            and signal["signal"] in (

                "BUY",

                "SELL",

                "STRONG BUY",

                "STRONG SELL"

            )

        ):

            self.position_controller.open_position(

                signal["signal"],

                trade["entry"],

                trade["stop_loss"],

                trade["take_profit"]

            )

            self.backtest.add_trade({

                "side": signal["signal"],

                "entry": trade["entry"],

                "pnl": 0

            })

        Logger.section("BACKTEST")

        stats = self.backtest.run()

        print()

        for key, value in stats.items():

            print(f"{key:15}: {value}")

        Logger.success("Core System completato.")