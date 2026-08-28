"""
========================================
PROJECT PHOENIX AI
Backtest Engine
Versione 12.0
========================================
"""

from Logs.logger import Logger


class BacktestEngine:

    def __init__(self):

        Logger.success("Backtest Engine V12 inizializzato.")

        self.history = []

        self.initial_capital = 10000.0

        self.closed_trades = 0

        # Posizione eventualmente ancora aperta
        # alla fine del dataset di backtest.
        # NON viene conteggiata nelle statistiche
        # dei trade chiusi.
        self.open_trade = None

        self.total_bars = 0

    # =====================================
    # AGGIUNGI TRADE
    # =====================================

    def add_trade(self, trade):

        if trade is None:

            return

        self.history.append(trade)

        self.closed_trades += 1

        Logger.info(

            f"Trade chiuso #{self.closed_trades}"

        )

    # =====================================
    # OPEN TRADE AT END
    # =====================================

    def set_open_trade(self, trade):

        if trade is None:
            self.open_trade = None
            return

        self.open_trade = trade.copy()

        Logger.info(
            "Backtest: posizione aperta "
            "rilevata alla fine del dataset."
        )

    # =====================================
    # ULTIMO TRADE
    # =====================================

    def last_trade(self):

        if not self.history:

            return None

        return self.history[-1]

    # =====================================
    # CANDELE TOTALI (per il calcolo di "activity")
    # =====================================

    def set_total_bars(self, total_bars):

        self.total_bars = int(total_bars)

    # =====================================
    # REPORT
    # =====================================

    def run(self):

        Logger.section("BACKTEST ENGINE")

        total = len(self.history)

        open_trades = (
            1
            if self.open_trade is not None
            else 0
        )

        buy = 0
        sell = 0

        wins = 0
        losses = 0

        gross_profit = 0.0
        gross_loss = 0.0

        capital = self.initial_capital

        peak = capital

        max_drawdown = 0.0

        for trade in self.history:

            side = str(

                trade.get("side", "HOLD")

            ).upper()

            pnl = float(

                trade.get("pnl", 0.0)

            )

            if "BUY" in side:

                buy += 1

            elif "SELL" in side:

                sell += 1

            capital += pnl

            if pnl > 0:

                wins += 1

                gross_profit += pnl

            elif pnl < 0:

                losses += 1

                gross_loss += abs(pnl)

            if capital > peak:

                peak = capital

            drawdown = peak - capital

            if drawdown > max_drawdown:

                max_drawdown = drawdown

        executed = wins + losses

        if executed > 0:

            win_rate = round(

                wins / executed * 100,

                2

            )

        else:

            win_rate = 0.0

        net_profit = gross_profit - gross_loss

        roi = round(

            net_profit /

            self.initial_capital * 100,

            2

        )

        if gross_loss > 0:

            profit_factor = round(

                gross_profit /

                gross_loss,

                2

            )

        else:

            profit_factor = 0.0

        # Prima "activity" era (buy+sell)/total*100: siccome ogni trade
        # e' sempre o BUY o SELL, questo era matematicamente sempre
        # uguale a 100, indipendentemente da quanto la strategia
        # tradasse davvero. Ora misura la vera frequenza: quante
        # candele su cento, delle candele effettivamente analizzate,
        # hanno prodotto un trade.
        if self.total_bars > 0:

            activity = round(
                total / self.total_bars * 100,
                2
            )

        else:

            activity = 0.0

        if buy > sell:

            market_bias = "LONG"

        elif sell > buy:

            market_bias = "SHORT"

        else:

            market_bias = "NEUTRAL"

        Logger.success(

            "Backtest completato."

        )

        return {

            "total_trades": total,

            "closed_trades": self.closed_trades,

            "open_trades": open_trades,

            "buy": buy,

            "sell": sell,

            "wins": wins,

            "losses": losses,

            "win_rate": win_rate,

            "gross_profit": round(

                gross_profit,

                2

            ),

            "gross_loss": round(

                gross_loss,

                2

            ),

            "net_profit": round(

                net_profit,

                2

            ),

            "capital": round(

                capital,

                2

            ),

            "roi": roi,

            "profit_factor": profit_factor,

            "max_drawdown": round(

                max_drawdown,

                2

            ),

            "activity": activity,

            "market_bias": market_bias

        }

    # =====================================
    # E71 HISTORICAL RESEARCH
    # =====================================

    def run_backtest(self, trades=None):
        """
        E71: esegue il calcolo storico utilizzando
        i trade forniti al BacktestEngine.

        Il motore non esegue ordini reali.
        """

        if trades is not None:
            self.history = list(trades)

        return self.run()

    # =====================================
    # RISULTATI E71
    # =====================================

    def get_results(self):
        """
        Restituisce i risultati dell'ultima analisi
        storica eseguita.
        """

        return self.run()

    # =====================================
    # E71 HISTORICAL RESEARCH
    # =====================================

    def run_backtest(self, trades=None):
        """
        E71: esegue il calcolo storico utilizzando
        i trade forniti al BacktestEngine.

        Il motore non esegue ordini reali.
        """

        if trades is not None:
            self.history = list(trades)

        return self.run()

    # =====================================
    # RISULTATI E71
    # =====================================

    def get_results(self):
        """
        Restituisce i risultati dell'ultima analisi
        storica eseguita.
        """

        return self.run()

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        self.history.clear()

        self.closed_trades = 0

        self.open_trade = None

        self.total_bars = 0

        Logger.info(

            "Backtest azzerato."

        )