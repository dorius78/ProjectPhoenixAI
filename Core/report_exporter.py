"""
========================================
PROJECT PHOENIX AI
Report Exporter
Versione 1.0
========================================
"""

from Logs.logger import Logger
from datetime import datetime


class ReportExporter:

    def __init__(self):

        Logger.success(

            "Report Exporter V1 inizializzato."

        )

    def export_txt(

        self,

        filename,

        lines

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

                "PROJECT PHOENIX AI REPORT\n"

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

            for line in lines:

                file.write(

                    str(line)

                )

                file.write(

                    "\n"

                )

        Logger.success(

            f"Report salvato in {filename}"

        )