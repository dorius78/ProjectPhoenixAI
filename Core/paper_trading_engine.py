from Core.position_controller import PositionController
from Core.portfolio_manager import PortfolioManager


class PaperTradingEngine:

    def __init__(self):

        self.position_controller = PositionController()
        self.portfolio = PortfolioManager()

        self.mode = "PAPER"

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
