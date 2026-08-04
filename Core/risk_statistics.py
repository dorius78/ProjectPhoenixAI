"""
========================================
PROJECT PHOENIX AI
Risk Statistics
Versione 1.0
========================================
"""

from Logs.logger import Logger


class RiskStatistics:

    def __init__(self):

        Logger.success(

            "Risk Statistics V1 inizializzato."

        )

    def calculate(

        self,

        database

    ):

        total = database.count()

        wins = database.wins()

        losses = database.losses()

        breakeven = database.breakeven()

        gross_profit = database.gross_profit()

        gross_loss = database.gross_loss()

        profit_factor = database.profit_factor()

        win_rate = database.win_rate()

        return {

            "total": total,

            "wins": wins,

            "losses": losses,

            "breakeven": breakeven,

            "gross_profit": gross_profit,

            "gross_loss": gross_loss,

            "profit_factor": profit_factor,

            "win_rate": win_rate

        }