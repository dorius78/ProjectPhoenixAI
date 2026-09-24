# PROJECT PHOENIX AI â€” TEST REGISTRY

## TEST SUPERATI

| Test | Stato |
|---|---|
| E76 MT5 DEMO / DRY RUN | PASS |
| E76.2 Tick Freshness Guard | PASS |
| E76.5 Market Closed | PASS |
| E76.34 Autonomous MT5 Failover | PASS |
| E76.34.4 Opportunity Selection | PASS |
| E76.35 BTCUSD Guard Diagnostic | PASS |
| E76.36 MT5 validation | PASS |

## TEST DI SICUREZZA

| Test | Stato |
|---|---|
| DEMO blocks MT5 order | DA ESEGUIRE |
| DEMO blocks MT5 close | DA ESEGUIRE |
| Regression suite | DA ESEGUIRE |

## REGOLA

Un test precedente non viene considerato perso.
Ogni nuova modifica deve essere verificata contro i test giÃ  certificati.

## E76.44 - PAPER TRADING END-TO-END
- Tests.test_end_to_end: PASS
- Analysis Engine: PASS
- Risk Manager: PASS
- Trade Builder: PASS
- Execution Engine Paper Trading: PASS
- Position Controller: PASS
- Break Even: PASS
- Take Profit: PASS
- Close/PnL: PASS (+200.00)
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO

## E76.45 - Paper Trading Lifecycle
- Paper Engine: PASS
- Position Open: PASS
- Price Update: PASS
- Break Even: PASS
- Trailing Stop: PASS
- Take Profit: PASS
- Position Close: PASS
- PnL: PASS (+200.00)
- Balance: PASS (10200.00)
- Portfolio Removal: PASS
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO

## E76.46 - Paper Decision Bridge Integration
- Default Symbol: PASS (BTC-USD)
- MT5 Historical Data: PASS
- Analysis Engine: PASS
- Signal Manager: PASS
- Risk Gate: PASS
- Trade Builder: PASS
- Paper Position: PASS
- run_once(): PASS
- Status: TRADE_OPENED
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO

## E76.47 - Paper Position Lifecycle Integration
- Existing Position Guard: PASS
- Second Position Prevention: PASS
- Price Update: PASS
- Break Even: PASS
- Trailing Stop: PASS
- Take Profit: PASS
- Position Close: PASS
- PnL: PASS (+200.00)
- Balance: PASS (10200.00)
- Portfolio Removal: PASS
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO

## E76.48 - Paper Autonomous Candle Guard
- Candle State: PASS
- Duplicate Candle Detection: PASS
- First run: PASS (TRADE_OPENED)
- Second run same candle: PASS (WAIT)
- Reason: PASS (Candle already processed)
- MT5 historical data: PASS
- Paper Trading: PASS
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO

## E76.49 - Paper Autonomous Loop
- run_loop(): PASS
- Continuous Loop: PASS
- run_once Integration: PASS
- Default Symbol: PASS (BTC-USD)
- Interval: PASS (1h)
- Delay: PASS (30s default)
- KeyboardInterrupt: PASS
- Exception Handling: PASS
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO

## E76.50 - Paper Loop Position Management
- Paper Loop Audit: PASS
- Position Open: PASS
- Price Update: PASS
- Break Even: PASS
- Take Profit: PASS
- Position Close: PASS
- PnL: PASS (+200.00)
- Balance: PASS (10200.00)
- Equity: PASS (10200.00)
- Final Position: PASS (False)
- Risk/Reward: PASS (2.0)
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO

## E76.51 - Paper Multi-Candle Continuity
- Candle State: PASS
- Same Candle Block: PASS
- New Candle Allowed: PASS
- Multi-Candle Continuity: PASS
- Paper Engine: PASS
- Position Controller: PASS
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO

