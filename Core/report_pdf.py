"""
========================================
PROJECT PHOENIX AI
Report PDF
Versione 2.0
========================================
"""

from datetime import datetime

from Logs.logger import Logger


class ReportPDF:

    def __init__(self):

        Logger.success(
            "Report PDF V2 inizializzato."
        )

    def export(

        self,

        filename,

        statistics

    ):

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(
                "========================================\n"
            )

            file.write(
                "PROJECT PHOENIX AI\n"
            )

            file.write(
                "PERFORMANCE REPORT\n"
            )

            file.write(
                "========================================\n\n"
            )

            file.write(
                "Creato: "
            )

            file.write(
                str(
                    datetime.now()
                )
            )

            file.write(
                "\n\n"
            )

            for key, value in statistics.items():

                file.write(

                    f"{key:<25}: {value}\n"

                )

        Logger.success(

            f"Report PDF salvato: {filename}"

        )