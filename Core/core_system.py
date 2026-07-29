"""
========================================
PROJECT PHOENIX AI
Core System
Versione 2.3
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

        Logger.success("Core System inizializzato.")

        self.market = MarketData()
        self.candles = CandleManager()

        self.analysis = AnalysisEngine()

        self.position_controller = PositionController()

        self.backtest = BacktestEngine()

    def start(self):

        Logger.section("PROJECT PHOENIX AI")

        Logger.info("Avvio del Core System...")

        # ==========================
        # MARKET
        # ==========================

        self.market.load_markets()

        price = self.market.get_price("BTC-USD")

        if price is None:

            Logger.error("Impossibile recuperare il prezzo.")
            return

        Logger.value("Prezzo BTC", round(price, 2))

        # ==========================
        # DOWNLOAD CANDELE
        # ==========================

        data = self.candles.get_candles(
            "BTC-USD",
            period="5d",
            interval="1h"
        )

        Logger.success(f"Candele scaricate: {len(data)}")

        # ==========================
        # ANALYSIS ENGINE
        # ==========================

        result = self.analysis.analyze(data, price)

        # ==========================
        # RISULTATI
        # ==========================

        Logger.section("RISULTATI")

        print()

        print("Trend            :", result["analysis"]["trend"])
        print("RSI              :", result["analysis"]["rsi"])
        print("Momentum         :", result["analysis"]["momentum"])

        print()

        print("Decision Engine  :", result["decision"])
        print("Segnale Finale   :", result["final_signal"])

        print()

        print("Rischio          :", result["risk"]["risk_level"])
        print("Score Rischio    :", result["risk"]["risk_score"])

        print(
            "Operazione       :",
            "CONSENTITA"
            if result["risk"]["allow_trade"]
            else "BLOCCATA"
        )

        # ==========================
        # ATR
        # ==========================

        Logger.section("ATR")

        print()

        print("ATR 14           :", round(result["atr14"].iloc[-1], 2))
        print("ADX 14           :", round(result["adx14"].iloc[-1], 2))

        # ==========================
        # PHOENIX BRAIN
        # ==========================

        Logger.section("PHOENIX BRAIN")

        print()

        print("Action           :", result["brain"]["action"])
        print("Score            :", result["brain"]["score"])
        print("Confidence       :", f'{result["brain"]["confidence"]}%')
        print("Strength         :", result["brain"]["strength"])
        print("Risk             :", result["brain"]["risk"])
        print("ADX              :", result["brain"]["adx"])

        print()

        print("Reasons")

        if result["brain"]["reasons"]:

            for reason in result["brain"]["reasons"]:

                print("  ✔", reason)

        else:

            print("  Nessuna")

        print()

        print("Warnings")

        if result["brain"]["warnings"]:

            for warning in result["brain"]["warnings"]:

                print("  ⚠", warning)

        else:

            print("  Nessuno")

        # ==========================
        # PHOENIX SCORE
        # ==========================

        Logger.section("PHOENIX SCORE")

        print()

        print("Score            :", result["phoenix_score"]["score"])

        print(
            "Affidabilità     :",
            f'{result["phoenix_score"]["confidence"]}%'
        )

        print(
            "Azione AI        :",
            result["phoenix_score"]["action"]
        )

        # ==========================
        # TRADE SETUP
        # ==========================

        Logger.section("TRADE SETUP")

        trade = result["trade"]

        print()

        print("Entrata          :", trade["entry"])
        print("Stop Loss        :", trade["stop_loss"])
        print("Take Profit      :", trade["take_profit"])
        print("Risk / Reward    :", trade["risk_reward"])

        print()

        # ==========================
        # BACKTEST
        # ==========================

        Logger.section("BACKTEST ENGINE")

        signals = [

            result["final_signal"],
            "BUY",
            "SELL",
            "BUY",
            "HOLD",
            "BUY"

        ]

        backtest = self.backtest.run(signals)

        print()

        print("Trade Totali     :", backtest["total_trades"])
        print("BUY              :", backtest["buy"])
        print("SELL             :", backtest["sell"])
        print("HOLD             :", backtest["hold"])

        print()

        # ==========================
        # FINE
        # ==========================

        Logger.section("FINE")

        Logger.success("Sistema pronto.")