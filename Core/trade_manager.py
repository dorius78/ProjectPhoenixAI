"""
========================================
PROJECT PHOENIX AI
Trade Manager
Versione 9.0
========================================
"""

from Logs.logger import Logger

from Core.risk_manager import RiskManager


class TradeManager:

    def __init__(self):

        self.risk = RiskManager()

        Logger.success("Trade Manager V9 inizializzato.")

    # =====================================
    # GENERA TRADE
    # =====================================

    def generate_trade(

        self,

        symbol,

        price,

        signal,

        atr

    ):

        if signal in (

            "HOLD",

            None

        ):

            return None

        trade = self.risk.build_trade(

            symbol=symbol,

            signal=signal,

            current_price=price,

            atr=atr

        )

        if trade is None:

            return None

        trade["symbol"] = symbol

        return trade

    # =====================================
    # REPORT
    # =====================================

    def summary(self, trade):

        if trade is None:

            Logger.warning("Nessun trade generato.")

            return

        Logger.section("TRADE MANAGER")

        Logger.info(

            f"Symbol       : {trade['symbol']}"

        )

        Logger.info(

            f"Side         : {trade['side']}"

        )

        Logger.info(

            f"Entry        : {trade['entry']}"

        )

        Logger.info(

            f"Stop Loss    : {trade['stop_loss']}"

        )

        Logger.info(

            f"Take Profit  : {trade['take_profit']}"

        )

        Logger.info(

            f"Risk Reward  : {trade['risk_reward']}"

        )

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        Logger.info(

            "Trade Manager azzerato."

        )