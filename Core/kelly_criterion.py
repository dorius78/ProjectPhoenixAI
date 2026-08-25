"""
========================================
PROJECT PHOENIX AI
Kelly Criterion
Versione 1.0
========================================
"""

from Logs.logger import Logger


class KellyCriterion:

    def __init__(self):

        Logger.success(

            "Kelly Criterion V1 inizializzato."

        )

    def calculate(

        self,

        database

    ):

        trades = database.load_trades()

        if len(trades) == 0:

            return 0.0

        wins = []

        losses = []

        for trade in trades:

            pnl = float(

                trade[7]

            )

            if pnl > 0:

                wins.append(

                    pnl

                )

            elif pnl < 0:

                losses.append(

                    abs(pnl)

                )

        if len(wins) == 0 or len(losses) == 0:

            return 0.0

        win_rate = len(

            wins

        ) / (

            len(wins) + len(losses)

        )

        avg_win = sum(

            wins

        ) / len(wins)

        avg_loss = sum(

            losses

        ) / len(losses)

        if avg_loss == 0:

            return 0.0

        ratio = avg_win / avg_loss

        kelly = win_rate - (

            (1 - win_rate)

            /

            ratio

        )

        return round(

            kelly * 100,

            2

        )