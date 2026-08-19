# PROJECT PHOENIX AI
# PHOENIX MASTER STATE
# Versione 1.0
# Data: 2026-08-19

---

# 1. IDENTITÀ DEL PROGETTO

PROJECT PHOENIX AI non è un semplice Expert Advisor basato su indicatori.

Obiettivo finale:

costruire un vero SISTEMA OPERATIVO DI TRADING BASATO SU IA.

Il sistema deve essere capace di:

- acquisire dati di mercato;
- analizzare il mercato;
- utilizzare indicatori tecnici;
- analizzare struttura e Smart Money;
- generare segnali;
- valutare il rischio;
- costruire il trade;
- eseguire ordini;
- aprire posizioni;
- monitorare posizioni;
- modificare la gestione della posizione;
- applicare Stop Loss e Take Profit;
- applicare Break Even e Trailing Stop;
- chiudere posizioni;
- calcolare PnL;
- registrare i trade;
- aggiornare il capitale;
- effettuare backtest;
- effettuare Paper Trading;
- supportare MT5;
- supportare successivamente Live Trading;
- produrre statistiche e report.

Il sistema deve essere modulare, estendibile e progressivamente autonomo.

---

# 2. STATO DEL PROGETTO

STATO GENERALE:

INTEGRAZIONE AVANZATA / FASE DI STABILIZZAZIONE FINALE

Il progetto possiede già una struttura significativa.

NON ripartire da zero.

NON ricostruire i moduli già esistenti senza necessità.

Il lavoro futuro deve partire dallo stato GitHub:

COMMIT:
b47aa39

TAG:
PHOENIX_CHECKPOINT_2026-08-19

BACKUP LOCALE:

C:\ProjectPhoenixAI_BACKUP_2026-08-19

---

# 3. CONFIGURAZIONE CENTRALE

File:

Config/settings.py

Versione:

8.0

Configurazione attuale principale:

APP_NAME = "PROJECT PHOENIX AI"

VERSION = "0.0.1"

MODE = "DEMO"

SYMBOL = "BTC-USD"

MT5_SYMBOL = "BTCUSD"

PERIOD = "5d"

INTERVAL = "1h"

START_BALANCE = 10000

MAX_RISK = 1.0

MIN_CONFIDENCE = 60

STOP_LOSS_ATR = 1.5

TAKE_PROFIT_ATR = 3.0

MAX_DAILY_LOSS_PERCENT = 3.0

MAX_CONSECUTIVE_LOSSES = 4

COMMISSION = 0.001

SLIPPAGE = 0.0

Config/settings.py è considerato la fonte centrale della configurazione.

---

# 4. PIPELINE PRINCIPALE

Il pipeline logico di Phoenix è:

MARKET DATA
    ↓
CANDLES
    ↓
INDICATORS
    ↓
MARKET ANALYSIS
    ↓
SMART MONEY
    ↓
PHOENIX BRAIN
    ↓
SIGNAL MANAGER
    ↓
RISK MANAGER
    ↓
TRADE BUILDER
    ↓
EXECUTION
    ↓
POSITION CONTROLLER
    ↓
POSITION MONITOR
    ↓
EXIT MANAGER
    ↓
CLOSE
    ↓
TRADE REPORT
    ↓
DATABASE
    ↓
PORTFOLIO
    ↓
TRADING GUARD
    ↓
PERFORMANCE ANALYTICS
    ↓
REPORTING

---

# 5. MARKET DATA

Componenti presenti:

- Market Provider
- Yahoo Finance Provider
- Market Data Manager
- Candle Manager
- Symbols Manager
- Market Scanner

Il sistema è stato verificato con:

ETH-USD

e ha ricevuto:

106 candele

periodo:

5d

intervallo:

1h

---

# 6. ANALYSIS ENGINE

Presente:

Core/analysis_engine.py

Versione osservata:

9

Componenti:

- Indicator Manager
- Market Analyzer
- Smart Money
- Phoenix Brain
- Signal Manager
- Risk Manager
- Trade Manager

Il sistema ha già prodotto un esempio reale di:

STRONG BUY

e ha costruito:

BUY ETH-USD

con size:

15.57

---

# 7. INDICATOR ENGINE

Indicator Manager presente.

Indicatori presenti:

- EMA
- SMA
- RSI
- MACD
- ATR
- ADX
- Bollinger Bands

---

# 8. SMART MONEY

