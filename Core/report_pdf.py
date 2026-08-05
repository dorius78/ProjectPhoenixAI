"""
========================================
PROJECT PHOENIX AI
PDF Report
Versione 1.0
========================================
"""

from Logs.logger import Logger


class PDFReport:

    def __init__(self):

        Logger.success(

            "PDF Report V1 inizializzato."

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

            for key, value in statistics.items():

                file.write(

                    f"{key:<25}: {value}\n"

                )

        Logger.success(

            f"PDF Report creato: {filename}"

        )