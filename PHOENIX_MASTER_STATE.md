# ============================================================
# PROJECT PHOENIX AI
# PHOENIX MASTER STATE
# ============================================================

Versione documento: 1.0
Data: 10/08/2026

Questo documento è la memoria principale del progetto.
Deve essere mantenuto aggiornato durante tutto lo sviluppo.

============================================================
1. IDENTITÀ DEL PROGETTO
============================================================

Nome:
PROJECT PHOENIX AI

Obiettivo:

Costruire un sistema di trading autonomo capace di:

- acquisire dati di mercato;
- analizzare dati attuali e storici;
- analizzare più strumenti e timeframe;
- utilizzare indicatori tecnici;
- analizzare Market Structure;
- analizzare Smart Money;
- valutare trend, momentum, volatilità e volume;
- individuare opportunità;
- prendere decisioni autonomamente;
- valutare il rischio;
- decidere se operare oppure non operare;
- costruire il trade;
- controllare l'operazione prima dell'esecuzione;
- eseguire tramite simulazione, DEMO e successivamente MT5;
- monitorare le posizioni;
- gestire SL, TP, break-even e trailing;
- chiudere le operazioni;
- registrare ogni operazione;
- analizzare le performance;
- studiare gli storici;
- ricercare pattern e condizioni di mercato;
- validare le strategie;
- migliorare progressivamente il sistema attraverso ricerca,
  test e validazione.

Phoenix AI deve diventare un sistema autonomo.

NON deve essere un semplice generatore di segnali BUY/SELL.

============================================================
2. FILOSOFIA DEL SISTEMA
============================================================

Regola 1:

MAI prendere una decisione senza dati.

Regola 2:

MAI eseguire un'operazione senza controllo del rischio.

Regola 3:

MAI superare i limiti di sicurezza.

Regola 4:

MAI considerare una strategia valida soltanto perché ha
funzionato sul passato.

Regola 5:

Ogni strategia o modifica importante deve essere testata
e validata prima dell'utilizzo operativo.

Regola 6:

Meglio NON operare che eseguire un'operazione non sufficientemente
valida o non controllata.

Regola 7:

Non creare moduli duplicati se una funzione equivalente esiste già.

============================================================
3. CARTELLA PRINCIPALE DEL PROGETTO
============================================================

Cartella principale di lavoro:

C:\ProjectPhoenixAI

Questa è la cartella principale da utilizzare per lo sviluppo.

La vecchia copia OneDrive/GitHub non deve essere utilizzata
per lo sviluppo quotidiano.

GitHub è il sistema di versionamento e backup del codice.

Repository:

ProjectPhoenixAI

Branch principale:

main

============================================================
4. STATO GIT
============================================================

Ultimo commit importante verificato:

6ae57df

Messaggio:

Project Phoenix AI - MT5 and Trading Guard

Stato verificato:

Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

Il progetto deve essere salvato su GitHub dopo ogni fase
importante e dopo modifiche verificate.

============================================================
5. SICUREZZA CREDENZIALI
============================================================

ATTENZIONE:

Le credenziali reali MT5 NON devono essere inserite nel repository
GitHub.

File protetto:

Config/mt5_credentials.py

Il file è escluso tramite .gitignore.

Nel repository deve essere presente soltanto:

Config/mt5_credentials.example.py

Le password reali non devono essere inserite in questo documento.

============================================================
6. ARCHITETTURA ATTUALE
============================================================

Struttura concettuale:

MARKET DATA
    |
    v
ANALYSIS
    |
    v
SMART MONEY
    |
    v
PHOENIX BRAIN
    |
    v
SIGNAL MANAGER
    |
    v
RISK MANAGER
    |
    v
TRADING GUARD
    |
    v
TRADE MANAGER
    |
    v
EXECUTION
    |
    v
POSITION MANAGEMENT
    |
    v
DATABASE
    |
    v
PERFORMANCE ANALYTICS
    |
    v
LEARNING / RESEARCH

============================================================
7. MODULI GIÀ PRESENTI
============================================================

CORE

- Core System
- Market Data Manager
- Candle Manager
- Analysis Engine
- Indicator Manager
- Market Analyzer
- Smart Money
- Phoenix Brain
- Phoenix Brain Logic
- Signal Manager
- Risk Manager
- Trade Manager
- Position Controller
- Portfolio Manager
- Backtest Engine
- Database Manager
- Performance Analytics
- Market Scanner
- Live Trading Engine
- Trading Guard

INDICATORI

- EMA
- SMA
- RSI
- MACD
- ATR
- ADX
- Bollinger Bands