Componenti presenti:

Smart Money

Smart Money Structure

Smart Money FVG

Smart Money Order Blocks

Smart Money Liquidity

Versioni osservate:

Smart Money V13

Structure V4

FVG V2

Order Blocks V2

Liquidity V2

---

# 9. PHOENIX BRAIN

Componenti presenti:

Phoenix Brain

Phoenix Brain Logic

Versioni osservate:

Phoenix Brain V10

Phoenix Brain Logic V4

---

# 10. SIGNAL MANAGER

Presente.

Versione osservata:

Signal Manager V10

Il sistema ha già validato:

STRONG BUY

---

# 11. RISK MANAGEMENT

Presente:

Risk Manager

Risk Limits

Risk Drawdown

Trading Guard

Versioni osservate:

Risk Manager V11

Risk Limits V1

Risk Drawdown V1

Trading Guard V1

Protections:

MAX_DAILY_LOSS_PERCENT = 3.0

MAX_CONSECUTIVE_LOSSES = 4

---

# 12. TRADE MANAGER

File:

Core/trade_manager.py

Versione:

12.0

Componenti:

- RiskManager
- TradeBuilder
- TradeReport

Funzione principale:

generate_trade()

Responsabilità:

- ricevere signal;
- utilizzare risk manager;
- costruire trade;
- produrre report.

---

# 13. POSITION CONTROLLER

File:

Core/position_controller.py

Versione:

12.5

Componenti:

- PositionMonitor
- ExitManager

Gestisce:

- apertura posizione;
- aggiornamento;
- monitoraggio;
- PnL;
- Stop Loss;
- Take Profit;
- Break Even;
- Trailing Stop;
- chiusura;
- motivo chiusura;
- timestamp;
- posizione attiva.

La posizione contiene:

symbol
side
entry
initial_stop_loss
stop_loss
take_profit
size
status
open_time
close_time
close_reason
current_price
current_profit
max_profit
break_even
trailing_stop

È stato verificato il ciclo:

OPEN
→ UPDATE
→ CLOSE

Il PnL viene calcolato in base a:

BUY:
(exit - entry) * size

SELL:
(entry - exit) * size

---

# 14. POSITION MONITOR

Presente:

Core/position_monitor.py

Responsabilità:

aggiornare:

- current_price
- current_profit
- max_profit

e supportare la gestione dinamica della posizione.

---

# 15. EXIT MANAGER

Presente:

Core/exit_manager.py

Responsabilità:

valutare condizioni di uscita.

Possibili motivi:

- STOP LOSS
- TAKE PROFIT
- BREAK EVEN
- TRAILING STOP
- MANUALE / altro

---

# 16. PORTFOLIO MANAGER

File:

Core/portfolio_manager.py

Versione:

2.0

Gestisce:

- balance;
- positions;
- equity;
- profitto corrente;
- esposizione;
- aggiunta posizione;
- rimozione posizione;
- aggiornamento posizione.

START_BALANCE:

10000

Il portfolio viene aggiornato quando una posizione viene aperta e quando viene chiusa.

---

# 17. BACKTEST ENGINE

File:

Core/backtest_engine.py

Versione:

12.0

Gestisce:

- storico trade;
- numero trade;
- BUY;
- SELL;
- wins;
- losses;
- win rate;
- gross profit;
- gross loss;
- net profit;
- capital;
- ROI;
- profit factor;
- max drawdown;
- activity;
- market bias.

È già presente una correzione importante:

activity non viene più calcolata come:

(BUY + SELL) / total * 100

perché avrebbe prodotto quasi sempre 100%.

Ora viene calcolata in rapporto alle candele realmente analizzate.

---

# 18. DATABASE

File:

Database/database_manager.py

Versione:

6.0

Database:

SQLite

Tabella:

trades

Campi:

id
symbol
side
entry
exit
stop_loss
take_profit
pnl
status
reason
open_time
close_time
duration
result
risk_reward

Funzioni disponibili:

save_trade()
load_trades()
count()
wins()
losses()
breakeven()
total_profit()
gross_profit()
gross_loss()
best_trade()
worst_trade()
average_profit()
profit_factor()
win_rate()
reset()
close()

IMPORTANTE:

DatabaseManager NON si trova in:

Core/database_manager.py

Si trova in:

Database/database_manager.py

Questo percorso deve essere mantenuto oppure uniformato successivamente senza rompere gli import.

---

