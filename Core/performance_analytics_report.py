"""
========================================
PROJECT PHOENIX AI
Performance Analytics Report
Versione 2.0
========================================
"""

from Logs.logger import Logger


class PerformanceAnalyticsReport:

    def __init__(self):

        Logger.success(
            "Performance Report V2 inizializzato."
        )

    def print_summary(self, data):

        risk = data["risk"]
        trade = data["trade"]

        print()

        print("Trade Totali     :", risk["total"])
        print("Trade Win        :", risk["wins"])
        print("Trade Loss       :", risk["losses"])
        print("Break Even       :", risk["breakeven"])

        print()

        print("Win Rate         :", risk["win_rate"], "%")
        print("Win/Loss Ratio   :", data["winloss"])
        print("Profit Factor    :", risk["profit_factor"])
        print("Sharpe Ratio     :", data["sharpe"])
        print("Sortino Ratio    :", data["sortino"])
        print("Calmar Ratio     :", data["calmar"])
        print("Recovery Factor  :", data["recovery"])
        print("Ulcer Index      :", data["ulcer"])
        print("Omega Ratio      :", data["omega"])
        print("Profit/Drawdown  :", data["profit_dd"])
        print("Kelly Criterion  :", data["kelly"], "%")
        print("Payoff Ratio     :", data["payoff"])

        print()

        print("Gross Profit     :", data["gross_profit"])
        print("Gross Loss       :", data["gross_loss"])
        print("Profitto Netto   :", data["net_profit"])
        print("Best Trade       :", data["best_trade"])
        print("Worst Trade      :", data["worst_trade"])
        print("Media Trade      :", data["average_trade"])

        print()

        print("Average Win      :", trade["average_win"])
        print("Average Loss     :", trade["average_loss"])
        print("Expectancy       :", trade["expectancy"])

        print()

        print("ROI              :", data["roi"], "%")
        print("Equity           :", round(data["equity"], 2))
        print("Drawdown Max     :", round(data["drawdown"], 2))

        print()

        print("Win Streak       :", data["longest_win"])
        print("Loss Streak      :", data["longest_loss"])

    def print_monthly(self, data):

        print()

        print("Performance Mensile")
        print("--------------------------------")

        for mese, profitto in data["monthly"].items():

            print(
                mese,
                ":",
                round(profitto, 2)
            )

    def print_symbols(self, data):

        print()

        print("Performance per Simbolo")
        print("--------------------------------")

        for symbol, info in data["symbols"].items():

            print(

                f"{symbol:10}"

                f" Trades:{info['trades']:3}"

                f" Win:{info['wins']:3}"

                f" Loss:{info['losses']:3}"

                f" Profit:{round(info['profit'],2)}"

            )

    def print_timeframes(self, data):

        print()

        print("Performance per Timeframe")
        print("--------------------------------")

        for tf, info in data["timeframes"].items():

            print(

                f"{tf:6}"

                f" Trades:{info['trades']:3}"

                f" Profit:{round(info['profit'],2)}"

            )

    def print_equity_curve(self, data):

        print()

        print("Equity Curve")
        print("--------------------------------")

        for value in data["equity_curve"]:

            print(value)

    def print_report(self, data):

        self.print_summary(data)
        self.print_monthly(data)
        self.print_symbols(data)
        self.print_timeframes(data)
        self.print_equity_curve(data)