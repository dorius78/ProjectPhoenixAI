"""
========================================
PROJECT PHOENIX AI
Live Trading Engine
Versione 1.0
========================================
"""

import time

from Logs.logger import Logger


class LiveTradingEngine:

    def __init__(

        self,

        candles,

        analysis,

        execution,

        position_controller,

        portfolio,

        backtest

    ):

        Logger.success(

            "Live Trading Engine V1 inizializzato."

        )

        self.candles = candles

        self.analysis = analysis

        self.execution = execution

        self.position_controller = position_controller

        self.portfolio = portfolio

        self.backtest = backtest

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

                data = self.candles.get_candles(

                    symbol,

                    period="5d",

                    interval=interval

                )

                if data is None or len(data) == 0:

                    time.sleep(delay)

                    continue

                price = float(

                    data["Close"].iloc[-1]

                )

                # ==========================
                # POSIZIONE APERTA
                # ==========================

                if self.position_controller.has_position():

                    closed = self.position_controller.update(

                        price

                    )

                    if (

                        closed is not None

                        and closed["status"] == "CLOSED"

                    ):

                        report = self.execution.close(

                            closed

                        )

                        self.backtest.add_trade({

                            "side": report["side"],

                            "entry": report["entry"],

                            "exit": report["exit"],

                            "pnl": report["pnl"]

                        })

                        self.portfolio.remove(

                            report["symbol"]

                        )

                # ==========================
                # NUOVA ANALISI
                # ==========================

                if not self.position_controller.has_position():

                    result = self.analysis.analyze(

                        data,

                        price,

                        symbol

                    )

                    signal = result["signal"]

                    trade = result["trade"]

                    if (

                        trade is not None

                        and signal["valid"]

                    ):

                        order = self.execution.execute(

                            trade

                        )

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

                time.sleep(delay)

            except KeyboardInterrupt:

                Logger.warning(

                    "Live Trading interrotto."

                )

                break

            except Exception as error:

                Logger.error(

                    str(error)

                )

                time.sleep(delay)