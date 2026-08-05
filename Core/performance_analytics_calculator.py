"""
========================================
PROJECT PHOENIX AI
Performance Analytics Calculator
Versione 2.0
========================================
"""

from Logs.logger import Logger

from Core.equity_curve import EquityCurve
from Core.risk_statistics import RiskStatistics
from Core.trade_statistics import TradeStatistics
from Core.monthly_statistics import MonthlyStatistics
from Core.symbol_statistics import SymbolStatistics
from Core.timeframe_statistics import TimeframeStatistics

from Core.sharpe_ratio import SharpeRatio
from Core.sortino_ratio import SortinoRatio
from Core.calmar_ratio import CalmarRatio
from Core.recovery_factor import RecoveryFactor
from Core.ulcer_index import UlcerIndex
from Core.omega_ratio import OmegaRatio

from Core.profit_to_drawdown import ProfitToDrawdown
from Core.kelly_criterion import KellyCriterion
from Core.payoff_ratio import PayoffRatio
from Core.win_loss_ratio import WinLossRatio


class PerformanceAnalyticsCalculator:

    INITIAL_CAPITAL = 10000.0

    def __init__(self, database):

        Logger.success(
            "Performance Analytics Calculator V2 inizializzato."
        )

        self.database = database

        self.equity_curve = EquityCurve()

        self.risk = RiskStatistics()
        self.trade_stats = TradeStatistics()

        self.monthly = MonthlyStatistics()
        self.symbols = SymbolStatistics()
        self.timeframes = TimeframeStatistics()

        self.sharpe = SharpeRatio()
        self.sortino = SortinoRatio()
        self.calmar = CalmarRatio()
        self.recovery = RecoveryFactor()
        self.ulcer = UlcerIndex()

        self.omega = OmegaRatio()
        self.profit_dd = ProfitToDrawdown()
        self.kelly = KellyCriterion()
        self.payoff = PayoffRatio()
        self.winloss = WinLossRatio()

    def calculate(self):

        trades = self.database.load_trades()

        if len(trades) == 0:

            return None

        risk = self.risk.calculate(self.database)
        trade = self.trade_stats.calculate(self.database)

        monthly = self.monthly.calculate(self.database)
        symbols = self.symbols.calculate(self.database)
        timeframes = self.timeframes.calculate(self.database)

        sharpe = self.sharpe.calculate(self.database)
        sortino = self.sortino.calculate(self.database)
        calmar = self.calmar.calculate(self.database)
        recovery = self.recovery.calculate(self.database)
        ulcer = self.ulcer.calculate(self.database)

        omega = self.omega.calculate(self.database)
        profit_dd = self.profit_dd.calculate(self.database)
        kelly = self.kelly.calculate(self.database)
        payoff = self.payoff.calculate(self.database)
        winloss = self.winloss.calculate(self.database)

        equity = self.INITIAL_CAPITAL
        peak = equity
        max_drawdown = 0

        longest_win = 0
        longest_loss = 0

        current_win = 0
        current_loss = 0

        equity_curve = self.equity_curve.calculate(
            list(reversed(trades))
        )

        for row in reversed(trades):

            pnl = float(row[7])

            equity += pnl

            if pnl > 0:

                current_win += 1
                current_loss = 0

            elif pnl < 0:

                current_loss += 1
                current_win = 0

            longest_win = max(
                longest_win,
                current_win
            )

            longest_loss = max(
                longest_loss,
                current_loss
            )

            if equity > peak:

                peak = equity

            drawdown = peak - equity

            if drawdown > max_drawdown:

                max_drawdown = drawdown

        roi = round(

            (
                equity - self.INITIAL_CAPITAL
            )

            /

            self.INITIAL_CAPITAL

            * 100,

            2

        )

        return {

            "risk": risk,
            "trade": trade,

            "monthly": monthly,
            "symbols": symbols,
            "timeframes": timeframes,

            "sharpe": sharpe,
            "sortino": sortino,
            "calmar": calmar,
            "recovery": recovery,
            "ulcer": ulcer,

            "omega": omega,
            "profit_dd": profit_dd,
            "kelly": kelly,
            "payoff": payoff,
            "winloss": winloss,

            "roi": roi,
            "equity": equity,
            "drawdown": max_drawdown,

            "longest_win": longest_win,
            "longest_loss": longest_loss,

            "equity_curve": equity_curve,

            "gross_profit": risk["gross_profit"],
            "gross_loss": risk["gross_loss"],

            "net_profit": self.database.total_profit(),
            "best_trade": self.database.best_trade(),
            "worst_trade": self.database.worst_trade(),
            "average_trade": self.database.average_profit()

        }