SMART MONEY

- Smart Money Structure
- Smart Money FVG
- Smart Money Order Blocks
- Smart Money Liquidity

RISK

- Risk Manager
- Risk Limits
- Risk Position Size
- Risk Drawdown
- Trading Guard

TRADE

- Trade Builder
- Trade Report
- Trade Manager

EXECUTION

- Execution Engine
- Execution Validator
- Execution Builder
- Execution Report
- MT5 Broker (preparazione)

PERFORMANCE

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

REPORTING

- Performance Report
- Report Statistics
- Report Service
- Report Factory
- Report Exporter
- Report CSV
- Report JSON
- Report HTML
- Report PDF
- Report Formats

TEST / MT5

- Tests/find_symbol.py
- Tests/test_mt5_connection.py
- find_symbol.py
- Execution/mt5_broker.py

============================================================
8. MARKET DATA
============================================================

Provider attualmente presente:

Yahoo Finance

Il sistema deve essere progettato per poter integrare
successivamente altre fonti dati.

Obiettivo finale:

- dati real-time;
- dati storici;
- OHLCV;
- timestamp;
- simbolo;
- timeframe;
- aggiornamento automatico;
- storico esteso;
- gestione di più mercati.

============================================================
9. ANALISI TECNICA
============================================================

Phoenix utilizza:

- EMA
- SMA
- RSI
- MACD
- ATR
- ADX
- Bollinger Bands
- trend
- momentum
- volume
- volatilità

L'analisi deve essere combinata.

NON utilizzare un singolo indicatore come decisione autonoma
di acquisto o vendita.

============================================================
10. SMART MONEY
============================================================

Phoenix deve analizzare:

- Break of Structure (BOS)
- Change of Character (CHoCH)
- Fair Value Gap (FVG)
- Order Block
- Liquidity Sweep

Questi elementi devono contribuire alla valutazione
complessiva del mercato.

============================================================
11. PHOENIX BRAIN
============================================================

Phoenix Brain è il motore decisionale.

Input:

- trend
- EMA
- MACD
- RSI
- ADX
- volume
- Smart Money
- altri dati disponibili
- rischio

Output:

- action
- score
- confidence
- strength
- risk
- reasons
- warnings

Azioni:

- STRONG BUY
- BUY
- HOLD
- SELL
- STRONG SELL

Il Brain attuale è un sistema decisionale deterministico.

NON deve essere considerato ancora un sistema completo
di Machine Learning.

============================================================
12. RISK MANAGER
============================================================

Il Risk Manager deve controllare:

- livello di rischio;
- rischio per operazione;
- position size;
- ATR;
- Stop Loss;
- Take Profit;
- Risk/Reward;
- drawdown;
- limiti operativi.

Il rischio deve avere priorità sulla decisione di trading.

============================================================
13. TRADING GUARD
============================================================

Trading Guard protegge il sistema.

Controlla almeno:

- perdita giornaliera;
- perdite consecutive;
- reset giornaliero;
- possibilità di continuare a operare.

Se viene raggiunto un limite:

TRADING BLOCCATO.

Il Trading Guard deve essere integrato nel flusso operativo
prima dell'esecuzione.

============================================================
14. TRADE MANAGER
============================================================

Il Trade Manager costruisce il trade.

Informazioni principali:

- symbol
- signal
- side
- entry
- stop_loss
- take_profit
- ATR
- risk_reward

Il trade deve essere costruito soltanto dopo che la decisione
è stata verificata.

============================================================
15. EXECUTION ENGINE
============================================================

Execution Engine comprende:

- Execution Validator
- Execution Builder
- Execution Report

Prima dell'esecuzione deve verificare:

- trade valido;
- segnale valido;
- side valido;
- entry;
- stop loss;
- take profit;
- risk/reward;
- condizioni di sicurezza.

Un errore deve portare a:

NESSUNA ESECUZIONE.

============================================================
16. POSITION MANAGEMENT
============================================================

QUESTA AREA NON È ANCORA COMPLETATA.

Deve essere completata con:

- Position Manager
- Position Monitor
- Exit Manager

Il ciclo completo deve diventare:

ENTRY
  |
  v
OPEN
  |
  v
MONITOR
  |
  +--> BREAK EVEN
  |
  +--> TRAILING STOP
  |
  +--> TAKE PROFIT
  |
  +--> STOP LOSS
  |
  +--> ALTRA USCITA VALIDA
  |
  v
CLOSE

============================================================
17. TRADE JOURNAL
============================================================

DA COMPLETARE.

