"""
========================================
PROJECT PHOENIX AI
Trade Report
Versione 1.0
========================================
"""

from Logs.logger import Logger


class TradeReport:

    def __init__(self):

        Logger.success(
            "Trade Report V1 inizializzato."
        )

    def print(self, trade):

        if trade is None:

            Logger.warning(
                "Nessun trade generato."
            )

            return

        Logger.section(
            "TRADE MANAGER"
        )

        Logger.info(
            f"Symbol       : {trade['symbol']}"
        )

        Logger.info(
            f"Signal       : {trade['signal']}"
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