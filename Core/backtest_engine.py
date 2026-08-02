"""
========================================
PROJECT PHOENIX AI
Backtest Engine
Versione 8.0
========================================
"""

from Logs.logger import Logger


class BacktestEngine:

    def __init__(self):

        Logger.success("Backtest Engine V8 inizializzato.")

        self.history = []

        self.initial_capital = 10000.0

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

        buy = 0
        sell = 0

        wins = 0
        losses = 0

        profit = 0.0

        capital = self.initial_capital

        for trade in self.history:

            side = trade.get("side", "HOLD")

            if side == "BUY":
                buy += 1

            elif side == "SELL":
                sell += 1

            pnl = float(trade.get("pnl", 0))

            capital += pnl
            profit += pnl

            if pnl > 0:

                wins += 1

            elif pnl < 0:

                losses += 1

        activity = 0.0

        if total > 0:

            activity = round((buy + sell) / total * 100, 2)

        market_bias = "NEUTRAL"

        if buy > sell:

            market_bias = "LONG"

        elif sell > buy:

            market_bias = "SHORT"

        win_rate = 0.0

        executed = wins + losses

        if executed > 0:

            win_rate = round(wins / executed * 100, 2)

        results = {

            "total_trades": total,

            "buy": buy,

            "sell": sell,

            "wins": wins,

            "losses": losses,

            "win_rate": win_rate,

            "profit": round(profit, 2),

            "capital": round(capital, 2),

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