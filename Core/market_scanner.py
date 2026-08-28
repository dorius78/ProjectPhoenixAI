"""
========================================
PROJECT PHOENIX AI
Market Scanner
Versione 2.0
========================================
"""

from Logs.logger import Logger


class MarketScanner:

    def __init__(self):

        Logger.success("Market Scanner V2 inizializzato.")

        self.symbols = []

        self.results = []

    # =====================================
    # WATCHLIST
    # =====================================

    def load_default(self):

        self.symbols = [

            "BTC-USD",

            "ETH-USD",

            "SOL-USD",

            "BNB-USD",

            "EURUSD=X",

            "GBPUSD=X",

            "USDJPY=X",

            "GC=F",

            "SI=F",

            "CL=F",

            "^GSPC",

            "^IXIC"

        ]

        Logger.success(

            f"Watchlist caricata ({len(self.symbols)} strumenti)."

        )

    # =====================================
    # LISTA
    # =====================================

    def get_symbols(self):

        return self.symbols

    # =====================================
    # AGGIUNGI RISULTATO
    # =====================================

    def add_result(

        self,

        symbol,

        decision,

        score,

        confidence

    ):

        self.results.append({

            "symbol": symbol,

            "decision": decision,

            "score": score,

            "confidence": confidence

        })

    # =====================================
    # ORDINA
    # =====================================

    def sort(self):

        self.results.sort(

            key=lambda x: x["score"],

            reverse=True

        )

    # =====================================
    # MIGLIORE OPPORTUNITÀ
    # =====================================

    def get_best_opportunity(self):

        if not self.results:
            return None

        self.sort()

        for result in self.results:

            decision = str(
                result.get("decision", "")
            ).upper()

            if decision in (
                "BUY",
                "STRONG BUY",
                "SELL",
                "STRONG SELL"
            ):

                return result

        return None

    # =====================================
    # REPORT
    # =====================================

    def report(self):

        Logger.section(

            "MARKET SCANNER"

        )

        self.sort()

        for result in self.results:

            Logger.info(

                f"{result['symbol']:10}"

                f" {result['decision']:12}"

                f" Score:{result['score']:3}"

                f" Conf:{result['confidence']:3}"

            )

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        self.results.clear()
