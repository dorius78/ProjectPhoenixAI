"""
========================================
PROJECT PHOENIX AI
Report Manager
Versione 2.0
========================================
"""

from Logs.logger import Logger

from Core.report_exporter import ReportExporter
from Core.report_formats import ReportFormats


class ReportManager:

    def __init__(self):

        Logger.success(
            "Report Manager V2 inizializzato."
        )

        self.exporter = ReportExporter()
        self.formats = ReportFormats()

    def export_performance(

        self,

        statistics,

        filename="performance_report"

    ):

        lines = self.formats.to_text(statistics)

        self.exporter.export_txt(

            filename + ".txt",

            lines

        )

    def export_csv(

        self,

        statistics,

        filename="performance_report"

    ):

        self.exporter.export_csv(

            filename + ".csv",

            statistics

        )

    def export_json(

        self,

        statistics,

        filename="performance_report"

    ):

        self.exporter.export_json(

            filename + ".json",

            statistics

        )

    def export_html(

        self,

        statistics,

        filename="performance_report"

    ):

        self.exporter.export_html(

            filename + ".html",

            statistics

        )

    def export_pdf(

        self,

        statistics,

        filename="performance_report"

    ):

        self.exporter.export_pdf(

            filename + ".pdf",

            statistics

        )

    def export_all(

        self,

        statistics,

        filename="performance_report"

    ):

        self.export_performance(

            statistics,

            filename

        )

        self.export_csv(

            statistics,

            filename

        )

        self.export_json(

            statistics,

            filename

        )

        self.export_html(

            statistics,

            filename

        )

        self.export_pdf(

            statistics,

            filename

        )