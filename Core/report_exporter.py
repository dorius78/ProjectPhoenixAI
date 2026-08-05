"""
========================================
PROJECT PHOENIX AI
Report Exporter
Versione 2.0
========================================
"""

import csv
import json

from datetime import datetime

from Logs.logger import Logger

from Core.report_csv import ReportCSV
from Core.report_json import ReportJSON
from Core.report_html import ReportHTML
from Core.report_pdf import ReportPDF


class ReportExporter:

    def __init__(self):

        Logger.success(
            "Report Exporter V2 inizializzato."
        )

        self.csv = ReportCSV()
        self.json = ReportJSON()
        self.html = ReportHTML()
        self.pdf = ReportPDF()

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

            f"Report TXT salvato in {filename}"

        )

    def export_csv(

        self,

        filename,

        statistics

    ):

        self.csv.export(

            filename,

            statistics

        )

    def export_json(

        self,

        filename,

        statistics

    ):

        self.json.export(

            filename,

            statistics

        )

    def export_html(

        self,

        filename,

        statistics

    ):

        self.html.export(

            filename,

            statistics

        )

    def export_pdf(

        self,

        filename,

        statistics

    ):

        self.pdf.export(

            filename,

            statistics
        )

    def export_all(

        self,

        filename,

        statistics,

        lines

    ):

        self.export_txt(

            filename + ".txt",

            lines

        )

        self.export_csv(

            filename + ".csv",

            statistics

        )

        self.export_json(

            filename + ".json",

            statistics

        )

        self.export_html(

            filename + ".html",

            statistics

        )

        self.export_pdf(

            filename + ".pdf",

            statistics

        )