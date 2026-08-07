"""
========================================
PROJECT PHOENIX AI
Trade Builder
Versione 1.0
========================================
"""

from Logs.logger import Logger


class TradeBuilder:

    def __init__(self):

        Logger.success(
            "Trade Builder V1 inizializzato."
        )

    def build(

        self,

        risk_manager,

        symbol,

        price,

        signal,

        atr,

        account_balance

    ):

        signal = str(signal).upper()

        if signal == "HOLD":

            return None

        side = signal

        if signal == "STRONG BUY":

            side = "BUY"

        elif signal == "STRONG SELL":

            side = "SELL"

        trade = risk_manager.build_trade(

            symbol=symbol,

            signal=side,

            current_price=price,

            atr=atr,

            account_balance=account_balance

        )

        if trade is None:

            return None

        trade["symbol"] = symbol
        trade["signal"] = signal
        trade["side"] = side

        return trade