# 19. EXECUTION ENGINE

File:

Execution/execution_engine.py

Versione:

9.0

Supporta:

- Paper Trading;
- Execution Validator;
- Execution Builder;
- Execution Report;
- MT5 Bridge;
- DRY RUN;
- apertura;
- chiusura.

Configurazione:

mt5_enabled=False

mt5_dry_run=True

Paper Trading è attualmente il percorso principale verificato.

---

# 20. MT5 BRIDGE

File principale:

MT5_Bridge/mt5_execution_recovered.py

Supporta:

- connessione MT5;
- apertura ordine;
- modifica SL/TP;
- chiusura posizione;
- DRY RUN;
- order_check;
- order_send;
- BUY;
- SELL.

La logica di chiusura è:

BUY → SELL

SELL → BUY

con prezzo:

BUY close → BID

SELL close → ASK

---

# 21. LIVE TRADING ENGINE

File:

Core/live_trading_engine.py

Versione osservata:

5.2

Comportamento attuale:

Se non esiste una posizione:

1. scarica dati;
2. ottiene prezzo;
3. controlla Trading Guard;
4. analizza;
5. genera signal;
6. costruisce trade;
7. esegue;
8. apre posizione;
9. registra nel Portfolio.

Se esiste una posizione:

1. recupera prezzo corrente;
2. aggiorna Position Controller;
3. aggiorna Portfolio;
4. verifica chiusura;
5. registra trade chiuso;
6. aggiorna database;
7. aggiorna backtest;
8. aggiorna balance;
9. aggiorna Trading Guard.

Questo evita di scaricare inutilmente tutte le candele durante la gestione di una posizione già aperta.

---

# 22. TRADE CLOSE PIPELINE

Quando una posizione viene chiusa:

1. viene calcolato il prezzo finale;
2. viene calcolato il PnL;
3. viene determinato il motivo;
4. viene calcolata la durata;
5. viene calcolato Risk/Reward;
6. viene creato il record trade;
7. viene salvato nel Database;
8. viene aggiunto al Backtest Engine;
9. viene aggiornato il Portfolio balance;
10. viene aggiornato Trading Guard;
11. viene rimossa la posizione dal Portfolio.

---

# 23. PERFORMANCE ANALYTICS

Presenti:

- Equity Curve
- Risk Statistics
- Trade Statistics
- Monthly Statistics
- Symbol Statistics
- Timeframe Statistics
- Sharpe Ratio
- Sortino Ratio
- Calmar Ratio
- Recovery Factor
- Ulcer Index
- Omega Ratio
- Profit to Drawdown
- Kelly Criterion
- Payoff Ratio
- Win Loss Ratio

---

# 24. REPORTING

Presenti:

- Performance Report
- Report Statistics
- Report Service
- Report Factory
- Report Exporter
- CSV
- JSON
- HTML
- PDF
- Report Formats

---

# 25. MARKET SCANNER

Presente:

Market Scanner V2

Watchlist:

12 strumenti

---

# 26. CORE SYSTEM

Presente:

Core System V20

Responsabile dell'integrazione dei principali moduli Phoenix.

Il Core è già riuscito ad avviare Live Trading.

Esempio verificato:

ETH-USD

Prezzo:

1921.6700439453125

Segnale:

STRONG BUY

Trade:

BUY ETH-USD

Size:

15.57

Esecuzione:

Paper Trading

Posizione:

OPEN

Portfolio:

registrato

---

# 27. TEST GIÀ ESEGUITI

È stato verificato:

PositionController:

OPEN
→ UPDATE
→ CLOSE

Esempio:

entry = 100

SL = 95

TP = 110

size = 1

update = 102

close = 105

PnL finale:

+5

È stato verificato anche:

Integration Import Test

con:

DatabaseManager OK

BacktestEngine OK

PortfolioManager OK

PositionController OK

ExecutionEngine OK

---

# 28. GIT / BACKUP

Repository:

ProjectPhoenixAI

Branch:

main

Checkpoint:

b47aa39

Tag:

PHOENIX_CHECKPOINT_2026-08-19

Tag precedente:

v0.1-stable

Backup locale:

C:\ProjectPhoenixAI_BACKUP_2026-08-19

Il checkpoint è stato pubblicato su origin/main.

Il tag checkpoint è stato pubblicato su origin.

NON cancellare il backup.

NON modificare il checkpoint.

---

