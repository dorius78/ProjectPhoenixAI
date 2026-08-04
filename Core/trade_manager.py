"""
========================================
PROJECT PHOENIX AI
Trade Manager
Versione 10.0
========================================
"""

from Logs.logger import Logger

from Core.risk_manager import RiskManager


class TradeManager:

    def __init__(self):

        self.risk = RiskManager()

        Logger.success("Trade Manager V10 inizializzato.")

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

        signal = str(signal).upper()

        if signal == "HOLD":

            return None

        side = signal

        if signal == "STRONG BUY":

            side = "BUY"

        elif signal == "STRONG SELL":

            side = "SELL"

        trade = self.risk.build_trade(

            symbol=symbol,

            signal=side,

            current_price=price,

            atr=atr

        )

        if trade is None:

            return None

        trade["symbol"] = symbol

        trade["signal"] = signal

        trade["side"] = side

        return trade

    # =====================================
    # REPORT
    # =====================================

    def summary(self, trade):

        if trade is None:

            Logger.warning("Nessun trade generato.")

            return

        Logger.section("TRADE MANAGER")

        Logger.info(f"Symbol       : {trade['symbol']}")

        Logger.info(f"Signal       : {trade['signal']}")

        Logger.info(f"Side         : {trade['side']}")

        Logger.info(f"Entry        : {trade['entry']}")

        Logger.info(f"Stop Loss    : {trade['stop_loss']}")

        Logger.info(f"Take Profit  : {trade['take_profit']}")

        Logger.info(f"Risk Reward  : {trade['risk_reward']}")

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        Logger.info("Trade Manager azzerato.")