Ogni operazione deve essere registrata con informazioni
sufficienti per poterla analizzare successivamente.

Dati desiderati:

- timestamp;
- symbol;
- timeframe;
- signal;
- side;
- score;
- confidence;
- entry;
- stop loss;
- take profit;
- exit;
- PnL;
- rischio;
- durata;
- motivo ingresso;
- motivo uscita;
- condizioni di mercato;
- risultato.

============================================================
18. DATABASE
============================================================

Database Manager già presente.

Il database deve diventare la memoria operativa del sistema.

Deve permettere di conservare:

- operazioni;
- risultati;
- performance;
- condizioni di mercato;
- segnali;
- decisioni;
- statistiche.

============================================================
19. PERFORMANCE ANALYTICS
============================================================

Sistema già molto avanzato.

Metriche presenti:

- Equity Curve
- Win Rate
- Win/Loss Ratio
- Profit Factor
- Sharpe Ratio
- Sortino Ratio
- Calmar Ratio
- Recovery Factor
- Ulcer Index
- Omega Ratio
- Profit/Drawdown
- Kelly Criterion
- Payoff Ratio
- Gross Profit
- Gross Loss
- Net Profit
- Best Trade
- Worst Trade
- Average Trade
- Average Win
- Average Loss
- Expectancy
- ROI
- Drawdown
- Win Streak
- Loss Streak
- Monthly Performance
- Symbol Performance
- Timeframe Performance

Questa area deve essere mantenuta e migliorata senza
creare duplicati.

============================================================
20. REPORTING
============================================================

Formati presenti:

- CSV
- JSON
- HTML
- PDF

Il reporting deve permettere di analizzare il comportamento
del sistema in modo chiaro.

============================================================
21. MARKET SCANNER
============================================================

Market Scanner presente.

Watchlist attuale verificata:

12 strumenti.

Obiettivo finale:

Phoenix deve poter:

- analizzare più strumenti;
- confrontarli;
- assegnare score;
- valutare confidence;
- valutare rischio;
- classificare opportunità;
- scegliere autonomamente le migliori opportunità.

============================================================
22. BACKTEST
============================================================

Backtest Engine presente.

Il backtest finale deve riprodurre il più possibile
l'intero processo operativo:

DATI STORICI
    |
    v
ANALISI
    |
    v
SMART MONEY
    |
    v
PHOENIX BRAIN
    |
    v
RISK
    |
    v
TRADING GUARD
    |
    v
TRADE
    |
    v
EXECUTION SIMULATA
    |
    v
POSITION MANAGEMENT
    |
    v
CLOSE
    |
    v
DATABASE
    |
    v
PERFORMANCE

============================================================
23. PAPER TRADING
============================================================

DA SVILUPPARE.

Phoenix deve poter lavorare su dati di mercato aggiornati
senza utilizzare denaro reale.

Obiettivo:

PAPER TRADING COMPLETAMENTE AUTONOMO.

============================================================
24. MT5
============================================================

Preparazione MT5 già presente.

File:

Execution/mt5_broker.py

Configurazione:

Config/mt5_credentials.example.py

Le credenziali reali sono escluse da GitHub.

Obiettivo:

- connessione MT5;
- controllo simboli;
- verifica account;
- esecuzione ordini;
- gestione posizioni;
- verifica ordini;
- gestione errori.

Prima del LIVE devono essere completati:

- Position Management;
- Exit Management;
- Trade Journal;
- Paper Trading;
- test DEMO;
- test di sicurezza;
- test di errore;
- validazione completa.

============================================================
25. AUTONOMIA
============================================================

OBIETTIVO FINALE.

Phoenix deve poter operare autonomamente.

Flusso:

DATI
  |
  v
ANALISI
  |
  v
RICERCA OPPORTUNITÀ
  |
  v
CLASSIFICAZIONE MERCATO
  |
  v
PHOENIX BRAIN
  |
  v
DECISIONE
  |
  v
RISK MANAGER
  |
  v
TRADING GUARD
  |
  v
TRADE MANAGER
  |
  v
EXECUTION
  |
  v
POSITION MANAGEMENT
  |
  v
CLOSE
  |
  v
DATABASE
  |
  v
PERFORMANCE
  |
  v
RESEARCH / LEARNING

Phoenix deve poter decidere anche:

NON OPERARE.

============================================================
26. HISTORICAL MARKET RESEARCH
============================================================

QUESTA È UNA DELLE GRANDI FASI FUTURE.

Phoenix deve utilizzare lo storico Yahoo Finance e,
successivamente, altre fonti.