## E76.54 - Paper Auto Take Profit
- Position Open: PASS
- Take Profit: PASS
- Position Close: PASS
- PnL: PASS (+200.00)
- Balance: PASS (10200.00)
- Portfolio Removal: PASS
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO


## E76.55 - Paper Auto Stop Loss
- Position Open: PASS
- Stop Loss: PASS
- Position Close: PASS
- PnL: PASS (-100.00)
- Balance: PASS (9900.00)
- Portfolio Removal: PASS
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO

## E76.59 - Paper Loop Live Price Management
- MT5 current price source: PASS
- Paper update_price: PASS
- BUY STOP LOSS: PASS
- SELL TAKE PROFIT: PASS
- Position auto-close: PASS
- Balance update: PASS
- Equity update: PASS
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO


## E76.60 - Paper Market Price vs Decision Price
- Closed candle decision source: PASS
- Current MT5 price source: PASS
- Decision/position price separation: PASS
- Paper position management: PASS
- Bid/Ask midpoint: PASS
- SL/TP price management: PASS
- Break Even / Trailing compatibility: PASS
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO


## E76.62 - Paper Autonomous Position Cycle
- Position open: PASS
- MT5 current price: PASS
- Price -> Paper Position: PASS
- update_price(): PASS
- STOP LOSS auto-close: PASS
- Position removed: PASS
- Balance: PASS (9900.0)
- Equity: PASS (9900.0)
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO


## E76.63 - Paper Price Failure Safety
- Price unavailable simulation: PASS
- PRICE RESULT = None: PASS
- Position remains OPEN: PASS
- Balance unchanged: PASS (10000.0)
- Equity unchanged: PASS (10000.0)
- Safety handling: PASS
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO


## E76.65 - Paper Closed Position Re-Entry
- Initial position open: PASS
- Automatic close: PASS
- Position cleared: PASS
- Balance after first trade: PASS (10200.0)
- New position after close: PASS
- SELL re-entry: PASS
- Final position status: OPEN
- Final balance: PASS (10200.0)
- Final equity: PASS (10200.0)
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO


## E76.66 - Paper Close to Re-Entry Cycle
- First BUY position: PASS
- TAKE PROFIT: PASS
- Position closed: PASS
- Position removed: PASS
- Balance after close: PASS (10200.0)
- SELL re-entry: PASS
- Position after re-entry: PASS
- Final balance: PASS (10200.0)
- Final equity: PASS (10200.0)
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO


## E76.63 - Paper Price Failure Safety
- Price unavailable simulation: PASS
- PRICE RESULT = None: PASS
- Position remains OPEN: PASS
- Balance unchanged: PASS (10000.0)
- Equity unchanged: PASS (10000.0)
- Safety handling: PASS
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO


## E76.67 - Paper Break Even and Trailing Stop
- BUY Break Even: PASS
- BUY Break Even stop: PASS (100000.0)
- BUY Trailing Stop: PASS
- BUY Trailing stop after 102000: PASS (101000.0)
- Position status: PASS (OPEN)
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO


## E76.68 - Paper SELL Break Even and Trailing Stop
- SELL Break Even: PASS
- SELL Break Even stop: PASS
- SELL Trailing Stop: PASS
- SELL trailing stop: PASS (99000.0)
- Position status: PASS (OPEN)
- Equity: PASS (10200.0)
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO


## E76.69 - Paper Trailing Stop Exit
- BUY Break Even: PASS
- BUY Trailing Stop: PASS (101000.0)
- Price reversal: PASS (100900.0)
- STOP LOSS auto-close: PASS
- Close reason: PASS (STOP LOSS)
- Position removed: PASS
- Balance: PASS (10100.0)
- Equity: PASS (10100.0)
- MT5 order_send: NON UTILIZZATO
- LIVE: NON UTILIZZATO


