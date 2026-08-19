"""
========================================
PROJECT PHOENIX AI
Settings
Versione 8.0

Questa e' l'UNICA fonte di configurazione del progetto. Prima
esisteva anche Core/config.py con alcuni parametri duplicati
(es. MAX_RISK con due valori diversi, 1.0 e 2.0) e altri presenti
solo li' (APP_NAME, MODE, START_BALANCE, CURRENCIES): tutto e'
stato unificato qui per evitare che due moduli leggano parametri
diversi per lo stesso concetto.
========================================
"""

# ======================================
# PROGETTO
# ======================================

APP_NAME = "PROJECT PHOENIX AI"

VERSION = "0.0.1"

MODE = "DEMO"          # DEMO oppure LIVE

# ======================================
# MERCATO
# ======================================

# Simbolo utilizzato dal sistema dati/analisi
SYMBOL = "BTC-USD"

# Simbolo reale utilizzato da MetaTrader 5
MT5_SYMBOL = "BTCUSD"

PERIOD = "5d"

INTERVAL = "1h"

CURRENCIES = [
    "EURUSD",
    "GBPUSD",
    "USDJPY",
    "XAUUSD"
]

# ======================================
# INDICATORI
# ======================================

EMA_PERIOD = 20

EMA_FAST = 20

EMA_SLOW = 50

SMA_PERIOD = 20

RSI_PERIOD = 14

ATR_PERIOD = 14

ADX_PERIOD = 14

# ======================================
# MACD
# ======================================

MACD_FAST = 12

MACD_SLOW = 26

MACD_SIGNAL = 9

# ======================================
# BOLLINGER
# ======================================

BOLLINGER_PERIOD = 20

BOLLINGER_STD = 2

# ======================================
# TRADE
# ======================================

STOP_LOSS_ATR = 1.5

TAKE_PROFIT_ATR = 3.0

# ======================================
# RISK MANAGEMENT
# ======================================

# Prima erano due valori diversi in due file (1.0 in Core/config.py,
# 2.0 qui): quello realmente in uso per il position sizing era 1.0
# (Core/config.py), quindi e' quello mantenuto per non alterare il
# comportamento gia' verificato nei backtest.
MAX_RISK = 1.0

MIN_CONFIDENCE = 60

# ======================================
# PROTEZIONI LIVE TRADING
# ======================================

# Se la perdita del giorno supera questa percentuale del saldo
# di inizio giornata, il Live Trading si ferma da solo (nessun
# nuovo trade, quelli aperti restano gestiti fino alla chiusura
# naturale via SL/TP).
MAX_DAILY_LOSS_PERCENT = 3.0

# Se si accumulano questi trade in perdita DI FILA, il Live
# Trading si ferma da solo (protezione contro condizioni di
# mercato anomale o un bug non ancora scoperto).
MAX_CONSECUTIVE_LOSSES = 4

# ======================================
# CAPITALE / BACKTEST
# ======================================

START_BALANCE = 10000

COMMISSION = 0.001

SLIPPAGE = 0.0

# ======================================
# LOG
# ======================================

LOG_LEVEL = "INFO"