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

