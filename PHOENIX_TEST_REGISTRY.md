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

