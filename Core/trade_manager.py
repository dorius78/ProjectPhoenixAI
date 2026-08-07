"""
========================================
PROJECT PHOENIX AI
Trade Manager
Versione 12.0
========================================
"""

from Logs.logger import Logger

from Core.risk_manager import RiskManager

from Core.trade_builder import TradeBuilder
from Core.trade_report import TradeReport


class TradeManager:

    def __init__(self):

        self.risk = RiskManager()

        self.builder = TradeBuilder()
        self.report = TradeReport()

        Logger.success(
            "Trade Manager V12 inizializzato."
        )

    # =====================================
    # GENERA TRADE
    # =====================================

    def generate_trade(

        self,

        symbol,

        price,

        signal,

        atr,

        account_balance

    ):

        return self.builder.build(

            self.risk,

            symbol,

            price,

            signal,

            atr,

            account_balance

        )

    # =====================================
    # REPORT
    # =====================================

    def summary(

        self,

        trade

    ):

        self.report.print(

            trade

        )

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        Logger.info(

            "Trade Manager azzerato."

        )