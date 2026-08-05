"""
========================================
PROJECT PHOENIX AI
Payoff Ratio
Versione 1.0
========================================
"""

from Logs.logger import Logger


class PayoffRatio:

    def __init__(self):

        Logger.success(

            "Payoff Ratio V1 inizializzato."

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

                    abs(

                        pnl

                    )

                )

        if len(wins) == 0:

            return 0.0

        if len(losses) == 0:

            return 0.0

        average_win = sum(

            wins

        ) / len(wins)

        average_loss = sum(

            losses

        ) / len(losses)

        if average_loss == 0:

            return 0.0

        return round(

            average_win /

            average_loss,

            3

        )