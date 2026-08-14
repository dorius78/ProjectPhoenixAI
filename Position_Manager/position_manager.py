"""
========================================
PROJECT PHOENIX AI
Position Manager
Versione 1.0
========================================
"""

from MT5_Bridge.mt5_execution_recovered import (
    MT5ExecutionEngine
)


class PhoenixPositionManager:

    def __init__(
        self,
        symbol,
        magic=260813
    ):

        self.symbol = symbol
        self.magic = magic

        self.bridge = (
            MT5ExecutionEngine(
                symbol=self.symbol,
                magic=self.magic
            )
        )

    # =====================================
    # CONNECTION
    # =====================================

    def connect(self):

        return self.bridge.connect()

    def disconnect(self):

        self.bridge.disconnect()

    # =====================================
    # PHOENIX POSITIONS
    # =====================================

    def get_positions(self):

        return (
            self.bridge.get_phoenix_positions()
        )

    # =====================================
    # ACTIVE POSITION
    # =====================================

    def get_active_position(self):

        positions = (
            self.get_positions()
        )

        if not positions:

            return None

        return positions[0]

    # =====================================
    # POSITION STATUS
    # =====================================

    def get_position_status(self):

        position = (
            self.get_active_position()
        )

        if position is None:

            return {

                "active":
                    False,

                "symbol":
                    self.symbol,

                "message":
                    "Nessuna posizione Phoenix aperta",

            }

        return {

            "active":
                True,

            "ticket":
                int(position.ticket),

            "symbol":
                position.symbol,

            "type":
                int(position.type),

            "volume":
                float(position.volume),

            "entry":
                float(position.price_open),

            "current_price":
                float(position.price_current),

            "sl":
                float(position.sl),

            "tp":
                float(position.tp),

            "profit":
                float(position.profit),

            "swap":
                float(position.swap),

            "magic":
                int(position.magic),

            "comment":
                position.comment,

        }

    # =====================================
    # CLOSE POSITION
    # =====================================

    def close_position(
        self,
        dry_run=True
    ):

        position = (
            self.get_active_position()
        )

        if position is None:

            return {

                "executed":
                    False,

                "dry_run":
                    dry_run,

                "message":
                    "Nessuna posizione Phoenix da chiudere",

                "result":
                    None,

            }

        return (
            self.bridge.close_position(
                position,
                dry_run=dry_run
            )
        )