Obiettivo:

non utilizzare lo storico soltanto per il backtest.

Phoenix deve STUDIARE lo storico.

Deve analizzare:

- trend;
- volatilità;
- volume;
- indicatori;
- market structure;
- Smart Money;
- pattern;
- comportamenti ricorrenti;
- condizioni favorevoli;
- condizioni sfavorevoli;
- performance per timeframe;
- performance per simbolo;
- performance per regime di mercato;
- risultati delle strategie.

Pipeline:

HISTORICAL DATA
    |
    v
HISTORICAL DATABASE
    |
    v
MARKET RESEARCH ENGINE
    |
    v
PATTERN ANALYSIS
    |
    v
MARKET REGIME ANALYSIS
    |
    v
STRATEGY TEST
    |
    v
VALIDATION
    |
    v
PAPER TRADING

============================================================
27. STRATEGY DISCOVERY
============================================================

DA SVILUPPARE.

Phoenix deve poter studiare quali combinazioni di condizioni
hanno prodotto risultati storicamente favorevoli.

NON bisogna semplicemente cercare la strategia con il profitto
più alto sul passato.

Devono essere utilizzati:

- backtest;
- out-of-sample test;
- walk-forward test;
- paper trading;
- controlli di robustezza.

============================================================
28. LEARNING ENGINE
============================================================

DA SVILUPPARE.

Il sistema dovrà poter analizzare i risultati delle operazioni
e identificare:

- condizioni favorevoli;
- condizioni sfavorevoli;
- errori ricorrenti;
- mercati più adatti;
- timeframe più adatti;
- strategie più robuste.

Il Learning Engine NON deve modificare liberamente il sistema
e mandare immediatamente ordini reali.

Ogni modifica deve essere:

RICERCATA
  |
  v
TESTATA
  |
  v
VALIDATA
  |
  v
APPROVATA
  |
  v
UTILIZZATA

============================================================
29. MACHINE LEARNING
============================================================

DA SVILUPPARE PIÙ AVANTI.

Il Machine Learning non è il prossimo passo.

Prima devono essere completati:

- dati;
- storico;
- database;
- backtest;
- position management;
- journal;
- paper trading;
- validazione.

Solo dopo si valuteranno:

- pattern recognition;
- regime detection;
- strategy optimization;
- machine learning.

============================================================
30. SUPERVISOR / DEVIL'S ADVOCATE
============================================================

DA SVILUPPARE.

Prima di un'operazione Phoenix deve poter avere un controllo
indipendente che cerchi motivi per NON eseguire il trade.

Esempio:

PHOENIX BRAIN:
"BUY"

SUPERVISOR:
"Quali sono i motivi per NON entrare?"

Controlli possibili:

- volatilità;
- spread;
- liquidità;
- drawdown;
- correlazioni;
- mercato laterale;
- eventi importanti;
- rischio portafoglio;
- qualità del segnale.

Obiettivo:

ridurre le decisioni deboli.

============================================================
31. MULTI-MARKET
============================================================

Phoenix deve poter confrontare:

- Forex;
- Crypto;
- Gold;
- Silver;
- altri strumenti disponibili.

Non deve necessariamente operare su tutti.

Deve scegliere le opportunità migliori in rapporto al rischio
complessivo.

============================================================
32. MODALITÀ OPERATIVE
============================================================

MODALITÀ 1:

Scanner Multi Market

MODALITÀ 2:

Live Trading

MODALITÀ 3:

Backtest

MODALITÀ 4:

Database Trade

MODALITÀ 5:

Performance Analytics

In futuro aggiungere/modificare le modalità soltanto se
necessario all'architettura definitiva.

============================================================
33. LIVELLI OPERATIVI
============================================================

LIVELLO 1:

DEMO / SIMULAZIONE

LIVELLO 2:

BACKTEST

LIVELLO 3:

PAPER TRADING

LIVELLO 4:

MT5 DEMO

LIVELLO 5:

LIVE

Il LIVE è l'ultimo livello.

============================================================
34. STATO ATTUALE
============================================================

