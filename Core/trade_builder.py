"""
========================================
PROJECT PHOENIX AI
Trade Builder
Versione 2.0
========================================
"""

from Logs.logger import Logger


class TradeBuilder:

    def __init__(self):

        Logger.success(
            "Trade Builder V2 inizializzato."
        )

    # =====================================
    # COSTRUZIONE TRADE
    # =====================================

    def build(

        self,

        risk_manager,

        symbol,

        price,

        signal,

        atr,

        account_balance

    ):

        signal = str(
            signal
        ).upper().strip()

        # =================================
        # HOLD
        # =================================

        if signal == "HOLD":

            return None

        # =================================
        # NORMALIZZAZIONE DIREZIONE
        # =================================

        if signal == "STRONG BUY":

            side = "BUY"

        elif signal == "STRONG SELL":

            side = "SELL"

        elif signal == "BUY":

            side = "BUY"

        elif signal == "SELL":

            side = "SELL"

        else:

            Logger.info(
                f"Trade Builder: segnale non valido: {signal}"
            )

            return None

        # =================================
        # COSTRUZIONE TRADE
        # =================================

        trade = risk_manager.build_trade(

            symbol=symbol,

            signal=side,

            current_price=price,

            atr=atr,

            account_balance=account_balance

        )

        # =================================
        # FALLIMENTO RISK MANAGER
        # =================================

        if trade is None:

            Logger.info(
                "Trade Builder: Risk Manager "
                "ha rifiutato il trade."
            )

            return None

        # =================================
        # METADATI PHOENIX
        # =================================

        trade["symbol"] = symbol

        trade["signal"] = signal

        trade["side"] = side

        # =================================
        # LOG
        # =================================

        Logger.success(
            f"Trade costruito: "
            f"{side} {symbol} "
            f"size={trade['size']}"
        )

        return trade

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        Logger.info(
            "Trade Builder resettato."
        )