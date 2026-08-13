"""
========================================
PROJECT PHOENIX AI
Risk Manager
Versione 11.0
========================================
"""

from Logs.logger import Logger

from Config.settings import MAX_RISK

from Core.risk_limits import RiskLimits
from Core.risk_position_size import RiskPositionSize
from Core.risk_drawdown import RiskDrawdown


class RiskManager:

    def __init__(self):

        Logger.success(
            "Risk Manager V11 inizializzato."
        )

        self.risk_reward_ratio = 2.0

        self.limits = RiskLimits()
        self.position_size = RiskPositionSize()
        self.drawdown = RiskDrawdown()

    # =====================================
    # RISK EVALUATION
    # =====================================

    def evaluate(
        self,
        analysis
    ):

        return self.limits.evaluate(
            analysis
        )

    # =====================================
    # POSITION SIZE
    # =====================================

    def calculate_position_size(
        self,
        account_balance,
        risk_percent,
        entry,
        stop_loss
    ):

        return self.position_size.calculate(
            account_balance,
            risk_percent,
            entry,
            stop_loss
        )

    # =====================================
    # DRAWDOWN
    # =====================================

    def calculate_drawdown(
        self,
        equity_curve
    ):

        return self.drawdown.calculate(
            equity_curve
        )

    # =====================================
    # BUILD TRADE
    # =====================================

    def build_trade(
        self,
        symbol,
        signal,
        current_price,
        atr,
        account_balance
    ):

        signal = str(
            signal
        ).upper().strip()

        # =================================
        # VALID SIGNAL
        # =================================

        if signal not in (
            "BUY",
            "SELL",
            "STRONG BUY",
            "STRONG SELL"
        ):

            return None

        atr = float(atr)
        entry = float(current_price)
        account_balance = float(account_balance)

        if atr <= 0:
            return None

        if entry <= 0:
            return None

        # =================================
        # RISK / REWARD
        # =================================

        rr = self.risk_reward_ratio

        # =================================
        # BUY
        # =================================

        if "BUY" in signal:

            stop_loss = entry - atr

            take_profit = (
                entry +
                (atr * rr)
            )

            side = "BUY"

        # =================================
        # SELL
        # =================================

        else:

            stop_loss = entry + atr

            take_profit = (
                entry -
                (atr * rr)
            )

            side = "SELL"

        # =================================
        # POSITION SIZE
        # =================================
        #
        # Il Core calcola la quantità
        # astratta in UNITA'.
        #
        # Il Core NON conosce:
        #
        # - contract size
        # - volume min
        # - volume max
        # - volume step
        # - caratteristiche broker
        #
        # La conversione in LOTTI MT5
        # viene effettuata dal MT5 Bridge.
        # =================================

        size = self.calculate_position_size(

            account_balance,

            MAX_RISK,

            entry,

            stop_loss

        )

        if size <= 0:
            return None

        # =================================
        # OUTPUT
        # =================================

        return {

            "symbol": symbol,

            "side": side,

            "entry": round(
                entry,
                6
            ),

            "stop_loss": round(
                stop_loss,
                6
            ),

            "take_profit": round(
                take_profit,
                6
            ),

            "atr": round(
                atr,
                6
            ),

            "risk_reward": rr,

            "risk_percent": MAX_RISK,

            "account_balance":
                account_balance,

            # =================================
            # CORE SIZE
            # =================================

            "size": size,

            "size_unit": "units"

        }