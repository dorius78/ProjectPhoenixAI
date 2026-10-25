# PROJECT PHOENIX AI — Piano di completamento della roadmap

Data revisione: 13/10/2026
Riferimento: roadmap storica in `Docs/Docs/Docs/03_ROADMAP.md`.

Questo documento aggiunge un piano operativo alla roadmap storica, senza sostituirla. Lo stato viene basato sui moduli presenti, sui checkpoint documentati e sulla suite completa eseguita nell'ultimo checkpoint disponibile (147 test superati). Il superamento dei test verifica il comportamento coperto dai test; non certifica redditività né prontezza per il trading reale.

## Stato sintetico

- Nucleo Alpha — implementato e ampiamente verificato.
- Smart Money, gestione del rischio e ciclo della posizione — implementati con copertura di test; da mantenere nel gate di regressione.
- Backtest, statistiche, portfolio e paper trading — implementati; la validazione delle prestazioni resta aperta.
- Ricerca storica, Strategy Discovery e apprendimento con approvazione — presenti; non equivalgono a ML/ottimizzazione autonoma pronta all'uso.
- MT5 — percorso DEMO e ciclo tecnico documentati; nessun passaggio LIVE è autorizzato da questo piano.
- Dashboard professionale — da realizzare o da dimostrare con un prodotto esistente.
- Multi-broker e multi-asset — requisiti da verificare e completare; la presenza di più provider dati non dimostra il supporto di più broker di esecuzione.
- Documentazione — disallineata: alcuni documenti indicano ancora Alpha o 2.0 Stable, mentre gli aggiornamenti più recenti descrivono checkpoint E76 e funzionalità successive.

## Fasi residue e criteri di chiusura

### 0. Allineare lo stato del progetto

- Stabilire un solo documento come registro dello stato corrente e linkare da esso la roadmap storica e gli audit archiviati.
- Registrare checkpoint, branch, test eseguiti, ambiente DEMO e modifiche locali non consolidate.
- Correggere le etichette obsolete dopo aver verificato che non cancellino decisioni o cronologia utili.

**Chiusura:** una persona che apre il progetto può determinare da un solo punto cosa è completato, cosa è in corso e quale sia il prossimo checkpoint.

### 1. Fissare il perimetro della versione 1.0

- Scrivere i requisiti minimi di dashboard, asset supportati, broker di esecuzione, modalità operative e report.
- Separare le funzioni obbligatorie per 1.0 da quelle successive.
- Definire esplicitamente quali funzioni sono solo DEMO e quali, eventualmente, potranno essere considerate per LIVE dopo approvazione separata.

**Chiusura:** ogni punto della roadmap ha un criterio verificabile e una modalità di prova definita.

### 2. Validare la qualità delle strategie e il ciclo DEMO

- Distinguere correttezza tecnica da qualità economica dei risultati.
- Definire prima dei test i periodi in-sample/out-of-sample, i costi e slippage, i limiti di drawdown e il numero minimo di operazioni.
- Eseguire validazioni walk-forward e forward DEMO ripetibili; conservare report e configurazioni.
- Bloccare la promozione di strategie che non superano le soglie approvate.

**Chiusura:** risultati riproducibili e documentati superano criteri concordati senza allentare i gate di rischio.

### 3. Completare l'esperienza e l'integrazione della piattaforma

- Realizzare la dashboard minima definita nella fase 1, inclusi stato del sistema, posizioni, rischio e report.
- Verificare ogni asset end-to-end: dati, simboli, precisione, dimensionamento, backtest, paper e DEMO.
- Verificare ogni broker di esecuzione end-to-end attraverso un contratto comune e test isolati; non contare un provider dati come broker.
- Definire installazione, configurazione, gestione errori e recupero dopo riavvio.

**Chiusura:** le funzioni dichiarate sono raggiungibili dall'utente e validate sul percorso completo senza dipendenze manuali non documentate.

### 4. Concludere learning e ottimizzazione controllata

- Mantenere la sequenza ricerca → validazione → approvazione → apprendimento.
- Separare i dati di selezione da quelli di valutazione e impedire leakage temporale.
- Confrontare ogni strategia o configurazione con una baseline e mantenere rollback.
- Dichiarare ML/AI Optimization completato solo dopo validazione fuori campione e approvazione esplicita.

**Chiusura:** nessun apprendimento o aggiornamento dei parametri cambia il percorso operativo senza superare i gate stabiliti.

### 5. Rilascio 1.0 e mantenimento

- Eseguire suite di regressione, test end-to-end e controlli di sicurezza in ambiente isolato.
- Verificare credenziali, permessi, log, database, backup/ripristino e arresto sicuro.
- Pubblicare guida d'installazione, limiti noti, configurazioni supportate e procedura di rollback.
- Produrre un verbale finale firmato con versione, risultati, limiti e modalità operative abilitate.

**Chiusura:** tutti i criteri obbligatori 1.0 sono PASS, le limitazioni sono dichiarate e il rilascio non abilita LIVE automaticamente.

## Ordine di lavoro

1. Allineare lo stato e fissare i requisiti di 1.0.
2. Validare prestazioni e sicurezza in backtest/paper/DEMO.
3. Completare dashboard, asset e broker secondo il perimetro approvato.
4. Validare learning/ottimizzazione fuori campione.
5. Eseguire il gate finale di rilascio.

La roadmap non attribuisce una percentuale numerica di completamento: la stima dipende dal perimetro che verrà scelto per dashboard, numero di asset/broker e durata minima della validazione forward.
