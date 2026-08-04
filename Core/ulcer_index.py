"""
========================================
PROJECT PHOENIX AI
Ulcer Index
Versione 1.0
========================================
"""

import math

from Logs.logger import Logger


class UlcerIndex:

    def __init__(self):

        Logger.success(

            "Ulcer Index V1 inizializzato."

        )

    def calculate(

        self,

        database

    ):

        trades = database.load_trades()

        if len(trades) == 0:

            return 0.0

        equity = 10000.0

        peak = equity

        drawdowns = []

        for trade in trades:

            equity += float(

                trade[7]

            )

            if equity > peak:

                peak = equity

            dd = (

                (peak - equity)

                /

                peak

            ) * 100

            drawdowns.append(

                dd

            )

        if len(drawdowns) == 0:

            return 0.0

        value = math.sqrt(

            sum(

                d ** 2

                for d in drawdowns

            )

            /

            len(drawdowns)

        )

        return round(

            value,

            3

        )