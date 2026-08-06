"""
========================================
PROJECT PHOENIX AI
Report Factory
Versione 1.0
========================================
"""

from Logs.logger import Logger

from Core.report_csv import ReportCSV
from Core.report_html import ReportHTML
from Core.report_json import ReportJSON
from Core.report_pdf import ReportPDF
from Core.report_exporter import ReportExporter


class ReportFactory:

    def __init__(self):

        Logger.success(

            "Report Factory V1 inizializzato."

        )

        self.txt = ReportExporter()
        self.csv = ReportCSV()
        self.html = ReportHTML()
        self.json = ReportJSON()
        self.pdf = ReportPDF()

    def export_txt(

        self,

        filename,

        lines

    ):

        self.txt.export_txt(

            filename,

            lines

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

    def export_html(

        self,

        filename,

        statistics

    ):

        self.html.export(

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

    def export_pdf(

        self,

        filename,

        statistics

    ):

        self.pdf.export(

            filename,

            statistics

        )