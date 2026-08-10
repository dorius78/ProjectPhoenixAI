"""
========================================
PROJECT PHOENIX AI
Live Trading Engine
Versione 4.0
========================================
"""

import time
from datetime import datetime

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

            "Live Trading Engine V4 inizializzato."

        )

        self.candles = candles

        self.analysis = analysis

        self.execution = execution

        self.position_controller = position_controller

        self.portfolio = portfolio

        self.backtest = backtest

        self.database = database

        self.guard = TradingGuard(self.portfolio.get_balance())

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

                        duration = (

                            report["close_time"]

                            -

                            closed["open_time"]

                        ).total_seconds()

                        result = (

                            "WIN"

                            if report["pnl"] > 0

                            else "LOSS"

                        )

                        risk = abs(

                            closed["entry"]

                            -

                            closed["initial_stop_loss"]

                        )

                        reward = abs(

                            report["exit"]

                            -

                            closed["entry"]

                        )

                        rr = 0

                        if risk > 0:

                            rr = round(

                                reward / risk,

                                2

                            )

                        trade = {

                            "symbol": report["symbol"],

                            "side": report["side"],

                            "entry": report["entry"],

                            "exit": report["exit"],

                            "stop_loss": closed["stop_loss"],

                            "take_profit": closed["take_profit"],

                            "pnl": report["pnl"],

                            "status": "CLOSED",

                            "reason": report["reason"],

                            "open_time": closed["open_time"],

                            "close_time": report["close_time"],

                            "duration": duration,

                            "result": result,

                            "risk_reward": rr

                        }

                        self.database.save_trade(

                            trade

                        )

                        self.backtest.add_trade(

                            trade

                        )

                        self.portfolio.update_balance(

                            report["pnl"]

                        )

                        self.guard.register_trade(

                            report["pnl"],

                            self.portfolio.get_balance()

                        )

                        self.portfolio.remove(

                            report["symbol"]

                        )

                        Logger.success(

                            "Trade registrato."

                        )

                # ==========================
                # NUOVO TRADE
                # ==========================

                if not self.position_controller.has_position():

                    can_trade, reason = self.guard.can_trade(

                        self.portfolio.get_balance()

                    )

                    if not can_trade:

                        Logger.warning(

                            f"Live Trading fermato dal Trading Guard: "

                            f"{reason}"

                        )

                        break

                    result = self.analysis.analyze(

                        data,

                        price,

                        symbol,

                        account_balance=self.portfolio.get_balance()

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

                                symbol=order["symbol"],

                                size=order["size"]

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