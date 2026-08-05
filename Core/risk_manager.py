"""
========================================
PROJECT PHOENIX AI
Risk Manager
Versione 10.0
========================================
"""

from Logs.logger import Logger

from Core.risk_limits import RiskLimits
from Core.risk_position_size import RiskPositionSize
from Core.risk_drawdown import RiskDrawdown


class RiskManager:

    def __init__(self):

        Logger.success(
            "Risk Manager V10 inizializzato."
        )

        self.risk_reward_ratio = 2.0

        self.limits = RiskLimits()
        self.position_size = RiskPositionSize()
        self.drawdown = RiskDrawdown()

    def evaluate(
        self,
        analysis
    ):

        return self.limits.evaluate(
            analysis
        )

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

    def calculate_drawdown(
        self,
        equity_curve
    ):

        return self.drawdown.calculate(
            equity_curve
        )

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

            return None

        atr = float(atr)
        entry = float(current_price)

        rr = self.risk_reward_ratio

        if "BUY" in signal:

            stop_loss = entry - atr
            take_profit = entry + (atr * rr)
            side = "BUY"

        else:

            stop_loss = entry + atr
            take_profit = entry - (atr * rr)
            side = "SELL"

        return {

            "symbol": symbol,
            "side": side,
            "entry": round(entry, 6),
            "stop_loss": round(stop_loss, 6),
            "take_profit": round(take_profit, 6),
            "atr": round(atr, 6),
            "risk_reward": rr

        }