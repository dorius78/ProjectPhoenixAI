"""
========================================
PROJECT PHOENIX AI
Professional Logger
Versione 1.0
========================================
"""

from datetime import datetime


class Logger:

    @staticmethod
    def line():
        print("=" * 60)

    @staticmethod
    def section(title):
        print()
        Logger.line()
        print(f" {title}")
        Logger.line()

    @staticmethod
    def info(message):
        now = datetime.now().strftime("%H:%M:%S")
        print(f"[INFO {now}] {message}")

    @staticmethod
    def success(message):
        now = datetime.now().strftime("%H:%M:%S")
        print(f"[ OK  {now}] {message}")

    @staticmethod
    def warning(message):
        now = datetime.now().strftime("%H:%M:%S")
        print(f"[WARN {now}] {message}")

    @staticmethod
    def error(message):
        now = datetime.now().strftime("%H:%M:%S")
        print(f"[ERR  {now}] {message}")

    @staticmethod
    def value(name, value):
        print(f"{name:<25}: {value}")