CORE                         COMPLETATO BASE
MARKET DATA                  COMPLETATO BASE
YAHOO FINANCE                COMPLETATO BASE
INDICATORS                   COMPLETATO
MARKET ANALYSIS              COMPLETATO BASE
SMART MONEY                  COMPLETATO BASE
PHOENIX BRAIN                COMPLETATO BASE
SIGNAL MANAGER               COMPLETATO BASE
RISK MANAGER                 COMPLETATO BASE
TRADING GUARD                COMPLETATO V1
TRADE MANAGER                COMPLETATO BASE
EXECUTION                    COMPLETATO BASE
PERFORMANCE ANALYTICS        AVANZATO
REPORTING                    COMPLETATO BASE
MARKET SCANNER               COMPLETATO BASE
BACKTEST                     PRESENTE
POSITION MANAGEMENT          INCOMPLETO
EXIT MANAGEMENT              DA COMPLETARE
TRADE JOURNAL                DA COMPLETARE
PAPER TRADING                DA SVILUPPARE
HISTORICAL RESEARCH          DA SVILUPPARE
STRATEGY DISCOVERY           DA SVILUPPARE
SUPERVISOR                   DA SVILUPPARE
LEARNING ENGINE              DA SVILUPPARE
MACHINE LEARNING             FUTURO
MT5 DEMO                     DA VALIDARE
MT5 LIVE                     FUTURO

============================================================
35. PROSSIMO OBIETTIVO UFFICIALE
============================================================

NON passare subito al Machine Learning.

NON aggiungere moduli casuali.

NON modificare moduli già funzionanti senza necessità.

PROSSIMO OBIETTIVO:

COMPLETARE IL TRADE LIFECYCLE.

Ordine:

1. Position Manager
2. Position Monitor
3. Exit Manager
4. Break Even
5. Trailing Stop
6. Stop Loss
7. Take Profit
8. Chiusura posizione
9. Trade Journal
10. Integrazione Database
11. Test completo

Flusso da ottenere:

SIGNAL
  |
  v
RISK
  |
  v
GUARD
  |
  v
TRADE
  |
  v
EXECUTION
  |
  v
POSITION OPEN
  |
  v
POSITION MONITOR
  |
  v
EXIT LOGIC
  |
  v
POSITION CLOSED
  |
  v
DATABASE
  |
  v
PERFORMANCE

============================================================
36. ROADMAP DEFINITIVA
============================================================

FASE 1
Trade Lifecycle
Position + Exit + Journal

FASE 2
Paper Trading

FASE 3
Historical Market Research

FASE 4
Autonomous Market Scanner

FASE 5
Autonomous Decision Engine

FASE 6
Supervisor / Devil's Advocate

FASE 7
Strategy Discovery

FASE 8
MT5 DEMO

FASE 9
Learning Engine

FASE 10
Machine Learning / Optimization

FASE 11
MT5 LIVE

============================================================
37. REGOLE DI SVILUPPO
============================================================

Il proprietario del progetto non è un programmatore.

Le istruzioni devono quindi essere:

- passo passo;
- semplici;
- una modifica alla volta;
- indicare sempre quale file aprire;
- fornire il codice completo quando necessario;
- dire chiaramente cosa copiare;
- dire chiaramente dove incollare;
- far eseguire il test;
- controllare l'output;
- solo dopo procedere al passaggio successivo.

NON dare troppi comandi contemporaneamente.

NON saltare i test.

NON perdere i punti della roadmap.

NON creare duplicati.

NON cambiare architettura senza prima verificarne la necessità.

============================================================
38. PROCEDURA STANDARD PER OGNI MODIFICA
============================================================

1. Identificare l'obiettivo.
2. Identificare il file/modulo coinvolto.
3. Controllare se esiste già.
4. Modificare soltanto ciò che serve.
5. Testare.
6. Eseguire:

python run.py

7. Controllare eventuali errori.
8. Eseguire:

git status

9. Se tutto è corretto:

git add .

git commit -m "descrizione modifica"

git push origin main

10. Aggiornare questo Master State se cambia lo stato
    del progetto o il prossimo obiettivo.

============================================================
39. PRINCIPIO FONDAMENTALE
============================================================

NON RIPARTIRE DA ZERO.

NON PERDERE IL LAVORO PRECEDENTE.

NON RISCRIVERE MODULI GIÀ FUNZIONANTI SENZA MOTIVO.

Il progetto deve evolvere progressivamente.

Ogni nuova chat deve utilizzare questo documento come
riferimento principale.

============================================================
40. STATO DI RIFERIMENTO
============================================================

Cartella principale:

C:\ProjectPhoenixAI

Repository:

ProjectPhoenixAI

Branch:

main

Ultimo commit verificato:

6ae57df

Ultimo test verificato:

python run.py

Risultato:

Sistema avviato correttamente.

Trading Guard V1 inizializzato.

Prossimo obiettivo:

TRADE LIFECYCLE / POSITION MANAGEMENT

============================================================
FINE PHOENIX MASTER STATE
============================================================