"""
========================================
PROJECT PHOENIX AI
Risk Drawdown
Versione 1.0
========================================
"""

from Logs.logger import Logger


class RiskDrawdown:

    def __init__(self):

        Logger.success(
            "Risk Drawdown V1 inizializzato."
        )

    def calculate(self, equity_curve):

        if not equity_curve:

            return 0.0

        peak = equity_curve[0]
        max_drawdown = 0.0

        for equity in equity_curve:

            if equity > peak:

                peak = equity

            drawdown = peak - equity

            if drawdown > max_drawdown:

                max_drawdown = drawdown

        return round(max_drawdown, 2)