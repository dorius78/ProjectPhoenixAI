"""
========================================
PROJECT PHOENIX AI
Main
Versione 16.0
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

    # =====================================
    # MODALITA'
    # =====================================

    print()

    print("1 - Scanner Multi Market")

    print("2 - Live Trading")

    print("3 - Backtest")

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