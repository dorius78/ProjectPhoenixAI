"""
========================================
PROJECT PHOENIX AI
Trading Guard
Versione 1.0

Protezione automatica per il Live Trading: ferma il ciclo se la
perdita giornaliera o le perdite consecutive superano una soglia
configurata in Config/settings.py. Non sostituisce la supervisione
umana, ma limita il danno se qualcosa va storto mentre non stai
guardando lo schermo.
========================================
"""

from datetime import date

from Config.settings import (
    MAX_DAILY_LOSS_PERCENT,
    MAX_CONSECUTIVE_LOSSES
)

from Logs.logger import Logger


class TradingGuard:

    def __init__(self, start_balance):

        self.day_start_balance = float(start_balance)

        self.current_day = date.today()

        self.daily_pnl = 0.0

        self.consecutive_losses = 0

        Logger.success("Trading Guard V1 inizializzato.")

    # =====================================
    # NUOVO GIORNO
    # =====================================

    def _check_new_day(self, current_balance):

        today = date.today()

        if today != self.current_day:

            self.current_day = today

            self.day_start_balance = current_balance

            self.daily_pnl = 0.0

            Logger.info(
                "Trading Guard: nuovo giorno, contatori azzerati."
            )

    # =====================================
    # REGISTRA UN TRADE CHIUSO
    # =====================================

    def register_trade(self, pnl, current_balance):

        self._check_new_day(current_balance)

        self.daily_pnl += float(pnl)

        if pnl < 0:

            self.consecutive_losses += 1

        else:

            self.consecutive_losses = 0

        Logger.info(
            f"Trading Guard: PnL giorno {self.daily_pnl:.2f} | "
            f"Perdite consecutive: {self.consecutive_losses}"
        )

    # =====================================
    # SI PUO' ANCORA OPERARE?
    # =====================================

    def can_trade(self, current_balance):

        self._check_new_day(current_balance)

        if self.day_start_balance > 0:

            daily_loss_percent = (
                -self.daily_pnl / self.day_start_balance * 100
            )

        else:

            daily_loss_percent = 0.0

        if daily_loss_percent >= MAX_DAILY_LOSS_PERCENT:

            return False, (
                f"Limite perdita giornaliera raggiunto "
                f"({daily_loss_percent:.2f}% >= "
                f"{MAX_DAILY_LOSS_PERCENT}%)"
            )

        if self.consecutive_losses >= MAX_CONSECUTIVE_LOSSES:

            return False, (
                f"Troppe perdite consecutive "
                f"({self.consecutive_losses} >= "
                f"{MAX_CONSECUTIVE_LOSSES})"
            )

        return True, None
