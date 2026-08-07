"""
========================================
PROJECT PHOENIX AI
Performance Analytics
Versione 16.0
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
from Core.performance_report import PerformanceReport

from Core.report_statistics import ReportStatistics
from Core.report_service import ReportService


class PerformanceAnalytics:

    INITIAL_CAPITAL = 10000.0

    def __init__(self, database):

        Logger.success(
            "Performance Analytics V16 inizializzato."
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
        self.report_builder = PerformanceReport()

        self.report_statistics = ReportStatistics()
        self.report_service = ReportService()

    def report(self):

        Logger.section("PERFORMANCE ANALYTICS")

        self.report_builder.clear()

        trades = self.database.load_trades()

        if len(trades) == 0:

            Logger.warning("Nessun trade presente.")

            return

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

        print()

        print("Trade Totali     :", risk["total"])
        print("Trade Win        :", risk["wins"])
        print("Trade Loss       :", risk["losses"])
        print("Break Even       :", risk["breakeven"])

        print()

        print("Win Rate         :", risk["win_rate"], "%")
        print("Win/Loss Ratio   :", winloss)
        print("Profit Factor    :", risk["profit_factor"])
        print("Sharpe Ratio     :", sharpe)
        print("Sortino Ratio    :", sortino)
        print("Calmar Ratio     :", calmar)
        print("Recovery Factor  :", recovery)
        print("Ulcer Index      :", ulcer)
        print("Omega Ratio      :", omega)
        print("Profit/Drawdown  :", profit_dd)
        print("Kelly Criterion  :", kelly, "%")
        print("Payoff Ratio     :", payoff)

        print()

        print("Gross Profit     :", risk["gross_profit"])
        print("Gross Loss       :", risk["gross_loss"])
        print("Profitto Netto   :", self.database.total_profit())
        print("Best Trade       :", self.database.best_trade())
        print("Worst Trade      :", self.database.worst_trade())
        print("Media Trade      :", self.database.average_profit())

        print()

        print("Average Win      :", trade["average_win"])
        print("Average Loss     :", trade["average_loss"])
        print("Expectancy       :", trade["expectancy"])

        print()

        print("ROI              :", roi, "%")
        print("Equity           :", round(equity, 2))
        print("Drawdown Max     :", round(max_drawdown, 2))

        print()

        print("Win Streak       :", longest_win)
        print("Loss Streak      :", longest_loss)

        print()

        print("Performance Mensile")
        print("--------------------------------")

        for mese, profitto in monthly.items():

            print(

                mese,

                ":",

                round(

                    profitto,

                    2

                )

            )

        print()

        print("Performance per Simbolo")
        print("--------------------------------")

        for symbol, info in symbols.items():

            print(

                f"{symbol:10}"

                f" Trades:{info['trades']:3}"

                f" Win:{info['wins']:3}"

                f" Loss:{info['losses']:3}"

                f" Profit:{round(info['profit'],2)}"

            )

        print()

        print("Performance per Timeframe")
        print("--------------------------------")

        for tf, info in timeframes.items():

            print(

                f"{tf:6}"

                f" Trades:{info['trades']:3}"

                f" Profit:{round(info['profit'],2)}"

            )

        print()

        print("Equity Curve")
        print("--------------------------------")

        for value in equity_curve:

            print(value)

        # =====================================
        # EXPORT
        # =====================================

        statistics = self.report_statistics.build(
            risk,
            trade,
            roi,
            equity,
            max_drawdown,
            sharpe,
            sortino,
            calmar,
            recovery,
            ulcer,
            omega,
            profit_dd,
            kelly,
            payoff,
            winloss
        )

        print()

        scelta = input(
            "Esportare questo report su file? (S/N): "
        ).strip().upper()

        if scelta == "S":

            self.report_service.export_all(statistics)

            Logger.success(
                "Report esportati: performance_report.txt/.csv/.json/.html/.pdf"
            )