## E76.70.7 - PAPER DATABASE RECORD VERIFICATION
- RESULT: PASS
- Database: phoenix_paper.db
- Database exists: YES
- Total trades: 1
- Symbol: BTC-USD
- Side: BUY
- Entry: 100000.0
- Exit: 102000.0
- Stop Loss: 99000.0
- Take Profit: 102000.0
- Size: 0.1
- PnL: +200.0
- Status: CLOSED
- Reason: TAKE PROFIT
- ORDER_SEND: NO
- MT5 ORDER: NO
- LIVE: NO


## E76.70.8 - PAPER DECISION BRIDGE DATABASE E2E

**RESULT:** PASS

**Database:** `phoenix_paper.db`  
**Bridge Database:** `DatabaseManager`  
**Engine Database:** `True`  
**Mode:** `PAPER`

**Test trade:**
- Symbol: BTC-USD
- Side: BUY
- Entry: 100000.0
- Exit: 102000.0
- Size: 0.1
- PnL: 200.0
- Status: CLOSED
- Reason: TAKE PROFIT

**Database persistence:** VERIFIED

**Safety:**
- ORDER_SEND: NO
- MT5 ORDER: NO
- LIVE: NO


## E76.71 - PAPER TRADING FULL E2E VALIDATION

**RESULT:** PASS

**Initial balance:** 10000.0
**Final balance:** 10200.0
**PnL:** +200.0
**Database:** `phoenix_paper.db`
**Database persistence:** VERIFIED
**Git database tracking:** EXCLUDED (`*.db`)

**Validated flow:**

OPEN -> MONITOR -> BREAK EVEN / TRAILING -> TAKE PROFIT -> CLOSE -> BALANCE -> DATABASE

**Trade:**
- Symbol: BTC-USD
- Side: BUY
- Entry: 100000.0
- Exit: 102000.0
- Size: 0.1
- PnL: 200.0
- Status: CLOSED
- Reason: TAKE PROFIT

**Safety:**
- ORDER_SEND: NO
- MT5 ORDER: NO
- LIVE: NO


## E76.72 - MT5 DEMO HARD SAFETY GATE VALIDATION

**RESULT:** PASS

**MODE:** DEMO

**Validated protections:**
- MT5 opening order blocked
- MT5 closing order blocked
- executed: False
- dry_run: True
- PHOENIX DEMO SAFETY GATE: ACTIVE
- ORDER_SEND: NOT EXECUTED
- LIVE: NO

**Opening test result:**
Ordine bloccato: MODE=DEMO

**Closing test result:**
Chiusura bloccata: MODE=DEMO

**Safety conclusion:**

In MODE=DEMO, Phoenix cannot open or close MT5 positions through the broker order_send() path.


## E76.73 - ACTIVE TEST SUITE STABILIZATION

**RESULT:** PASS

**Validated:**
- pytest.ini presente nella root del progetto.
- Directory Archive/ esclusa dalla raccolta pytest.
- Tests/test_analysis.py aggiornato alle firme correnti.
- Test Analysis: 3/3 PASS.
- Suite attiva completa: 91/91 PASS.
- 0 failed.
- Nessuna modifica al codice di produzione.
- PHOENIX DEMO SAFETY GATE: ACTIVE.
- ORDER_SEND: NO.
- MT5 ORDER: NO.
- LIVE: NO.

**Conclusion:**

La suite attiva di PROJECT PHOENIX AI Ã¨ completamente verde: 91/91 test PASS.
I test storici presenti in Archive/ rimangono preservati ma non vengono piÃ¹ raccolti dalla suite attiva.

## E76.74 - TRAILING STOP EXIT CLASSIFICATION FIX

**RESULT:** PASS

**Validated:**
- Corretto `Core/exit_manager.py` per la classificazione delle uscite Trailing Stop.
- Applicata la correzione sia BUY sia SELL.
- Preservata la logica di Break Even e Stop Loss.
- Test Exit Manager: 18/18 PASS.
- Test di regressione BUY Trailing Stop: PASS.
- Verifica SELL Trailing Stop: PASS.
- Suite attiva completa: 92/92 PASS.
- 0 failed.
- PHOENIX DEMO SAFETY GATE: ACTIVE.
- ORDER_SEND: NO.
- MT5 ORDER: NO.
- LIVE: NO.

