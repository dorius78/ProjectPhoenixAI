"""
========================================
PROJECT PHOENIX AI
Report Statistics
Versione 1.0
========================================
"""

from Logs.logger import Logger


class ReportStatistics:

    def __init__(self):

        Logger.success(

            "Report Statistics V1 inizializzato."

        )

    def build(

        self,

        risk,

        trade,

        roi,

        equity,

        drawdown,

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

    ):

        return {

            "Trade Totali": risk["total"],

            "Trade Win": risk["wins"],

            "Trade Loss": risk["losses"],

            "Break Even": risk["breakeven"],

            "Win Rate": str(risk["win_rate"]) + " %",

            "Win/Loss Ratio": winloss,

            "Profit Factor": risk["profit_factor"],

            "Sharpe Ratio": sharpe,

            "Sortino Ratio": sortino,

            "Calmar Ratio": calmar,

            "Recovery Factor": recovery,

            "Ulcer Index": ulcer,

            "Omega Ratio": omega,

            "Profit/Drawdown": profit_dd,

            "Kelly Criterion": str(kelly) + " %",

            "Payoff Ratio": payoff,

            "Gross Profit": risk["gross_profit"],

            "Gross Loss": risk["gross_loss"],

            "Average Win": trade["average_win"],

            "Average Loss": trade["average_loss"],

            "Expectancy": trade["expectancy"],

            "ROI": str(roi) + " %",

            "Equity": round(equity, 2),

            "Max Drawdown": round(drawdown, 2)

        }