# 29. PROBLEMI NOTI / DA RISOLVERE

## PROBLEMA 1 — ExecutionEngine.close()

Nel codice attuale esiste una struttura errata nel dizionario di ritorno della chiusura MT5.

Deve essere verificato/corretto il campo:

dry_run

La struttura corretta deve essere:

"dry_run": result.get(
    "dry_run",
    self.mt5_dry_run
)

e non un valore senza chiave.

---

## PROBLEMA 2 — CONTRATTI TRA MODULI

Devono essere uniformati i contratti:

Trade
Order
Position
Closed Trade
Execution Result
Report

senza rompere il Core esistente.

---

## PROBLEMA 3 — PAPER vs MT5

Deve essere garantito che:

PAPER TRADING

e

MT5

utilizzino lo stesso contratto logico.

Il Core non deve conoscere dettagli specifici del broker.

---

## PROBLEMA 4 — CHIUSURA MT5

La chiusura MT5 deve essere integrata correttamente con:

Position Controller
Portfolio
Database
Trading Guard
Performance Analytics

---

## PROBLEMA 5 — GESTIONE POSIZIONI

Occorre completare e stabilizzare:

- Break Even;
- Trailing Stop;
- modifica SL;
- sincronizzazione Portfolio;
- sincronizzazione MT5;
- protezione da doppia chiusura.

---

## PROBLEMA 6 — BACKTEST

Il Backtest Engine esiste, ma deve essere collegato definitivamente al ciclo storico completo.

Obiettivo:

Candele
→ Analisi
→ Signal
→ Risk
→ Trade
→ Position
→ Exit
→ PnL
→ Statistics

---

## PROBLEMA 7 — DATABASE

Il Database Manager esiste e deve diventare il registro persistente ufficiale dei trade chiusi.

---

## PROBLEMA 8 — LIVE TRADING

Prima del LIVE reale deve essere completato:

Paper Trading
→ MT5 DRY RUN
→ MT5 DEMO
→ MT5 LIVE

senza saltare livelli.

---

# 30. ARCHITETTURA FINALE DESIDERATA

PROJECT PHOENIX AI deve arrivare a:

DATA INTELLIGENCE
+
MARKET INTELLIGENCE
+
NEWS INTELLIGENCE
+
SENTIMENT AI
+
TECHNICAL AI
+
PATTERN RECOGNITION
+
SMART MONEY
+
RISK AI
+
DECISION AI
+
EXECUTION
+
POSITION MANAGEMENT
+
PORTFOLIO
+
BACKTEST
+
PAPER TRADING
+
LIVE TRADING
+
PERFORMANCE ANALYTICS
+
DATABASE
+
REPORTING

---

# 31. REGOLA DI SVILUPPO

NON ricominciare da zero.

NON sostituire moduli funzionanti senza motivo.

NON duplicare funzionalità.

NON introdurre configurazioni duplicate.

Ogni modifica deve:

1. preservare il funzionamento esistente;
2. migliorare l'integrazione;
3. mantenere compatibilità;
4. essere salvata in Git;
5. essere documentata nel MASTER STATE quando cambia l'architettura.

---

# 32. ORDINE DELLE PROSSIME FASI

FASE A
Stabilizzazione Execution Engine.

FASE B
Stabilizzazione ciclo completo Position → Close.

FASE C
Integrazione Database + Portfolio + Guard.

FASE D
Backtest end-to-end.

FASE E
Paper Trading end-to-end.

FASE F
MT5 DRY RUN.

FASE G
MT5 DEMO.

FASE H
Performance e Reporting finale.

FASE I
Live Trading controllato.

FASE L
Espansione AI:

- News Intelligence
- Sentiment AI
- Decision AI avanzata
- Pattern Recognition avanzata
- Market Regime Detection
- Adaptive Risk
- Multi-market intelligence

---

# 33. OBIETTIVO RELEASE

La prima release completa deve essere:

PROJECT PHOENIX AI

Trading Operating System

con:

DATA
→ INTELLIGENCE
→ DECISION
→ RISK
→ EXECUTION
→ POSITION
→ PORTFOLIO
→ PERFORMANCE

completamente integrati.

---

# 34. STATO MASTER

Questo file diventa il riferimento ufficiale dello stato del progetto a partire dal:

2026-08-19

Checkpoint precedente:

PHOENIX_CHECKPOINT_2026-08-19

Prossimo obiettivo:

FINAL INTEGRATION