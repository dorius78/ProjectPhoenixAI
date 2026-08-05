"""
========================================
PROJECT PHOENIX AI
JSON Report
Versione 1.0
========================================
"""

import json

from Logs.logger import Logger


class JSONReport:

    def __init__(self):

        Logger.success(

            "JSON Report V1 inizializzato."

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

                ensure_ascii=False

            )

        Logger.success(

            f"JSON creato: {filename}"

        )