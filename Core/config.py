"""
PROJECT PHOENIX AI
Configuration Manager
"""

class Config:

    APP_NAME = "PROJECT PHOENIX AI"
    VERSION = "0.0.1"

    MODE = "DEMO"          # DEMO oppure LIVE

    START_BALANCE = 10000

    MAX_RISK = 1.0         # Percentuale di rischio per operazione

    CURRENCIES = [
        "EURUSD",
        "GBPUSD",
        "USDJPY",
        "XAUUSD"
    ]