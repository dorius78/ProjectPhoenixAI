# PROJECT PHOENIX AI â€” CHANGELOG

## 2026-08-29

### Safety Gate E76.34.x

**Problema rilevato**

Durante il test autonomo DEMO il percorso Live Trading ha raggiunto MT5
con `dry_run=False`, causando un ordine reale BTCUSD SELL 0.45.

**Correzione**

- `ExecutionEngine`: MODE=DEMO forza `mt5_dry_run=True`.
- `MT5Broker.execute()`: MODE=DEMO blocca qualsiasi apertura MT5.
- `MT5Broker.close()`: MODE=DEMO blocca qualsiasi chiusura MT5.
- Creati backup pre-modifica.
- Aggiunto sistema di test di sicurezza.

**Regola permanente**

`MODE=DEMO` deve sempre impedire qualsiasi `mt5.order_send()`.


## E76.41 - Position Sizing Mathematical Audit
- Confermata formula corretta basata su MT5 tick_size e tick_value.
- Rischio target: account_balance * MAX_RISK / 100.
- Il Core RiskPositionSize attuale usa solo stop_distance e non conosce le specifiche dello strumento.
- MT5 Broker possiede gia' le specifiche necessarie: tick_size, tick_value, contract_size, volume_min, volume_max, volume_step.
- Decisione: mantenere il Core broker-agnostic e implementare il calcolo volume reale nel layer MT5.
- Test E76.41 completato senza order_send, senza ordini e senza modifiche MT5.


## E76.41 - Position Sizing CLOSED
- Audit completato.
- Nessuna modifica al sizing applicata.
- Confermato che RiskPositionSize produce UNITS, non lotti MT5.
- Confermato che MT5Broker._to_volume() converte correttamente UNITS -> LOTS tramite trade_contract_size.
- GBPUSD 76213.55 units = 0.76 MT5 lots.
- EURUSD 100000 units = 1.00 MT5 lot.
- BTCUSD 0.10 units = 0.10 MT5 lots.
- Nessun order_send durante i test.
- E76.41 CHIUSO: nessuna correzione necessaria.


## E76.44 - Paper Trading End-to-End VERIFIED
- Test Tests.test_end_to_end superato.
- Pipeline verificata: Analysis -> Signal -> Risk -> Trade Builder -> Execution -> Paper Trading -> Position Controller -> Break Even -> Take Profit -> Close.
- PnL test verificato: +200.00.
- Nessun order_send.
- Nessun ordine MT5.
- Nessun LIVE.
- Nessuna modifica ai moduli necessaria.


## E76.45 - Paper Trading Lifecycle VERIFIED
- PaperTradingEngine inizializzato correttamente.
- Balance iniziale: 10000.00.
- Apertura BUY BTC-USD: entry 100000.00, size 0.10.
- Break Even attivato.
- Trailing Stop aggiornato a 100500.00.
- Take Profit raggiunto a 102000.00.
- Posizione chiusa correttamente.
- PnL finale: +200.00.
- Balance finale: 10200.00.
- Posizione rimossa dal Portfolio.
- Nessun order_send.
- Nessun ordine MT5.
- Nessun LIVE.
- E76.45 PAPER TRADING LIFECYCLE SUPERATO.

## E76.46 - Paper Decision Bridge Symbol Fix
- Individuato errore: run_once() utilizzava symbol=None come default.
- Correzione applicata: PaperDecisionBridge usa Config.settings.SYMBOL come default.
- SYMBOL configurato: BTC-USD.
- py_compile superato.
- Paper Decision Bridge run_once() verificato con dati reali BTC-USD.
- Analysis Engine: PASS.
- Signal Manager: PASS.
- Risk Gate: PASS.
- Trade Builder: PASS.
- Paper Position: PASS.
- Status: TRADE_OPENED.
- Nessun order_send.
- Nessun ordine MT5.
- Nessun LIVE.
- E76.46 SUPERATO.

## E76.47 - Paper Position Lifecycle Integration
- Verificata gestione posizione Paper già esistente.
- Posizione BUY BTC-USD aperta correttamente.
- Nuovo run_once() con posizione già presente: nessuna seconda posizione aperta.
- Price Update: PASS.
- Break Even: PASS.
- Trailing Stop: PASS.
- Take Profit: PASS.
- Position Close: PASS.
- PnL finale: +200.00.
- Balance finale: 10200.00.
- Posizione rimossa correttamente dal Portfolio.
- Nessun order_send.
- Nessun ordine MT5.
- Nessun LIVE.
- Git verificato pulito.
- E76.47 SUPERATO.

