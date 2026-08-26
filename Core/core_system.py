"""
========================================
PROJECT PHOENIX AI
Core System
Versione 19.0
========================================
"""

from Logs.logger import Logger

from Data.market_data import MarketData
from Data.candle_manager import CandleManager

from Database.database_manager import DatabaseManager

from Core.analysis_engine import AnalysisEngine
from Core.backtest_engine import BacktestEngine
from Core.position_controller import PositionController
from Core.portfolio_manager import PortfolioManager
from Core.market_scanner import MarketScanner
from Core.live_trading_engine import LiveTradingEngine
from Core.performance_analytics import PerformanceAnalytics

from Execution.execution_engine import ExecutionEngine
from Config.settings import (
    MODE,
    LIVE_DATABASE,
    BACKTEST_DATABASE
)


class CoreSystem:

    def __init__(self):

        Logger.success("Core System V19 inizializzato.")

        self.market = MarketData()

        self.candles = CandleManager()

        self.analysis = AnalysisEngine()

        self.position_controller = PositionController()

        self.portfolio = PortfolioManager()

        # =================================================
        # EXECUTION ROUTING
        # =================================================
        # Paper Trading rimane il default.
        # Il broker MT5 viene attivato esclusivamente
        # dal percorso Live Trading.
        self.execution = ExecutionEngine()

        self.backtest = BacktestEngine()

        self.live_database = DatabaseManager(
            LIVE_DATABASE
        )

        self.backtest_database = DatabaseManager(
            BACKTEST_DATABASE
        )

        # =====================================
        # DATABASE SEPARATI
        # =====================================

        # Database storico phoenix_ai.db:
        # NON viene utilizzato dal sistema operativo.
        #
        # LIVE:
        # utilizzato esclusivamente dal Live Trading.
        #
        # BACKTEST:
        # utilizzato esclusivamente dal Backtest.

        self.database = self.live_database

        self.live_performance = PerformanceAnalytics(
            self.live_database
        )

        self.backtest_performance = PerformanceAnalytics(
            self.backtest_database
        )

        # Compatibilita' con il codice esistente:
        # Performance Analytics predefinito = LIVE.
        self.performance = self.live_performance

        self.scanner = MarketScanner()

        self.scanner.load_default()

        self.live_engine = LiveTradingEngine(

            self.candles,

            self.analysis,

            self.execution,

            self.position_controller,

            self.portfolio,

            self.backtest,

            self.database

        )

    # =====================================
    # AVVIO
    # =====================================

    def start(self):

        self.run_live()

    # =====================================
    # SCANNER
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

                symbol,

                account_balance=self.portfolio.get_balance()

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

        # Lo Scanner Multi Market e' pensato per segnalare, non per
        # operare: mostra solo la classifica e il miglior segnale.
        # Prima apriva davvero una posizione (paper trading) che pero'
        # non veniva mai monitorata ne' chiusa (lo scanner e' un
        # comando "one-shot", non un ciclo continuo come il Live
        # Trading), restando orfana in memoria fino alla chiusura del
        # programma. Se vuoi operare su un segnale trovato qui, usa
        # il Live Trading (opzione 2) sul simbolo scelto.

        Logger.section("DATABASE")

        Logger.info(
            f"Trade salvati : {self.database.count()}"
        )

        Logger.success(
            "Core System completato."
        )

    # =====================================
    # LIVE TRADING
    # =====================================

    def run_live_trading(self, symbol="BTC-USD"):

        Logger.section("LIVE TRADING")

        self.market.load_markets()

        if MODE == "LIVE":

            self._run_live_trading_broker(symbol)

        else:

            self.live_engine.start(
                symbol=symbol,
                interval="1h",
                delay=30
            )

    def _run_live_trading_broker(self, symbol):

        # MODE == "LIVE" in Config/settings.py: usa un broker vero
        # (MT5) invece della simulazione. Import qui, non in cima al
        # file, cosi' chi usa solo la simulazione non ha bisogno del
        # pacchetto MetaTrader5 installato (funziona solo su Windows).
        from Execution.mt5_broker import MT5Broker

        Logger.warning(
            "MODE = LIVE: questo ciclo apre e chiude posizioni REALI "
            "tramite MT5 (conto demo o reale a seconda delle "
            "credenziali in Config/mt5_credentials.py)."
        )

        conferma = input(
            "Digita CONFERMO per avviare il trading automatico "
            "tramite broker reale: "
        ).strip()

        if conferma.upper() != "CONFERMO":

            Logger.info("Avvio annullato dall'utente.")

            return

        broker = MT5Broker()

        if not broker.connect():

            Logger.warning(
                "Connessione al broker fallita. Live Trading annullato."
            )

            return

        live_engine = LiveTradingEngine(
            self.candles,
            self.analysis,
            broker,
            self.position_controller,
            self.portfolio,
            self.backtest,
            self.database
        )

        try:

            live_engine.start(
                symbol=symbol,
                interval="1h",
                delay=30
            )

        finally:

            broker.disconnect()

    # =====================================
    # PERFORMANCE
    # =====================================

    def run_performance(self):

        self.performance.report()

    # =====================================
    # BACKTEST
    # =====================================

    def run_backtest(self, symbol="BTC-USD", period="3mo", interval="1h"):

        Logger.section("BACKTEST")

        Logger.info(f"Backtest {symbol} ({period} - {interval})")

        data = self.candles.get_backtest_data(symbol, period=period, interval=interval)

        if data is None or len(data) < 100:
            Logger.warning("Dati insufficienti per il backtest (servono almeno 100 candele).")
            return

        # Stato pulito ad ogni backtest: nessuna posizione residua
        # da una precedente esecuzione (Live Trading o backtest),
        # e saldo che riparte dal capitale iniziale di Config.
        self.position_controller = PositionController()
        self.portfolio.reset()
        self.backtest.reset()

        total_bars = len(data)

        # Le prime candele servono solo a "riscaldare" gli indicatori
        # (EMA/ADX/ecc. richiedono uno storico minimo per essere
        # affidabili): non generiamo trade prima di questo punto.
        start = 100

        for i in range(start, total_bars):

            window = data.iloc[:i + 1]
            current_candle = window.iloc[-1]

            current_price = float(current_candle["Close"])
            candle_high = float(current_candle["High"])
            candle_low = float(current_candle["Low"])
            candle_time = window.index[-1]

            if self.position_controller.has_position():

                closed = self.position_controller.update(
                    current_price,
                    candle_time,
                    high=candle_high,
                    low=candle_low
                )

                if closed is not None and closed["status"] == "CLOSED":

                    report = self.execution.close(closed)

                    duration = (report["close_time"] - closed["open_time"]).total_seconds()

                    # =====================================
                    # RISULTATO TRADE
                    # =====================================

                    if report["pnl"] > 0:
                        result = "WIN"
                    elif report["pnl"] < 0:
                        result = "LOSS"
                    else:
                        result = "BREAKEVEN"

                    # =====================================
                    # RISK / REWARD
                    # =====================================
                    # Il rischio deve essere quello iniziale
                    # del trade, non lo Stop Loss eventualmente
                    # modificato da Break Even / Trailing Stop.

                    initial_stop = closed.get(
                        "initial_stop_loss",
                        closed["stop_loss"]
                    )

                    risk = abs(
                        closed["entry"] - initial_stop
                    )

                    reward = abs(
                        report["exit"] - closed["entry"]
                    )

                    rr = round(
                        reward / risk,
                        2
                    ) if risk > 0 else 0

                    trade = {
                        "symbol": report["symbol"],
                        "side": report["side"],
                        "entry": report["entry"],
                        "exit": report["exit"],
                        "stop_loss": closed["stop_loss"],
                        "initial_stop_loss": closed["initial_stop_loss"],
                        "take_profit": closed["take_profit"],
                        "size": closed["size"],
                        "pnl": report["pnl"],
                        "status": "CLOSED",
                        "reason": report["reason"],
                        "open_time": closed["open_time"],
                        "close_time": report["close_time"],
                        "duration": duration,
                        "result": result,
                        "risk_reward": rr
                    }

                    self.backtest_database.save_trade(trade)
                    self.backtest.add_trade(trade)
                    self.portfolio.update_balance(report["pnl"])
                    self.portfolio.remove(report["symbol"])

            if not self.position_controller.has_position():

                result_analysis = self.analysis.analyze(
                    window,
                    current_price,
                    symbol,
                    account_balance=self.portfolio.get_balance()
                )
                signal = result_analysis["signal"]
                trade = result_analysis["trade"]

                if trade is not None and signal["valid"]:

                    order = self.execution.execute(trade)

                    if order["success"]:

                        opened = self.position_controller.open_position(
                            side=order["side"],
                            entry=order["entry"],
                            stop_loss=order["stop_loss"],
                            take_profit=order["take_profit"],
                            symbol=order["symbol"],
                            size=order["size"],
                            timestamp=candle_time
                        )

                        if opened:

                            self.portfolio.add(
                                order["symbol"],
                                self.position_controller.get_position()
                            )

        # =====================================
        # POSIZIONE APERTA ALLA FINE DEL DATASET
        # =====================================

        final_position = (
            self.position_controller.get_position()
        )

        self.backtest.set_open_trade(
            final_position
        )

        self.backtest.set_total_bars(
            total_bars - start
        )

        stats = self.print_backtest()

        Logger.section("DATABASE")

        Logger.info(
            f"Trade salvati nel Backtest DB : "
            f"{self.backtest_database.count()}"
        )
        return stats

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

        return stats