# PROJECT PHOENIX AI - MT5 HANDOFF

Generato: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')

## CONTINUITÀ
- Progetto principale: C:\ProjectPhoenixAI
- Non ripartire da zero.
- Mantenere la roadmap ufficiale.
- Repository OneDrive NON usare per commit.
- MT5 DEMO fino a validazione completa.

## MT5
- EA: PhoenixAI_v3_21
- Versione: 3.21
- Broker: Pepperstone DEMO
- Simbolo principale: EURUSD
- Timeframe: H4
- Higher timeframe: D1
- MTF confirmation: ON
- Magic Number: 260813
- Maximum positions: 1
- Risk: 1%
- Risk/Reward: 2
- ATR multiplier: 1
- Margin cap: 50%
- Safety points: 5
- Score threshold: 60
- Confidence threshold: 55
- Break Even: ON
- Trailing Stop: ON
- Trading default: DISABLED

## VALIDAZIONI MT5
- E76.72: MT5 DEMO hard safety gate
- E76.73: test stabilization
- E76.76: PhoenixAI_v3_21
- E76.77: MT5 OrderCheck
- E76.78: higher timeframe ordering
- E76.79: higher timeframe D1
- Precedente ordine DEMO validato: EURUSD SELL
- OrderCheck: OK
- OrderSend retcode: 10009
- Magic: 260813
- LIVE non autorizzato.

## AI OPTIMIZATION
- E71.5: Phoenix Brain parameters centralizzati.
- E71.6: Strategy Discovery integration.
- StrategyDiscovery presente.
- apply_parameters() presente e testato.
- restore_parameters() presente e testato.
- Test StrategyDiscovery: 2 passed.
- CoreSystem.run_backtest() è il backtest reale esistente.
- NON creare un secondo BacktestEngine.
- Prima ottimizzazione: 5 soglie Phoenix.
- Ranking iniziale: net_profit.

## PROSSIMO PASSO
Integrare Strategy Discovery con il vero CoreSystem.run_backtest(), mantenendo il ripristino dei parametri e senza modificare il percorso MT5 DEMO.

## SICUREZZA
Prima di commit:
- test
- py_compile
- git diff --check
- git status

Commit/push solo da C:\ProjectPhoenixAI.
