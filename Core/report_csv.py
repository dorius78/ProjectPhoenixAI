"""
========================================
PROJECT PHOENIX AI
CSV Report
Versione 1.0
========================================
"""

import csv

from Logs.logger import Logger


class CSVReport:

    def __init__(self):

        Logger.success(

            "CSV Report V1 inizializzato."

        )

    def export(

        self,

        filename,

        statistics

    ):

        with open(

            filename,

            "w",

            newline="",

            encoding="utf-8"

        ) as file:

            writer = csv.writer(file)

            writer.writerow(

                [

                    "Parametro",

                    "Valore"

                ]

            )

            for key, value in statistics.items():

                writer.writerow(

                    [

                        key,

                        value

                    ]

                )

        Logger.success(

            f"CSV creato: {filename}"

        )