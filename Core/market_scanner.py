"""
========================================
PROJECT PHOENIX AI
Market Scanner
Versione 2.0
========================================
"""

from Logs.logger import Logger

try:
    import MetaTrader5 as mt5
except ImportError:
    mt5 = None


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

    def _is_mt5_market_active(self, symbol):

        # =====================================
        # E76.34 - MT5 MARKET ACTIVITY GUARD
        # =====================================

        if mt5 is None:
            return False

        # =====================================
        # E76.34.3 - MT5 CONNECTION GUARD
        # =====================================

        try:

            terminal = mt5.terminal_info()

            if terminal is None or not getattr(
                terminal,
                "connected",
                False
            ):

                if not mt5.initialize():
                    Logger.warning(
                        "E76.34.3: MT5 non connesso."
                    )
                    return False

        except Exception as error:

            Logger.warning(
                f"E76.34.3: inizializzazione MT5 "
                f"fallita: {error}"
            )

            return False

        mt5_symbol = (
            str(symbol)
            .replace("=X", "")
            .replace("-", "")
            .replace("^", "")
        )

        try:

            info = mt5.symbol_info(mt5_symbol)

            if info is None:
                return False

            if getattr(
                info,
                "trade_mode",
                mt5.SYMBOL_TRADE_MODE_DISABLED
            ) == mt5.SYMBOL_TRADE_MODE_DISABLED:
                return False

            # =====================================
            # TICK RETRY
            # =====================================

            # Un tick puo' essere temporaneamente assente
            # anche quando il simbolo MT5 e' correttamente
            # disponibile e tradable.
            for _ in range(3):

                tick1 = mt5.symbol_info_tick(
                    mt5_symbol
                )

                if (
                    tick1 is not None
                    and tick1.bid > 0
                    and tick1.ask > 0
                ):

                    return True

                time.sleep(0.2)

            return False

        except Exception as error:

            Logger.warning(
                f"MT5 market check fallito "
                f"per {symbol}: {error}"
            )

            return False

    # =====================================
    # MIGLIORE OPPORTUNITA'
    # =====================================

    def get_best_opportunity(self):

        if not self.results:
            return None

        self.sort()

        for result in self.results:

            decision = str(
                result.get("decision", "")
            ).upper()

            if decision not in (
                "BUY",
                "STRONG BUY",
                "SELL",
                "STRONG SELL"
            ):
                continue

            symbol = result.get(
                "symbol",
                ""
            )

            if not self._is_mt5_market_active(
                symbol
            ):
                Logger.info(
                    f"E76.34: {symbol} "
                    "scartato: mercato MT5 "
                    "non attivo."
                )
                continue

            Logger.success(
                f"E76.34: opportunita' selezionata "
                f"{symbol}."
            )

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
