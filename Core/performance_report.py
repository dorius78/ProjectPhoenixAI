"""
========================================
PROJECT PHOENIX AI
Performance Report
Versione 2.0
========================================
"""

from Logs.logger import Logger


class PerformanceReport:

    def __init__(self):

        Logger.success(

            "Performance Report V2 inizializzato."

        )

        self.rows = []

    def clear(self):

        self.rows = []

    def line(self, label, value):

        self.rows.append(

            (label, value)

        )

    def print(self):

        print()

        for label, value in self.rows:

            print(

                f"{label:<18}: {value}"

            )

        print()