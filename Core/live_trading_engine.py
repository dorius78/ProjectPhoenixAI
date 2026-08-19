"""
========================================
PROJECT PHOENIX AI
Live Trading Engine
Versione 5.2
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
- Compatibilità Paper Trading / MT5
- Aggiornamento prezzo corrente
- Evita download storico durante
  la gestione di una posizione aperta
========================================
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
            "Live Trading Engine V5.2 inizializzato."
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
        """
        Recupera il prezzo piu' aggiornato disponibile.

        Priorita':

        1. CandleManager.get_current_price()
        2. CandleManager.current_price()
        3. Ultimo Close delle candele

        Il fallback sulle candele mantiene
        la compatibilita' con l'architettura
        esistente.
        """

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
        # FALLBACK
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
    # CHIUSURA TRADE
    # =====================================

    def _process_closed_position(
        self,
        closed
    ):

        if closed is None:

            return

        if closed.get("status") != "CLOSED":

            return

        # =================================
        # EXECUTION CLOSE
        # =================================

        report = self.execution.close(
            closed
        )

        if not report.get(
            "success",
            True
        ):

            Logger.warning(
                "Execution close non confermato: "
                f"{report.get('message', '')}"
            )

        # =================================
        # DATI CHIUSURA
        # =================================

        close_time = report.get(
            "close_time",
            closed.get("close_time")
        )

        if close_time is None:

            close_time = closed.get(
                "close_time"
            )

        # =================================
        # DURATA
        # =================================

        duration = 0.0

        open_time = closed.get(
            "open_time"
        )

        if (
            close_time is not None
            and open_time is not None
        ):

            try:

                duration = (
                    close_time - open_time
                ).total_seconds()

            except Exception:

                duration = 0.0

        # =================================
        # PNL
        # =================================

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
        # RISULTATO
        # =================================

        result = (
            "WIN"
            if pnl > 0
            else "LOSS"
        )

        # =================================
        # RISK
        # =================================

        risk = abs(
            float(
                closed["entry"]
            )
            -
            float(
                closed["initial_stop_loss"]
            )
        )

        # =================================
        # REWARD
        # =================================

        exit_price = float(
            report.get(
                "exit",
                closed.get(
                    "current_price",
                    closed["entry"]
                )
            )
        )

        reward = abs(
            exit_price
            -
            float(
                closed["entry"]
            )
        )

        # =================================
        # RISK / REWARD
        # =================================

        rr = 0.0

        if risk > 0:

            rr = round(
                reward / risk,
                2
            )

        # =================================
        # TRADE DATABASE
        # =================================

        trade = {

            "symbol":
                report.get(
                    "symbol",
                    closed["symbol"]
                ),

            "side":
                report.get(
                    "side",
                    closed["side"]
                ),

            "entry":
                report.get(
                    "entry",
                    closed["entry"]
                ),

            "exit":
                exit_price,

            "stop_loss":
                closed["stop_loss"],

            "take_profit":
                closed["take_profit"],

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
                closed["open_time"],

            "close_time":
                close_time,

            "duration":
                duration,

            "result":
                result,

            "risk_reward":
                rr

        }

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
            pnl
        )

        # =================================
        # TRADING GUARD
        # =================================

        self.guard.register_trade(
            pnl,
            self.portfolio.get_balance()
        )

        # =================================
        # RIMUOVI PORTFOLIO
        # =================================

        self.portfolio.remove(
            trade["symbol"]
        )

        Logger.success(
            f"Trade chiuso #{trade['symbol']} "
            f"| {trade['reason']} "
            f"| PnL {pnl:.2f}"
        )

        Logger.success(
            "Trade registrato."
        )

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
                #
                # Se esiste gia' una posizione,
                # NON scarichiamo nuovamente
                # tutte le candele.
                #
                # Recuperiamo direttamente
                # il prezzo corrente.
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
                    # AGGIORNAMENTO POSIZIONE
                    # =================================

                    closed = (
                        self.position_controller.update(
                            price
                        )
                    )

                    # =================================
                    # SINCRONIZZAZIONE PORTFOLIO
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

                    # =================================
                    # ATTESA
                    # =================================

                    time.sleep(delay)

                    continue

                # =================================
                # NESSUNA POSIZIONE
                # =================================
                #
                # Solo qui scarichiamo le candele
                # necessarie per una nuova analisi.
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

                    time.sleep(delay)

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

                    time.sleep(delay)

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

                        if opened:

                            self.portfolio.add(

                                order["symbol"],

                                self.position_controller.get_position()

                            )

                            Logger.success(
                                "Posizione registrata "
                                "nel Portfolio."
                            )

                # =================================
                # ATTESA
                # =================================

                time.sleep(delay)

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
                    str(error)
                )

                time.sleep(delay)