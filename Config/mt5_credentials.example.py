"""
========================================
PROJECT PHOENIX AI
Test connessione MT5
Versione 1.0

Script isolato per verificare che il collegamento a MetaTrader 5
funzioni PRIMA di usarlo nel ciclo di trading automatico.

Uso:
    python Tests/test_mt5_connection.py

Fase 1: si connette e mostra i dati del conto (nessun rischio).
Fase 2 (opzionale, richiede conferma esplicita): piazza UN piccolo
ordine di prova al volume minimo consentito dal simbolo, aspetta
3 secondi, poi lo richiude. Usalo SOLO su un conto DEMO.
========================================
"""

import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from Execution.mt5_broker import MT5Broker


def main():

    print("=" * 60)
    print(" TEST CONNESSIONE MT5")
    print("=" * 60)

    broker = MT5Broker()

    print("\n--- FASE 1: connessione ---\n")

    if not broker.connect():

        print(
            "\nConnessione fallita. Controlla Config/mt5_credentials.py "
            "(login, password, server) e che il terminale MT5 sia "
            "installato e raggiungibile."
        )

        return

    print(f"\nSaldo conto: {broker.get_balance()}")

    print(
        "\nSe questo e' un conto DEMO e i dati sopra sono corretti, "
        "puoi procedere con la Fase 2."
    )

    print(
        "\nATTENZIONE: la Fase 2 piazza un ordine VERO (anche se su "
        "conto demo, e' un'esecuzione reale sul server del broker)."
    )

    scelta = input(
        "\nVuoi procedere con un ordine di prova? (scrivi CONFERMO): "
    ).strip()

    if scelta != "CONFERMO":

        print("\nFase 2 saltata. Disconnessione.")

        broker.disconnect()

        return

    print("\n--- FASE 2: ordine di prova ---\n")

    simbolo = input(
        "Simbolo da testare, formato Yahoo Finance (es. EURUSD=X): "
    ).strip()

    if simbolo == "":

        simbolo = "EURUSD=X"

    mt5_symbol = broker._mt5_symbol(simbolo)

    import MetaTrader5 as mt5

    tick = mt5.symbol_info_tick(mt5_symbol)

    if tick is None:

        print(
            f"\nNessun prezzo disponibile per {mt5_symbol}. "
            "Controlla il nome del simbolo in Config/mt5_credentials.py "
            "(SYMBOL_MAP) confrontandolo con quello nel Market Watch "
            "del terminale MT5."
        )

        broker.disconnect()

        return

    prezzo = tick.ask

    trade = {
        "symbol": simbolo,
        "side": "BUY",
        "entry": prezzo,
        "stop_loss": prezzo * 0.99,
        "take_profit": prezzo * 1.01,
        "size": 1.0
    }

    print(f"\nApertura ordine di prova BUY su {mt5_symbol} @ {prezzo}...")

    order = broker.execute(trade)

    print("Risultato apertura:", order)

    if not order["success"]:

        print("\nOrdine non eseguito, vedi il motivo sopra.")

        broker.disconnect()

        return

    print("\nAttendo 3 secondi prima di richiudere...")

    time.sleep(3)

    closed_position = {
        "symbol": simbolo,
        "side": "BUY",
        "entry": order["entry"],
        "current_price": prezzo,
        "current_profit": 0.0,
        "close_reason": "TEST",
        "close_time": None,
        "mt5_symbol": mt5_symbol
    }

    report = broker.close(closed_position)

    print("Risultato chiusura:", report)

    broker.disconnect()

    print("\nTest completato.")


if __name__ == "__main__":

    main()