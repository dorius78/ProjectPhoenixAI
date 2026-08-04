"""
========================================
PROJECT PHOENIX AI
Performance Analytics
Versione 10.0
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


class PerformanceAnalytics:

    INITIAL_CAPITAL = 10000.0

    def __init__(self, database):

        Logger.success(
            "Performance Analytics V10 inizializzato."
        )

        self.database = database

        self.equity_curve = EquityCurve()

        self.risk = RiskStatistics()

        self.trade_stats = TradeStatistics()

        self.monthly = MonthlyStatistics()

        self.symbols = SymbolStatistics()

        self.timeframes = TimeframeStatistics()

        self.sharpe = SharpeRatio()

    def report(self):

        Logger.section(
            "PERFORMANCE ANALYTICS"
        )

        trades = self.database.load_trades()

        if len(trades) == 0:

            Logger.warning(
                "Nessun trade presente."
            )

            return

        risk = self.risk.calculate(
            self.database
        )

        trade = self.trade_stats.calculate(
            self.database
        )

        monthly = self.monthly.calculate(
            self.database
        )

        symbols = self.symbols.calculate(
            self.database
        )

        timeframes = self.timeframes.calculate(
            self.database
        )

        sharpe = self.sharpe.calculate(
            self.database
        )

        equity = self.INITIAL_CAPITAL

        peak = equity

        max_drawdown = 0

        longest_win = 0

        longest_loss = 0

        current_win = 0

        current_loss = 0

        equity_curve = self.equity_curve.calculate(

            list(

                reversed(trades)

            )

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

        print("Trade Totali :", risk["total"])

        print("Trade Win    :", risk["wins"])

        print("Trade Loss   :", risk["losses"])

        print("Break Even   :", risk["breakeven"])

        print()

        print("Win Rate     :", risk["win_rate"], "%")

        print("Profit Factor:", risk["profit_factor"])

        print("Sharpe Ratio :", sharpe)

        print()

        print("Gross Profit :", risk["gross_profit"])

        print("Gross Loss   :", risk["gross_loss"])

        print("Profitto     :", self.database.total_profit())

        print("Best Trade   :", self.database.best_trade())

        print("Worst Trade  :", self.database.worst_trade())

        print("Media Trade  :", self.database.average_profit())

        print()

        print("Average Win  :", trade["average_win"])

        print("Average Loss :", trade["average_loss"])

        print("Expectancy   :", trade["expectancy"])

        print()

        print("ROI          :", roi, "%")

        print("Equity       :", round(equity, 2))

        print("Drawdown Max :", round(max_drawdown, 2))

        print()

        print("Win Streak   :", longest_win)

        print("Loss Streak  :", longest_loss)

        print()

        print("Performance Mensile")

        print("--------------------------------")

        for mese, profitto in monthly.items():

            print(mese, ":", round(profitto, 2))

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