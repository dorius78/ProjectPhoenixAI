"""
========================================
PROJECT PHOENIX AI
Live Trading Engine
Versione 5.3
========================================

Responsabilità:

- Ciclo continuo di Live Trading
- Analisi mercato
- Trading Guard
- Apertura posizione
- Gestione posizione
- Chiusura posizione
- Database
- Backtest
- Portfolio
- Paper Trading
- Compatibilità MT5
- Aggiornamento prezzo corrente
- Sincronizzazione posizione
- Protezione contro registrazioni
  di chiusure non eseguite
- Evita download storico durante
  la gestione di una posizione aperta

FASE 1
TRADE LIFECYCLE DEFINITIVO

Analysis
    ↓
Signal
    ↓
Risk
    ↓
Trade
    ↓
Execution
    ↓
Position
    ↓
Exit
    ↓
Execution Close
    ↓
Database
    ↓
Backtest
    ↓
Portfolio
    ↓
Trading Guard
"""

import time

from Logs.logger import Logger
from Core.trading_guard import TradingGuard


class LiveTradingEngine:

    def __init__(
        self,
        candles,
        analysis,
        execution,
        position_controller,
        portfolio,
        backtest,
        database
    ):

        Logger.success(
            "Live Trading Engine V5.3 inizializzato."
        )

        self.candles = candles
        self.analysis = analysis
        self.execution = execution
        self.position_controller = position_controller
        self.portfolio = portfolio
        self.backtest = backtest
        self.database = database

        self.guard = TradingGuard(
            self.portfolio.get_balance()
        )

    # =====================================
    # PREZZO CORRENTE
    # =====================================

    def _get_current_price(
        self,
        symbol,
        data=None
    ):

        # =================================
        # METODO 1
        # =================================

        try:

            method = getattr(
                self.candles,
                "get_current_price",
                None
            )

            if callable(method):

                value = method(symbol)

                if value is not None:

                    value = float(value)

                    if value > 0:

                        return value

        except Exception as error:

            Logger.warning(
                "get_current_price non disponibile: "
                f"{error}"
            )

        # =================================
        # METODO 2
        # =================================

        try:

            value = getattr(
                self.candles,
                "current_price",
                None
            )

            if callable(value):

                value = value(symbol)

            if value is not None:

                value = float(value)

                if value > 0:

                    return value

        except Exception:

            pass

        # =================================
        # FALLBACK CANDLE
        # =================================

        if data is not None:

            try:

                value = float(
                    data["Close"].iloc[-1]
                )

                if value > 0:

                    return value

            except Exception as error:

                Logger.error(
                    "Impossibile determinare "
                    f"il prezzo di {symbol}: {error}"
                )

        return None

    # =====================================
    # COSTRUZIONE TRADE DATABASE
    # =====================================

    def _build_closed_trade(
        self,
        closed,
        report
    ):

        if closed is None:

            return None

        # =================================
        # DATI BASE
        # =================================

        symbol = report.get(
            "symbol",
            closed.get("symbol")
        )

        side = report.get(
            "side",
            closed.get("side")
        )

        entry = float(
            report.get(
                "entry",
                closed.get("entry", 0.0)
            )
        )

        exit_price = float(
            report.get(
                "exit",
                closed.get(
                    "current_price",
                    entry
                )
            )
        )

        pnl = float(
            report.get(
                "pnl",
                closed.get(
                    "current_profit",
                    0.0
                )
            )
        )

        # =================================
        # TEMPI
        # =================================

        open_time = closed.get(
            "open_time"
        )

        close_time = report.get(
            "close_time",
            closed.get("close_time")
        )

        duration = 0.0

        if (
            open_time is not None
            and close_time is not None
        ):

            try:

                duration = (
                    close_time - open_time
                ).total_seconds()

            except Exception:

                duration = 0.0

        # =================================
        # RISULTATO
        # =================================

        if pnl > 0:

            result = "WIN"

        elif pnl < 0:

            result = "LOSS"

        else:

            result = "BREAKEVEN"

        # =================================
        # RISK
        # =================================

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
                    0.0
                )
            )

        )

        # =================================
        # REWARD
        # =================================

        reward = abs(

            exit_price
            -
            entry

        )

        # =================================
        # RISK / REWARD
        # =================================

        if risk > 0:

            risk_reward = round(
                reward / risk,
                2
            )

        else:

            risk_reward = 0.0

        # =================================
        # TRADE FINALE
        # =================================

        return {

            "symbol":
                symbol,

            "side":
                side,

            "entry":
                entry,

            "exit":
                exit_price,

            "stop_loss":
                float(
                    closed.get(
                        "stop_loss",
                        closed.get(
                            "initial_stop_loss",
                            0.0
                        )
                    )
                ),

            "take_profit":
                float(
                    closed.get(
                        "take_profit",
                        0.0
                    )
                ),

            "pnl":
                pnl,

            "status":
                "CLOSED",

            "reason":
                report.get(
                    "reason",
                    closed.get(
                        "close_reason",
                        "UNKNOWN"
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

    # =====================================
    # PROCESSAMENTO CHIUSURA
    # =====================================

    def _process_closed_position(
        self,
        closed
    ):

        if closed is None:

            return False

        if closed.get("status") != "CLOSED":

            return False

        # =================================
        # EXECUTION CLOSE
        # =================================

        report = self.execution.close(
            closed
        )

        # =================================
        # VERIFICA ESECUZIONE
        # =================================

        execution_success = report.get(
            "success",
            True
        )

        dry_run = report.get(
            "dry_run",
            False
        )

        # =================================
        # CHIUSURA NON CONFERMATA
        # =================================

        if not execution_success:

            # DRY RUN non è una chiusura reale.

            if dry_run:

                Logger.warning(
                    "Chiusura in MT5 DRY RUN: "
                    "trade NON registrato come "
                    "chiuso nel database."
                )

            else:

                Logger.error(
                    "CHIUSURA NON CONFERMATA: "
                    "trade NON registrato."
                )

            return False

        # =================================
        # TRADE DATABASE
        # =================================

        trade = self._build_closed_trade(
            closed,
            report
        )

        if trade is None:

            Logger.error(
                "Impossibile costruire "
                "il trade chiuso."
            )

            return False

        # =================================
        # DATABASE
        # =================================

        self.database.save_trade(
            trade
        )

        # =================================
        # BACKTEST
        # =================================

        self.backtest.add_trade(
            trade
        )

        # =================================
        # PORTFOLIO
        # =================================

        self.portfolio.update_balance(
            trade["pnl"]
        )

        # =================================
        # TRADING GUARD
        # =================================

        self.guard.register_trade(
            trade["pnl"],
            self.portfolio.get_balance()
        )

        # =================================
        # RIMOZIONE PORTFOLIO
        # =================================

        self.portfolio.remove(
            trade["symbol"]
        )

        # =================================
        # REPORT
        # =================================

        Logger.success(

            f"Trade chiuso #{trade['symbol']} "
            f"| {trade['reason']} "
            f"| {trade['result']} "
            f"| PnL {trade['pnl']:.2f}"

        )

        Logger.success(
            "Trade registrato in Database."
        )

        return True

    # =====================================
    # APERTURA POSIZIONE
    # =====================================

    def _open_position_from_order(
        self,
        order
    ):

        if order is None:

            return False

        if not order.get(
            "success",
            False
        ):

            return False

        # =================================
        # POSITION CONTROLLER
        # =================================

        opened = (
            self.position_controller.open_position(

                side=order["side"],

                entry=order["entry"],

                stop_loss=order["stop_loss"],

                take_profit=order["take_profit"],

                symbol=order["symbol"],

                size=order["size"]

            )
        )

        if not opened:

            Logger.warning(
                "Execution riuscita ma "
                "Position Controller non "
                "ha aperto la posizione."
            )

            return False

        # =================================
        # PORTFOLIO
        # =================================

        position = (
            self.position_controller.get_position()
        )

        self.portfolio.add(
            order["symbol"],
            position
        )

        Logger.success(
            "Posizione registrata "
            "nel Portfolio."
        )

        return True

    # =====================================
    # AVVIO
    # =====================================

    def start(
        self,
        symbol,
        interval="1h",
        delay=30
    ):

        Logger.section(
            "LIVE TRADING ENGINE"
        )

        Logger.info(
            f"Monitoraggio {symbol}"
        )

        while True:

            try:

                # =================================
                # POSIZIONE APERTA
                # =================================

                if self.position_controller.has_position():

                    price = self._get_current_price(
                        symbol
                    )

                    if price is None:

                        Logger.warning(
                            f"Prezzo {symbol} "
                            "non disponibile."
                        )

                        time.sleep(delay)

                        continue

                    position_before = (
                        self.position_controller.get_position()
                    )

                    if position_before is not None:

                        Logger.info(
                            f"Gestione posizione "
                            f"{symbol} @ {price:.6f}"
                        )

                    # =================================
                    # UPDATE POSITION
                    # =================================

                    closed = (
                        self.position_controller.update(
                            price
                        )
                    )

                    # =================================
                    # POSIZIONE ANCORA APERTA
                    # =================================

                    if (
                        closed is None
                        and
                        self.position_controller.has_position()
                    ):

                        current_position = (
                            self.position_controller.get_position()
                        )

                        self.portfolio.update(
                            symbol,
                            current_position
                        )

                    # =================================
                    # POSIZIONE CHIUSA
                    # =================================

                    if (
                        closed is not None
                        and
                        closed.get("status") == "CLOSED"
                    ):

                        self._process_closed_position(
                            closed
                        )

                    time.sleep(
                        delay
                    )

                    continue

                # =================================
                # NESSUNA POSIZIONE
                # =================================

                data = self.candles.get_candles(

                    symbol,

                    period="5d",

                    interval=interval

                )

                if (
                    data is None
                    or len(data) == 0
                ):

                    Logger.warning(
                        "Nessun dato mercato disponibile."
                    )

                    time.sleep(
                        delay
                    )

                    continue

                # =================================
                # PREZZO
                # =================================

                price = self._get_current_price(
                    symbol,
                    data
                )

                if price is None:

                    Logger.warning(
                        f"Prezzo {symbol} "
                        "non disponibile."
                    )

                    time.sleep(
                        delay
                    )

                    continue

                # =================================
                # TRADING GUARD
                # =================================

                can_trade, reason = (
                    self.guard.can_trade(
                        self.portfolio.get_balance()
                    )
                )

                if not can_trade:

                    Logger.warning(
                        "Live Trading fermato "
                        "dal Trading Guard: "
                        f"{reason}"
                    )

                    break

                # =================================
                # ANALISI
                # =================================

                result = self.analysis.analyze(

                    data,

                    price,

                    symbol,

                    account_balance=(

                        self.portfolio.get_balance()

                    )

                )

                signal = result["signal"]

                trade = result["trade"]

                # =================================
                # TRADE VALIDO
                # =================================

                if (
                    trade is not None
                    and
                    signal["valid"]
                ):

                    order = (
                        self.execution.execute(
                            trade
                        )
                    )

                    # =================================
                    # ORDINE NON ESEGUITO
                    # =================================

                    if not order.get(
                        "success",
                        False
                    ):

                        if order.get(
                            "dry_run",
                            False
                        ):

                            Logger.info(
                                "MT5 DRY RUN: "
                                "nessuna posizione "
                                "aperta nel Core."
                            )

                        else:

                            Logger.warning(
                                "Ordine non eseguito: "
                                f"{order.get('message', '')}"
                            )

                    # =================================
                    # ORDINE ESEGUITO
                    # =================================

                    else:

                        self._open_position_from_order(
                            order
                        )

                # =================================
                # ATTESA
                # =================================

                time.sleep(
                    delay
                )

            # =================================
            # INTERRUZIONE MANUALE
            # =================================

            except KeyboardInterrupt:

                Logger.warning(
                    "Live Trading interrotto manualmente."
                )

                break

            # =================================
            # ERRORE
            # =================================

            except Exception as error:

                Logger.error(
                    f"Live Trading Error: {error}"
                )

                time.sleep(
                    delay
                )