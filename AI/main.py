import os
import sys



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
    core.start()

    Logger.info("Core System avviato correttamente")

    print("=" * 60)


if __name__ == "__main__":
    main()