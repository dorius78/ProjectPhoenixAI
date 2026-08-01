"""
========================================
PROJECT PHOENIX AI
Risk Manager
Versione 7.0
========================================
"""

from Config.settings import RISK_REWARD_RATIO
from Logs.logger import Logger


class RiskManager:

    def __init__(self):

        Logger.success("Risk Manager V7 inizializzato.")

    # =====================================
    # COSTRUZIONE TRADE
    # =====================================

    def build_trade(

        self,

        symbol,

        signal,

        current_price,

        atr

    ):

        signal = signal.upper()

        if signal not in (

            "BUY",

            "SELL",

            "STRONG BUY",

            "STRONG SELL"

        ):

            Logger.info("Nessun trade generato.")

            return None

        atr = float(atr)

        if atr <= 0:

            Logger.warning("ATR non valido.")

            return None

        entry = float(current_price)

        rr = float(RISK_REWARD_RATIO)

        # ==========================
        # BUY
        # ==========================

        if "BUY" in signal:

            stop_loss = entry - atr

            take_profit = entry + (atr * rr)

            side = "BUY"

        # ==========================
        # SELL
        # ==========================

        else:

            stop_loss = entry + atr

            take_profit = entry - (atr * rr)

            side = "SELL"

        trade = {

            "symbol": symbol,

            "side": side,

            "entry": round(entry, 6),

            "stop_loss": round(stop_loss, 6),

            "take_profit": round(take_profit, 6),

            "atr": round(atr, 6),

            "risk_reward": rr

        }

        Logger.success(f"Trade costruito: {side}")

        return trade

    # =====================================
    # REPORT
    # =====================================

    def summary(self, trade):

        if trade is None:

            Logger.warning("Nessun trade.")

            return

        Logger.separator()

        Logger.title("RISK MANAGER")

        Logger.info(f"Symbol       : {trade['symbol']}")
        Logger.info(f"Side         : {trade['side']}")
        Logger.info(f"Entry        : {trade['entry']}")
        Logger.info(f"Stop Loss    : {trade['stop_loss']}")
        Logger.info(f"Take Profit  : {trade['take_profit']}")
        Logger.info(f"ATR          : {trade['atr']}")

        Logger.separator()

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        Logger.info("Risk Manager resettato.")