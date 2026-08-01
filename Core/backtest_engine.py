"""
========================================
PROJECT PHOENIX AI
Backtest Engine
Versione 7.0
========================================
"""

from Logs.logger import Logger


class BacktestEngine:

    def __init__(self):

        Logger.success("Backtest Engine V7 inizializzato.")

        self.history = []

    # =====================================
    # REGISTRA TRADE
    # =====================================

    def add_trade(self, trade):

        if trade is None:
            return

        self.history.append(trade)

    # =====================================
    # BACKTEST
    # =====================================

    def run(self):

        Logger.section("BACKTEST ENGINE")

        total = len(self.history)

        buy = sum(
            1 for t in self.history
            if t["side"] == "BUY"
        )

        sell = sum(
            1 for t in self.history
            if t["side"] == "SELL"
        )

        activity = 0.0

        if total > 0:
            activity = 100.0

        market_bias = "NEUTRAL"

        if buy > sell:
            market_bias = "LONG"

        elif sell > buy:
            market_bias = "SHORT"

        results = {

            "total_trades": total,

            "buy": buy,

            "sell": sell,

            "activity": activity,

            "market_bias": market_bias

        }

        Logger.success("Backtest completato.")

        return results

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        self.history.clear()

        Logger.info("Storico Backtest azzerato.")