"""
========================================
PROJECT PHOENIX AI
Report CSV
Versione 2.0
========================================
"""

import csv

from Logs.logger import Logger


class ReportCSV:

    def __init__(self):

        Logger.success(
            "Report CSV V2 inizializzato."
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

            f"Report CSV salvato: {filename}"

        )