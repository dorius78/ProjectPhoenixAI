"""
========================================
PROJECT PHOENIX AI
Portfolio Manager
Versione 2.0
========================================
"""

from Logs.logger import Logger


class PortfolioManager:

    def __init__(self):

        Logger.success("Portfolio Manager V2 inizializzato.")

        self.positions = {}

    # =====================================
    # AGGIUNGI POSIZIONE
    # =====================================

    def add(self, symbol, position):

        self.positions[symbol] = position

        Logger.info(

            f"Portfolio -> aggiunta {symbol}"

        )

    # =====================================
    # RIMUOVI POSIZIONE
    # =====================================

    def remove(self, symbol):

        if symbol in self.positions:

            del self.positions[symbol]

            Logger.info(

                f"Portfolio -> rimossa {symbol}"

            )

    # =====================================
    # AGGIORNA POSIZIONE
    # =====================================

    def update(self, symbol, position):

        if symbol in self.positions:

            self.positions[symbol] = position

    # =====================================
    # POSIZIONE
    # =====================================

    def get(self, symbol):

        return self.positions.get(symbol)

    # =====================================
    # TUTTE
    # =====================================

    def get_all(self):

        return self.positions

    # =====================================
    # ESISTE
    # =====================================

    def has_position(self, symbol):

        return symbol in self.positions

    # =====================================
    # NUMERO POSIZIONI
    # =====================================

    def count(self):

        return len(self.positions)

    # =====================================
    # LISTA SIMBOLI
    # =====================================

    def symbols(self):

        return list(self.positions.keys())

    # =====================================
    # PROFITTO TOTALE
    # =====================================

    def total_profit(self):

        total = 0.0

        for position in self.positions.values():

            total += position.get(

                "current_profit",

                0.0

            )

        return round(total, 2)

    # =====================================
    # ESPOSIZIONE
    # =====================================

    def exposure(self):

        buy = 0

        sell = 0

        for position in self.positions.values():

            side = position.get("side")

            if side in ("BUY", "STRONG BUY"):

                buy += 1

            elif side in ("SELL", "STRONG SELL"):

                sell += 1

        return {

            "buy": buy,

            "sell": sell,

            "total": buy + sell

        }

    # =====================================
    # REPORT
    # =====================================

    def report(self):

        Logger.section("PORTFOLIO")

        Logger.info(

            f"Posizioni : {self.count()}"

        )

        Logger.info(

            f"Profitto  : {self.total_profit()}"

        )

        expo = self.exposure()

        Logger.info(

            f"BUY : {expo['buy']}"

        )

        Logger.info(

            f"SELL: {expo['sell']}"

        )

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        self.positions.clear()

        Logger.info(

            "Portfolio azzerato."

        )