"""
========================================
PROJECT PHOENIX AI
Professional Logger
Versione 7.0
========================================
"""

from datetime import datetime


class Logger:

    @staticmethod
    def _time():
        return datetime.now().strftime("%H:%M:%S")

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
        print(f"[INFO {Logger._time()}] {message}")

    @staticmethod
    def success(message):
        print(f"[ OK  {Logger._time()}] {message}")

    @staticmethod
    def warning(message):
        print(f"[WARN {Logger._time()}] {message}")

    @staticmethod
    def error(message):
        print(f"[ERR  {Logger._time()}] {message}")

    @staticmethod
    def value(name, value):
        print(f"{name:<25}: {value}")

    @staticmethod
    def debug(message):
        print(f"[DBG  {Logger._time()}] {message}")