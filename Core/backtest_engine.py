"""
========================================
PROJECT PHOENIX AI
Backtest Engine
Versione 2.0
========================================
"""

from Logs.logger import Logger


class BacktestEngine:

    def __init__(self):

        Logger.success("Backtest Engine inizializzato.")

    def run(self, signals):

        Logger.section("BACKTEST ENGINE")

        total = len(signals)

        buy = signals.count("BUY")
        sell = signals.count("SELL")
        hold = signals.count("HOLD")

        executed = buy + sell

        if executed > 0:
            activity = round((executed / total) * 100, 2)
        else:
            activity = 0.0

        if buy > sell:
            market_bias = "LONG"

        elif sell > buy:
            market_bias = "SHORT"

        else:
            market_bias = "NEUTRO"

        results = {

            "total_trades": total,

            "executed_trades": executed,

            "buy": buy,

            "sell": sell,

            "hold": hold,

            "activity": activity,

            "market_bias": market_bias

        }

        Logger.success("Backtest completato.")

        return results