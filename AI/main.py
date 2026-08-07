"""
========================================
PROJECT PHOENIX AI
Main
Versione 19.0
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
    print("5 - Performance Analytics")

    print()

    scelta = input("Seleziona modalità: ").strip()

    print()

    if scelta == "1":

        core.run_live()

    elif scelta == "2":

        simbolo = input(

            "Symbol (BTC-USD): "

        ).strip()

        if simbolo == "":

            simbolo = "BTC-USD"

        core.run_live_trading(

            simbolo

        )

    elif scelta == "3":

        simbolo = input("Symbol (BTC-USD): ").strip()

        if simbolo == "":
            simbolo = "BTC-USD"

        periodo = input(
            "Periodo storico - 1mo/3mo/6mo/1y/2y (3mo): "
        ).strip()

        if periodo == "":
            periodo = "3mo"

        core.run_backtest(symbol=simbolo, period=periodo)

    elif scelta == "4":

        Logger.section(

            "DATABASE"

        )

        trades = core.database.load_trades()

        if len(trades) == 0:

            print()

            print("Nessun trade presente.")

            print()

        else:

            for trade in trades:

                print(trade)

    elif scelta == "5":

        core.run_performance()

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