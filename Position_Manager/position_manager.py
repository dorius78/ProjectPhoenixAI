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
    # POSITION MONITORING
    # =====================================

    def monitor_position(self):

        position = (
            self.get_active_position()
        )

        if position is None:

            return {

                "active":
                    False,

                "symbol":
                    self.symbol,

                "status":
                    "NO_POSITION",

                "message":
                    "Nessuna posizione Phoenix attiva",

            }

        profit = float(
            getattr(
                position,
                "profit",
                0.0
            )
        )

        entry = float(
            getattr(
                position,
                "price_open",
                0.0
            )
        )

        current_price = float(
            getattr(
                position,
                "price_current",
                0.0
            )
        )

        sl = float(
            getattr(
                position,
                "sl",
                0.0
            )
        )

        tp = float(
            getattr(
                position,
                "tp",
                0.0
            )
        )

        position_type = int(
            getattr(
                position,
                "type",
                -1
            )
        )

        # ---------------------------------
        # PROFIT / LOSS STATUS
        # ---------------------------------

        if profit > 0:

            profit_status = "PROFIT"

        elif profit < 0:

            profit_status = "LOSS"

        else:

            profit_status = "BREAKEVEN"

        # ---------------------------------
        # PRICE STATUS
        # ---------------------------------

        if position_type == 0:

            direction = "BUY"

        elif position_type == 1:

            direction = "SELL"

        else:

            direction = "UNKNOWN"

        # ---------------------------------
        # DISTANCE FROM SL / TP
        # ---------------------------------

        distance_sl = None
        distance_tp = None

        if sl > 0:

            distance_sl = abs(
                current_price - sl
            )

        if tp > 0:

            distance_tp = abs(
                tp - current_price
            )

        return {

            "active":
                True,

            "ticket":
                int(position.ticket),

            "symbol":
                position.symbol,

            "direction":
                direction,

            "volume":
                float(position.volume),

            "entry":
                entry,

            "current_price":
                current_price,

            "sl":
                sl,

            "tp":
                tp,

            "profit":
                profit,

            "swap":
                float(
                    getattr(
                        position,
                        "swap",
                        0.0
                    )
                ),

            "profit_status":
                profit_status,

            "distance_sl":
                distance_sl,

            "distance_tp":
                distance_tp,

            "magic":
                int(position.magic),

            "comment":
                position.comment,

        }

    # =====================================
    # SL / TP STATUS
    # =====================================

    def get_sl_tp_status(self):

        position = (
            self.get_active_position()
        )

        if position is None:

            return {

                "active":
                    False,

                "symbol":
                    self.symbol,

                "status":
                    "NO_POSITION",

                "sl_present":
                    False,

                "tp_present":
                    False,

                "message":
                    "Nessuna posizione Phoenix attiva",

            }

        sl = float(
            getattr(
                position,
                "sl",
                0.0
            )
        )

        tp = float(
            getattr(
                position,
                "tp",
                0.0
            )
        )

        return {

            "active":
                True,

            "ticket":
                int(position.ticket),

            "symbol":
                position.symbol,

            "direction":
                (
                    "BUY"
                    if int(position.type) == 0
                    else "SELL"
                    if int(position.type) == 1
                    else "UNKNOWN"
                ),

            "sl":
                sl,

            "tp":
                tp,

            "sl_present":
                sl > 0,

            "tp_present":
                tp > 0,

            "sl_tp_protected":
                sl > 0 and tp > 0,

            "status":
                (
                    "PROTECTED"
                    if sl > 0 and tp > 0
                    else "PARTIAL_PROTECTION"
                    if sl > 0 or tp > 0
                    else "UNPROTECTED"
                ),

        }

    # =====================================
    # POSITION PROTECTION CHECK
    # =====================================

    def check_position_protection(self):

        status = (
            self.get_sl_tp_status()
        )

        if not status["active"]:

            return {

                "active":
                    False,

                "protected":
                    False,

                "status":
                    "NO_POSITION",

                "message":
                    "Nessuna posizione Phoenix da proteggere",

            }

        sl_present = bool(
            status["sl_present"]
        )

        tp_present = bool(
            status["tp_present"]
        )

        if sl_present and tp_present:

            protection_status = (
                "FULLY_PROTECTED"
            )

            protected = True

            message = (
                "Posizione Phoenix "
                "completamente protetta"
            )

        elif sl_present or tp_present:

            protection_status = (
                "PARTIALLY_PROTECTED"
            )

            protected = False

            message = (
                "Posizione Phoenix "
                "parzialmente protetta"
            )

        else:

            protection_status = (
                "UNPROTECTED"
            )

            protected = False

            message = (
                "ATTENZIONE: posizione Phoenix "
                "senza SL e TP"
            )

        return {

            "active":
                True,

            "protected":
                protected,

            "status":
                protection_status,

            "ticket":
                status["ticket"],

            "symbol":
                status["symbol"],

            "direction":
                status["direction"],

            "sl":
                status["sl"],

            "tp":
                status["tp"],

            "sl_present":
                sl_present,

            "tp_present":
                tp_present,

            "message":
                message,

        }

    # =====================================
    # POSITION STATE ENGINE
    # =====================================

    def get_position_state(self):

        position = (
            self.get_active_position()
        )

        if position is None:

            return {

                "active":
                    False,

                "state":
                    "NO_POSITION",

                "symbol":
                    self.symbol,

                "message":
                    "Nessuna posizione Phoenix attiva",

            }

        profit = float(
            getattr(
                position,
                "profit",
                0.0
            )
        )

        sl = float(
            getattr(
                position,
                "sl",
                0.0
            )
        )

        tp = float(
            getattr(
                position,
                "tp",
                0.0
            )
        )

        # ---------------------------------
        # PROFIT / LOSS
        # ---------------------------------

        if profit > 0:

            result_state = "PROFIT"

        elif profit < 0:

            result_state = "LOSS"

        else:

            result_state = "BREAKEVEN"

        # ---------------------------------
        # PROTECTION
        # ---------------------------------

        if sl > 0 and tp > 0:

            protection_state = (
                "FULLY_PROTECTED"
            )

        elif sl > 0 or tp > 0:

            protection_state = (
                "PARTIALLY_PROTECTED"
            )

        else:

            protection_state = (
                "UNPROTECTED"
            )

        # ---------------------------------
        # POSITION STATE
        # ---------------------------------

        return {

            "active":
                True,

            "state":
                "POSITION_OPEN",

            "result_state":
                result_state,

            "protection_state":
                protection_state,

            "ticket":
                int(position.ticket),

            "symbol":
                position.symbol,

            "direction":
                (
                    "BUY"
                    if int(position.type) == 0
                    else "SELL"
                    if int(position.type) == 1
                    else "UNKNOWN"
                ),

            "volume":
                float(position.volume),

            "entry":
                float(position.price_open),

            "current_price":
                float(position.price_current),

            "sl":
                sl,

            "tp":
                tp,

            "profit":
                profit,

            "swap":
                float(
                    getattr(
                        position,
                        "swap",
                        0.0
                    )
                ),

            "magic":
                int(position.magic),

            "comment":
                position.comment,

        }

    # =====================================
    # POSITION METRICS
    # =====================================

    def get_position_metrics(self):

        position = (
            self.get_active_position()
        )

        if position is None:

            return {

                "active":
                    False,

                "symbol":
                    self.symbol,

                "status":
                    "NO_POSITION",

                "message":
                    "Nessuna posizione Phoenix attiva",

            }

        entry = float(
            getattr(
                position,
                "price_open",
                0.0
            )
        )

        current_price = float(
            getattr(
                position,
                "price_current",
                0.0
            )
        )

        sl = float(
            getattr(
                position,
                "sl",
                0.0
            )
        )

        tp = float(
            getattr(
                position,
                "tp",
                0.0
            )
        )

        volume = float(
            getattr(
                position,
                "volume",
                0.0
            )
        )

        profit = float(
            getattr(
                position,
                "profit",
                0.0
            )
        )

        swap = float(
            getattr(
                position,
                "swap",
                0.0
            )
        )

        position_type = int(
            getattr(
                position,
                "type",
                -1
            )
        )

        # ---------------------------------
        # DIRECTION
        # ---------------------------------

        if position_type == 0:

            direction = "BUY"

        elif position_type == 1:

            direction = "SELL"

        else:

            direction = "UNKNOWN"

        # ---------------------------------
        # PRICE DISTANCES
        # ---------------------------------

        distance_sl = None
        distance_tp = None

        if sl > 0:

            distance_sl = abs(
                current_price - sl
            )

        if tp > 0:

            distance_tp = abs(
                tp - current_price
            )

        # ---------------------------------
        # PRICE MOVEMENT
        # ---------------------------------

        price_difference = (
            current_price - entry
        )

        if direction == "SELL":

            price_difference = (
                entry - current_price
            )

        # ---------------------------------
        # PROFIT STATUS
        # ---------------------------------

        if profit > 0:

            profit_status = "PROFIT"

        elif profit < 0:

            profit_status = "LOSS"

        else:

            profit_status = "BREAKEVEN"

        # ---------------------------------
        # PROTECTION
        # ---------------------------------

        sl_present = (
            sl > 0
        )

        tp_present = (
            tp > 0
        )

        if sl_present and tp_present:

            protection_status = (
                "FULLY_PROTECTED"
            )

        elif sl_present or tp_present:

            protection_status = (
                "PARTIALLY_PROTECTED"
            )

        else:

            protection_status = (
                "UNPROTECTED"
            )

        # ---------------------------------
        # METRICS
        # ---------------------------------

        return {

            "active":
                True,

            "status":
                "POSITION_OPEN",

            "ticket":
                int(position.ticket),

            "symbol":
                position.symbol,

            "direction":
                direction,

            "volume":
                volume,

            "entry":
                entry,

            "current_price":
                current_price,

            "price_difference":
                price_difference,

            "sl":
                sl,

            "tp":
                tp,

            "distance_sl":
                distance_sl,

            "distance_tp":
                distance_tp,

            "profit":
                profit,

            "swap":
                swap,

            "profit_status":
                profit_status,

            "sl_present":
                sl_present,

            "tp_present":
                tp_present,

            "protection_status":
                protection_status,

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





