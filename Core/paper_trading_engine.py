from Core.position_controller import PositionController
from Core.portfolio_manager import PortfolioManager
from Database.database_manager import DatabaseManager
from datetime import datetime


class PaperTradingEngine:

    def __init__(self):

        self.position_controller = PositionController()
        self.portfolio = PortfolioManager()

        self.mode = "PAPER"

        # Database opzionale:
        # Paper Trading continua a funzionare
        # anche senza database esplicito.
        self.database = None

    # =====================================
    # APERTURA PAPER POSITION
    # =====================================

    def open_trade(
        self,
        side,
        entry,
        stop_loss,
        take_profit,
        symbol,
        size
    ):

        if self.mode != "PAPER":
            raise RuntimeError(
                "PaperTradingEngine non è in modalità PAPER."
            )

        if self.position_controller.has_position():
            return None

        opened = self.position_controller.open_position(
            side=side,
            entry=entry,
            stop_loss=stop_loss,
            take_profit=take_profit,
            symbol=symbol,
            size=size
        )

        if not opened:
            return None

        position = self.position_controller.get_position()

        self.portfolio.add(
            symbol,
            position
        )

        return position

    # =====================================
    # AGGIORNAMENTO PREZZO
    # =====================================

    def update_price(
        self,
        current_price
    ):

        position = self.position_controller.update(
            current_price=current_price
        )

        if position is None:
            return None

        if position.get("status") == "CLOSED":

            symbol = position.get("symbol")

            pnl = float(
                position.get(
                    "current_profit",
                    0
                )
            )

            self.portfolio.update_balance(
                pnl
            )

            self.portfolio.remove(
                symbol
            )

            # =====================================
            # PAPER TRADE DATABASE
            # =====================================

            if self.database is not None:

                trade_record = dict(
                    position
                )

                trade_record["symbol"] = symbol

                trade_record["pnl"] = pnl

                trade_record["profit"] = pnl

                trade_record["result"] = pnl

                entry_price = float(
                    trade_record.get(
                        "entry",
                        0.0
                    )
                )

                exit_price = float(
                    trade_record.get(
                        "current_price",
                        entry_price
                    )
                )

                stop_price = float(
                    trade_record.get(
                        "initial_stop_loss",
                        trade_record.get(
                            "stop_loss",
                            entry_price
                        )
                    )
                )

                risk = abs(
                    entry_price - stop_price
                )

                reward = abs(
                    exit_price - entry_price
                )

                if risk > 0:

                    trade_record["risk_reward"] = round(
                        reward / risk,
                        6
                    )

                else:

                    trade_record["risk_reward"] = 0.0

                trade_record["status"] = "CLOSED"

                trade_record["exit"] = position.get(
                    "current_price"
                )

                trade_record["close_time"] = datetime.now()

                trade_record["reason"] = (
                    position.get(
                        "close_reason",
                        "PAPER"
                    )
                    or "PAPER"
                )

                open_time = position.get(
                    "open_time"
                )

                close_time = trade_record.get(
                    "close_time"
                )

                if (
                    open_time is not None
                    and close_time is not None
                ):

                    trade_record["duration"] = (
                        close_time - open_time
                    ).total_seconds()

                else:

                    trade_record["duration"] = 0.0

                self.database.save_trade(
                    trade_record
                )

        else:

            symbol = position.get("symbol")

            self.portfolio.update(
                symbol,
                position
            )

        return position

    # =====================================
    # STATO
    # =====================================

    def get_position(self):

        return self.position_controller.get_position()

    def get_balance(self):

        return self.portfolio.get_balance()

    def get_equity(self):

        return self.portfolio.get_equity()

    def has_position(self):

        return self.position_controller.has_position()

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        self.position_controller.reset()
        self.portfolio.reset()
