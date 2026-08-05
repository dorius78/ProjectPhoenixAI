"""
========================================
PROJECT PHOENIX AI
Report Writer
Versione 1.0
========================================
"""

from Logs.logger import Logger


class ReportWriter:

    def __init__(self):

        Logger.success(

            "Report Writer V1 inizializzato."

        )

    def write(

        self,

        filename,

        lines

    ):

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            for line in lines:

                file.write(

                    str(line)

                )

                file.write(

                    "\n"

                )

        Logger.success(

            f"File creato: {filename}"

        )