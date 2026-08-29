# PROJECT PHOENIX AI — TEST REGISTRY

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
Ogni nuova modifica deve essere verificata contro i test già certificati.

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
