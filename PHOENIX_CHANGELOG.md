# PROJECT PHOENIX AI — CHANGELOG

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
