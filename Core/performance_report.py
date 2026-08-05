"""
========================================
PROJECT PHOENIX AI
Performance Report
Versione 1.0
========================================
"""

from Logs.logger import Logger


class PerformanceReport:

    def __init__(self):

        Logger.success(

            "Performance Report V1 inizializzato."

        )

    def section(

        self,

        title

    ):

        print()

        print(title)

        print("--------------------------------")

    def line(

        self,

        label,

        value

    ):

        print(f"{label:<18}: {value}")