**Conclusion:**

La classificazione delle uscite Trailing Stop è stata corretta e verificata su BUY e SELL.
La suite attiva di PROJECT PHOENIX AI è completamente verde: 92/92 test PASS.

## E76.75 - H4 TIMEFRAME CONSOLIDATION AND AUTONOMOUS MARKET SELECTION

**RESULT:** PASS

**Validated:**
- Timeframe operativo H4 consolidato nei flussi interessati.
- Selezione autonoma dello strumento di mercato verificata.
- Flusso multi-market verificato.
- ModalitÃ  DEMO e protezioni di sicurezza preservate.
- Nessun ordine LIVE eseguito.

## E76.76 - PHOENIXAI V3.21 MT5 NATIVE SOURCE

**RESULT:** PASS

**Validated:**
- Sorgente nativa MT5 `PhoenixAI_v3_21.mq5` aggiunta al progetto.
- Versione EA: 3.21.
- BUY/SELL, SL/TP, Break Even e Trailing Stop verificati.
- Risk management e margin gate verificati.
- Compilazione MetaEditor: 0 errori, 0 warning.
- Nessun ordine LIVE eseguito.

## E76.77 - MT5 ORDERCHECK VALIDATION FIX

**RESULT:** PASS

**Validated:**
- Corretta la verifica del risultato `OrderCheck()`.
- `check.retcode == 0` riconosciuto correttamente come esito positivo del controllo.
- EA PhoenixAI v3.21 ricompilato: 0 errori, 0 warning.
- Strategy Tester EURUSD H4, real ticks, 01/01/2026â€“10/09/2026: PASS.
- Aperture BUY/SELL verificate.
- SL/TP verificati.
- Break Even verificato.
- Trailing Stop verificato.
- Chiusure automatiche verificate.
- 215 operazioni di trading / 430 deal.
- Chiusura di fine test distinta dalle chiusure autonome dell'EA.
- Risultato economico negativo del test separato dalla validazione tecnica.
- Nessun ordine LIVE.
- MT5 Demo/Tester utilizzato.

**Conclusion:**

Il ciclo tecnico nativo MT5 `Signal -> Risk -> OrderCheck -> Order -> Position Management -> Exit` Ã¨ stato verificato con esito PASS.

## E76.78 - HIGHER TIMEFRAME ORDERING VALIDATION

**RESULT:** PASS

**Validated:**
- Controllo dell'ordine dei timeframe aggiunto nel native EA PhoenixAI v3.21.
- PeriodSeconds() utilizzato per verificare che il Higher Timeframe sia superiore al Main Timeframe.
- Configurazione H4 + H1 rifiutata correttamente.
- Configurazione H4 + D1 accettata correttamente.
- MetaEditor: 0 errori, 0 warning.
- Nessun ordine LIVE eseguito.

**Conclusion:**

Il controllo dell'ordine dei timeframe è stato validato correttamente.

## E76.79 - SET HIGHER TIMEFRAME TO D1

**RESULT:** PASS

**Validated:**
- Higher Timeframe predefinito del native EA PhoenixAI v3.21 modificato da H1 a D1.
- Main Timeframe: H4.
- Higher Timeframe: D1.
- Higher Timeframe Confirmation: ON.
- Higher TF Weight: 10.
- EA avviato correttamente su EURUSD H4.
- Conferma MTF H4 -> D1 verificata nel log MT5.
- Decision Engine operativo.
- HTF_BEARISH=YES e CONFIRMATION=YES osservati durante il test.
- Trading disattivato durante la validazione.
- Nessun ordine reale inviato.

**Conclusion:**

La configurazione PhoenixAI v3.21 H4 -> D1 è stata validata direttamente su MT5 con esito PASS.