## E76.48 - Paper Autonomous Candle Guard
- Aggiunto last_processed_candle al PaperDecisionBridge.
- Implementato Candle Duplicate Guard.
- La stessa candela chiusa non viene rielaborata.
- Prima run reale BTC-USD: TRADE_OPENED.
- Seconda run sulla stessa candela: WAIT.
- Reason: Candle already processed.
- MT5 historical data: PASS.
- Paper Trading: PASS.
- Nessun order_send.
- Nessun ordine MT5.
- Nessun LIVE.
- E76.48 SUPERATO.

## E76.49 - Paper Autonomous Loop
- Implementato run_loop() nel PaperDecisionBridge.
- Loop continuo PAPER con run_once().
- Configurazione predefinita: BTC-USD / 1h / delay 30 secondi.
- Candle Duplicate Guard mantenuto.
- Gestione KeyboardInterrupt verificata.
- Gestione eccezioni verificata.
- Test E76.49.8: PASS.
- Nessun order_send.
- Nessun ordine MT5.
- Nessun LIVE.
- E76.49 SUPERATO.

## E76.50 - Paper Loop Position Management
- Audit Paper Loop: PASS.
- Paper Position Lifecycle: PASS.
- Position Open: PASS.
- Price Update: PASS.
- Break Even: PASS.
- Take Profit: PASS.
- Position Close: PASS.
- PnL finale: +200.00.
- Balance finale: 10200.00.
- Equity finale: 10200.00.
- Position state finale: False.
- Risk/Reward: 2.0.
- Nessun order_send.
- Nessun ordine MT5.
- Nessun LIVE.
- E76.50 SUPERATO.

## E76.51 - Paper Multi-Candle Continuity
- Verificato Candle Duplicate Guard.
- Stessa candela: correttamente bloccata.
- Nuova candela: correttamente consentita.
- Multi-Candle Continuity: PASS.
- Paper Engine: PASS.
- Position Controller: PASS.
- Nessun order_send.
- Nessun ordine MT5.
- Nessun LIVE.
- E76.51 SUPERATO.

## E76.54 - Paper Auto Take Profit
- Auto Take Profit: PASS.
- BUY BTC-USD 100000 -> 102000.
- PnL: +200.00.
- Balance finale: 10200.00.
- Position Close: PASS.
- Portfolio Removal: PASS.
- Nessun order_send.
- Nessun ordine MT5.
- Nessun LIVE.
- E76.54 SUPERATO.


## E76.55 - Paper Auto Stop Loss
- Auto Stop Loss: PASS.
- BUY BTC-USD 100000 -> 99000.
- PnL: -100.00.
- Balance finale: 9900.00.
- Position Close: PASS.
- Portfolio Removal: PASS.
- Nessun order_send.
- Nessun ordine MT5.
- Nessun LIVE.
- E76.55 SUPERATO.

## E76.59 - Paper Loop Live Price Management
- Paper Loop collegato al prezzo corrente MT5 tramite MT5Provider.get_price().
- update_price() collegato alla gestione della posizione PAPER.
- Prezzo corrente Bid/Ask midpoint utilizzato dal provider.
- E76.59.8: prezzo MT5 -> Paper Position: PASS.
- E76.59.8: STOP LOSS automatico: PASS.
- E76.59.9: TAKE PROFIT automatico: PASS.
- Paper balance/equity aggiornati correttamente.
- MT5 order_send: NON UTILIZZATO.
- LIVE: NON UTILIZZATO.


## E76.60 - Paper Market Price vs Decision Price
- Decision engine mantiene la valutazione sulla candela chiusa.
- Paper Loop utilizza MT5Provider.get_price() per il prezzo corrente.
- Gestione posizione PAPER separata dalla decisione di mercato.
- Prezzo corrente MT5 ottenuto tramite Bid/Ask midpoint.
- SL/TP/Break Even/Trailing ricevono il prezzo corrente.
- E76.60 audit: PASS.
- MT5 order_send: NON UTILIZZATO.
- LIVE: NON UTILIZZATO.

