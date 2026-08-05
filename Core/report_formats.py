"""
========================================
PROJECT PHOENIX AI
Report Formats
Versione 1.0
========================================
"""

from Logs.logger import Logger


class ReportFormats:

    def __init__(self):

        Logger.success(

            "Report Formats V1 inizializzato."

        )

    def performance(self, statistics):

        lines = []

        lines.append("========================================")
        lines.append("PROJECT PHOENIX AI")
        lines.append("PERFORMANCE REPORT")
        lines.append("========================================")
        lines.append("")

        for key, value in statistics.items():

            lines.append(

                f"{key:<25}: {value}"

            )

        return lines