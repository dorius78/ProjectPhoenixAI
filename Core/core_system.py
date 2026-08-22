"""
========================================
PROJECT PHOENIX AI
Core System
Versione 21.0
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
from Core.trading_guard import TradingGuard
from Core.market_scanner import MarketScanner
from Core.live_trading_engine import LiveTradingEngine
from Core.performance_analytics import PerformanceAnalytics

from Execution.execution_engine import ExecutionEngine
from Config.settings import MODE, MT5_SYMBOL


class CoreSystem:

    def __init__(self):

        Logger.success(
            "Core System V21 inizializzato."
        )

        self.market = MarketData()
        self.candles = CandleManager()
        self.analysis = AnalysisEngine()

        self.position_controller = PositionController()
        self.portfolio = PortfolioManager()

        self.execution = ExecutionEngine(symbol=MT5_SYMBOL, magic=260813, mt5_enabled=(MODE == "DEMO"), mt5_dry_run=False)

        self.backtest = BacktestEngine()

        # Guard dedicato al Backtest.
        # Il Live Trading mantiene il proprio Guard
        # all'interno di LiveTradingEngine.
        self.backtest_guard = None

        self.database = DatabaseManager()

        self.performance = PerformanceAnalytics(
            self.database
        )

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

        Logger.section(
            "PROJECT PHOENIX AI"
        )

        Logger.info(
            "Modalità LIVE SCANNER"
        )

        self.market.load_markets()

        self.scanner.reset()

        symbols = self.scanner.get_symbols()

        Logger.info(
            f"Scanner: {len(symbols)} strumenti"
        )

        best_result = None

        for symbol in symbols:

            Logger.info(
                f"Analisi {symbol}"
            )

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

        Logger.section(
            "DATABASE"
        )

        Logger.info(
            f"Trade salvati : {self.database.count()}"
        )

        Logger.success(
            "Core System completato."
        )

    # =====================================
    # LIVE TRADING
    # =====================================

    def run_live_trading(
        self,
        symbol="BTC-USD"
    ):

        Logger.section(
            "LIVE TRADING"
        )

        self.market.load_markets()

        if MODE == "LIVE":

            self._run_live_trading_broker(
                symbol
            )

        else:

            self.live_engine.start(
                symbol=symbol,
                interval="1h",
                delay=30
            )

    # =====================================
    # LIVE TRADING MT5
    # =====================================

    def _run_live_trading_broker(
        self,
        symbol
    ):

        Logger.warning(
            "MODE = LIVE: utilizzo del nuovo "
            "Execution Engine V9 + MT5 Bridge."
        )

        Logger.warning(
            "MT5 parte in DRY RUN: "
            "nessun ordine reale verrà inviato."
        )

        execution = ExecutionEngine(
            symbol=symbol,
            magic=260813,
            mt5_enabled=True,
            mt5_dry_run=True
        )

        if not execution.connect_mt5():

            Logger.warning(
                "Connessione MT5 fallita. "
                "Live Trading annullato."
            )

            return

        try:

            live_engine = LiveTradingEngine(
                self.candles,
                self.analysis,
                execution,
                self.position_controller,
                self.portfolio,
                self.backtest,
                self.database
            )

            live_engine.start(
                symbol=symbol,
                interval="1h",
                delay=30
            )

        finally:

            execution.disconnect_mt5()

    # =====================================
    # PERFORMANCE
    # =====================================

    def run_performance(self):

        self.performance.report()

    # =====================================
    # RESET BACKTEST
    # =====================================

    def _reset_backtest_state(self):

        self.position_controller = PositionController()

        self.portfolio.reset()

        self.backtest.reset()

        # Nuova sessione Guard per ogni Backtest.
        self.backtest_guard = TradingGuard(
            self.portfolio.get_balance()
        )

        # Ricostruzione del Live Engine con
        # i riferimenti aggiornati.
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
    # REGISTRA TRADE CHIUSO
    # =====================================

    def _register_closed_trade(
        self,
        closed,
        guard=None
    ):

        if closed is None:
            return None

        if closed.get("status") != "CLOSED":
            return None

        report = self.execution.close(
            closed
        )

        if not report:
            return None

        close_time = report.get(
            "close_time",
            closed.get("close_time")
        )

        open_time = closed.get(
            "open_time"
        )

        duration = 0.0

        if (
            open_time is not None
            and close_time is not None
        ):

            duration = (
                close_time - open_time
            ).total_seconds()

        pnl = float(
            report.get(
                "pnl",
                closed.get(
                    "current_profit",
                    0.0
                )
            )
        )

        result = (
            "WIN"
            if pnl > 0
            else
            "LOSS"
            if pnl < 0
            else
            "BREAKEVEN"
        )

        risk = abs(
            float(
                closed.get(
                    "entry",
                    0.0
                )
            )
            -
            float(
                closed.get(
                    "initial_stop_loss",
                    closed.get(
                        "stop_loss",
                        0.0
                    )
                )
            )
        )

        reward = abs(
            float(
                report.get(
                    "exit",
                    closed.get(
                        "current_price",
                        0.0
                    )
                )
            )
            -
            float(
                closed.get(
                    "entry",
                    0.0
                )
            )
        )

        risk_reward = (

            round(
                reward / risk,
                2
            )

            if risk > 0

            else 0.0
        )

        trade = {

            "symbol":
                report.get(
                    "symbol",
                    closed.get("symbol")
                ),

            "side":
                report.get(
                    "side",
                    closed.get("side")
                ),

            "entry":
                report.get(
                    "entry",
                    closed.get("entry")
                ),

            "exit":
                report.get(
                    "exit",
                    closed.get("current_price")
                ),

            "stop_loss":
                closed.get(
                    "stop_loss"
                ),

            "take_profit":
                closed.get(
                    "take_profit"
                ),

            "pnl":
                pnl,

            "status":
                "CLOSED",

            "reason":
                report.get(
                    "reason",
                    closed.get(
                        "close_reason"
                    )
                ),

            "open_time":
                open_time,

            "close_time":
                close_time,

            "duration":
                duration,

            "result":
                result,

            "risk_reward":
                risk_reward
        }

        self.database.save_trade(
            trade
        )

        self.backtest.add_trade(
            trade
        )

        self.portfolio.update_balance(
            pnl
        )

        # Trading Guard: nel Backtest utilizziamo
        # la data storica della chiusura.
        if guard is not None:

            guard.register_trade(
                pnl,
                self.portfolio.get_balance(),
                current_day=close_time
            )

        self.portfolio.remove(
            trade["symbol"]
        )

        return trade

    # =====================================
    # CHIUSURA FORZATA FINE BACKTEST
    # =====================================

    def _close_backtest_position(
        self,
        final_price,
        final_time
    ):

        if not self.position_controller.has_position():

            return None

        closed = self.position_controller.close_position(
            reason="BACKTEST END",
            timestamp=final_time,
            current_price=final_price
        )

        if closed is None:
            return None

        return self._register_closed_trade(
            closed,
            guard=self.backtest_guard
        )

    # =====================================
    # BACKTEST
    # =====================================

    def run_backtest(
        self,
        symbol="BTC-USD",
        period="3mo",
        interval="1h"
    ):

        Logger.section(
            "BACKTEST"
        )

        Logger.info(
            f"Backtest {symbol} "
            f"({period} - {interval})"
        )

        data = self.candles.get_backtest_data(
            symbol,
            period=period,
            interval=interval
        )

        if data is None or len(data) < 100:

            Logger.warning(
                "Dati insufficienti per il backtest "
                "(servono almeno 100 candele)."
            )

            return

        # =================================
        # RESET STATO
        # =================================

        self._reset_backtest_state()

        total_bars = len(data)

        start = 100

        analysed_bars = total_bars - start

        # =================================
        # CICLO STORICO
        # =================================

        for i in range(
            start,
            total_bars
        ):

            window = data.iloc[
                :i + 1
            ]

            current_price = float(
                window["Close"].iloc[-1]
            )

            candle_high = float(
                window["High"].iloc[-1]
            )

            candle_low = float(
                window["Low"].iloc[-1]
            )

            candle_time = (
                window.index[-1]
            )

            # =================================
            # GESTIONE POSIZIONE ESISTENTE
            # =================================

            if self.position_controller.has_position():

                closed = (
                    self.position_controller.update(
                        current_price,
                        candle_time,
                        high=candle_high,
                        low=candle_low
                    )
                )

                if (
                    closed is not None
                    and closed.get(
                        "status"
                    ) == "CLOSED"
                ):

                    self._register_closed_trade(
                        closed,
                        guard=self.backtest_guard
                    )

            # =================================
            # NUOVO TRADE
            # =================================

            if not self.position_controller.has_position():

                can_trade, guard_reason = (
                    self.backtest_guard.can_trade(
                        self.portfolio.get_balance(),
                        current_day=candle_time
                    )
                )

                if not can_trade:

                    Logger.warning(
                        "Backtest fermato dal Trading Guard: "
                        f"{guard_reason}"
                    )

                    break

                result_analysis = (
                    self.analysis.analyze(
                        window,
                        current_price,
                        symbol,
                        account_balance=(
                            self.portfolio.get_balance()
                        )
                    )
                )

                signal = result_analysis.get(
                    "signal"
                )

                trade = result_analysis.get(
                    "trade"
                )

                if (
                    trade is not None
                    and signal is not None
                    and signal.get(
                        "valid",
                        False
                    )
                ):

                    order = (
                        self.execution.execute(
                            trade
                        )
                    )

                    if order.get(
                        "success",
                        False
                    ):

                        opened = (
                            self.position_controller.open_position(
                                side=order["side"],
                                entry=order["entry"],
                                stop_loss=order["stop_loss"],
                                take_profit=order["take_profit"],
                                symbol=order["symbol"],
                                size=order["size"],
                                timestamp=candle_time
                            )
                        )

                        if opened:

                            self.portfolio.add(
                                order["symbol"],
                                self.position_controller.get_position()
                            )

        # =================================
        # CHIUSURA FINALE
        # =================================

        final_price = float(
            data["Close"].iloc[-1]
        )

        final_time = data.index[-1]

        self._close_backtest_position(
            final_price,
            final_time
        )

        # =================================
        # ATTIVITÀ
        # =================================

        self.backtest.set_total_bars(
            analysed_bars
        )

        # =================================
        # REPORT
        # =================================

        self.print_backtest()

        Logger.section(
            "DATABASE"
        )

        Logger.info(
            f"Trade salvati : "
            f"{self.database.count()}"
        )

        Logger.section(
            "PORTFOLIO"
        )

        self.portfolio.report()

        Logger.success(
            "Backtest completato."
        )

    # =====================================
    # RISULTATI
    # =====================================

    def print_result(
        self,
        result
    ):

        Logger.section(
            "RISULTATI"
        )

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

            print(
                "Motivazioni:"
            )

            for reason in decision["reasons"]:

                print(
                    " -",
                    reason
                )

            print()

        if trade:

            print(
                "Symbol     :",
                trade["symbol"]
            )

            print(
                "Entry      :",
                trade["entry"]
            )

            print(
                "Stop Loss  :",
                trade["stop_loss"]
            )

            print(
                "Take Profit:",
                trade["take_profit"]
            )

            print()

    # =====================================
    # BACKTEST REPORT
    # =====================================

    def print_backtest(self):

        Logger.section(
            "BACKTEST"
        )

        stats = self.backtest.run()

        print()

        for key, value in stats.items():

            print(
                f"{key:15}: {value}"
            )
