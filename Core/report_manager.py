"""
========================================
PROJECT PHOENIX AI
Report Manager
Versione 1.0
========================================
"""

from Logs.logger import Logger

from Core.report_exporter import ReportExporter


class ReportManager:

    def __init__(self):

        Logger.success(

            "Report Manager V1 inizializzato."

        )

        self.exporter = ReportExporter()

    def export_performance(

        self,

        statistics,

        filename="performance_report.txt"

    ):

        lines = []

        for key, value in statistics.items():

            lines.append(

                f"{key:<20}: {value}"

            )

        self.exporter.export_txt(

            filename,

            lines

        )