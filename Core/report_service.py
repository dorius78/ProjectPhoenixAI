"""
========================================
PROJECT PHOENIX AI
Report Service
Versione 1.0
========================================
"""

from Logs.logger import Logger

from Core.report_factory import ReportFactory
from Core.report_formats import ReportFormats


class ReportService:

    def __init__(self):

        Logger.success(

            "Report Service V1 inizializzato."

        )

        self.factory = ReportFactory()

        self.formats = ReportFormats()

    def export_all(

        self,

        statistics,

        prefix="performance_report"

    ):

        lines = self.formats.performance(

            statistics

        )

        self.factory.export_txt(

            prefix + ".txt",

            lines

        )

        self.factory.export_csv(

            prefix + ".csv",

            statistics

        )

        self.factory.export_json(

            prefix + ".json",

            statistics

        )

        self.factory.export_html(

            prefix + ".html",

            statistics

        )

        self.factory.export_pdf(

            prefix + ".pdf",

            statistics

        )