"""
========================================
PROJECT PHOENIX AI
Trade Manager
Versione 1.1
========================================
"""

from Logs.logger import Logger

from Config.settings import (
    STOP_LOSS_ATR,
    TAKE_PROFIT_ATR
)


class TradeManager:

    def __init__(self):

        Logger.success("Trade Manager inizializzato.")

    def generate_trade(self, price, decision, atr):

        # ==========================
        # NESSUNA OPERAZIONE
        # ==========================

        if decision == "HOLD":

            return {

                "entry": round(price, 2),
                "stop_loss": None,
                "take_profit": None,
                "risk_reward": "N/D"

            }

        # ==========================
        # BUY
        # ==========================

        if decision == "BUY":

            stop_loss = price - (atr * STOP_LOSS_ATR)
            take_profit = price + (atr * TAKE_PROFIT_ATR)

        # ==========================
        # SELL
        # ==========================

        elif decision == "SELL":

            stop_loss = price + (atr * STOP_LOSS_ATR)
            take_profit = price - (atr * TAKE_PROFIT_ATR)

        # ==========================
        # RISULTATO
        # ==========================

        return {

            "entry": round(price, 2),
            "stop_loss": round(stop_loss, 2),
            "take_profit": round(take_profit, 2),
            "risk_reward": "1 : 2"

        }