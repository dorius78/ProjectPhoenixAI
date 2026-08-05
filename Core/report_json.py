"""
========================================
PROJECT PHOENIX AI
Report JSON
Versione 2.0
========================================
"""

import json

from Logs.logger import Logger


class ReportJSON:

    def __init__(self):

        Logger.success(
            "Report JSON V2 inizializzato."
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

            json.dump(

                statistics,

                file,

                indent=4,

                ensure_ascii=False,

                default=str

            )

        Logger.success(

            f"Report JSON salvato: {filename}"

        )