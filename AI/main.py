"""
========================================
PROJECT PHOENIX AI
Main
Versione 17.0
========================================
"""

from Core.core_system import CoreSystem
from Core.config import Config
from Logs.logger import Logger


def main():

    print("=" * 60)
    print(Config.APP_NAME)
    print(f"Versione {Config.VERSION}")
    print(f"Modalità: {Config.MODE}")
    print("=" * 60)

    Logger.info("Avvio di Project Phoenix AI")

    core = CoreSystem()

    print()

    print("1 - Scanner Multi Market")
    print("2 - Live Trading")
    print("3 - Backtest")
    print("4 - Database Trade")
    print("5 - Trade Journal")

    print()

    scelta = input("Seleziona modalità: ").strip()

    print()

    if scelta == "1":

        core.run_live()

    elif scelta == "2":

        simbolo = input(

            "Symbol (es. BTC-USD): "

        ).strip()

        if simbolo == "":

            simbolo = "BTC-USD"

        core.run_live_trading(

            simbolo

        )

    elif scelta == "3":

        core.run_backtest()

    elif scelta == "4":

        trades = core.database.load_trades()

        print()

        print("=" * 60)
        print("DATABASE TRADE")
        print("=" * 60)

        for trade in trades:

            print(trade)

        print()

    elif scelta == "5":

        print()

        print("=" * 60)
        print("TRADE JOURNAL")
        print("=" * 60)

        print(f"Trade Totali : {core.database.count()}")
        print(f"Trade Win    : {core.database.wins()}")
        print(f"Trade Loss   : {core.database.losses()}")
        print(f"Profitto Tot.: {core.database.total_profit()}")

        print()

        for trade in core.database.load_trades():

            print(trade)

    else:

        Logger.warning(

            "Modalità non valida."

        )

    Logger.info(

        "Core System avviato correttamente"

    )

    print("=" * 60)


if __name__ == "__main__":

    main()