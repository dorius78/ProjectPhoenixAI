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
    # POSITION RISK GUARD
    # =====================================

    def check_position_risk(
        self,
        action,
        expected_symbol=None,
        expected_magic=None
    ):

        action = str(
            action
        ).strip().upper()

        if expected_symbol is None:

            expected_symbol = self.symbol

        if expected_magic is None:

            expected_magic = self.magic

        allowed_actions = {
            "HOLD",
            "CLOSE",
            "PROTECT",
            "MODIFY",
        }

        # ---------------------------------
        # ACTION VALIDATION
        # ---------------------------------

        if action not in allowed_actions:

            return {

                "approved":
                    False,

                "status":
                    "BLOCKED",

                "action":
                    action,

                "reason":
                    "Azione posizione non consentita",

                "message":
                    "Risk Guard ha bloccato l'azione",

            }

        # ---------------------------------
        # ACTIVE POSITION
        # ---------------------------------

        position = (
            self.get_active_position()
        )

        if position is None:

            return {

                "approved":
                    False,

                "status":
                    "NO_POSITION",

                "action":
                    action,

                "reason":
                    "Nessuna posizione Phoenix attiva",

                "message":
                    "Impossibile autorizzare l'azione",

            }

        # ---------------------------------
        # MAGIC VALIDATION
        # ---------------------------------

        position_magic = int(
            getattr(
                position,
                "magic",
                -1
            )
        )

        if position_magic != int(
            expected_magic
        ):

            return {

                "approved":
                    False,

                "status":
                    "BLOCKED",

                "action":
                    action,

                "reason":
                    "Magic number non corrispondente",

                "message":
                    "Posizione non riconosciuta come Phoenix",

                "ticket":
                    int(position.ticket),

                "position_magic":
                    position_magic,

                "expected_magic":
                    int(expected_magic),

            }

        # ---------------------------------
        # SYMBOL VALIDATION
        # ---------------------------------

        position_symbol = str(
            getattr(
                position,
                "symbol",
                ""
            )
        )

        if position_symbol != str(
            expected_symbol
        ):

            return {

                "approved":
                    False,

                "status":
                    "BLOCKED",

                "action":
                    action,

                "reason":
                    "Simbolo non corrispondente",

                "message":
                    "Il simbolo della posizione non coincide",

                "ticket":
                    int(position.ticket),

                "position_symbol":
                    position_symbol,

                "expected_symbol":
                    str(expected_symbol),

            }

        # ---------------------------------
        # VOLUME VALIDATION
        # ---------------------------------

        volume = float(
            getattr(
                position,
                "volume",
                0.0
            )
        )

        if volume <= 0:

            return {

                "approved":
                    False,

                "status":
                    "BLOCKED",

                "action":
                    action,

                "reason":
                    "Volume posizione non valido",

                "message":
                    "Il volume deve essere maggiore di zero",

                "ticket":
                    int(position.ticket),

                "volume":
                    volume,

            }

        # ---------------------------------
        # PROTECTION CHECK
        # ---------------------------------

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

        protection_status = (

            "FULLY_PROTECTED"

            if sl > 0 and tp > 0

            else

            "PARTIALLY_PROTECTED"

            if sl > 0 or tp > 0

            else

            "UNPROTECTED"

        )

        # ---------------------------------
        # FINAL APPROVAL
        # ---------------------------------

        return {

            "approved":
                True,

            "status":
                "APPROVED",

            "action":
                action,

            "ticket":
                int(position.ticket),

            "symbol":
                position_symbol,

            "magic":
                position_magic,

            "volume":
                volume,

            "sl":
                sl,

            "tp":
                tp,

            "protection_status":
                protection_status,

            "reason":
                "Controlli Risk Guard superati",

            "message":
                "Azione posizione autorizzata",

        }

    # =====================================
    # POSITION DECISION PIPELINE
    # =====================================

    def run_position_decision_pipeline(self):

        evaluation = (
            self.evaluate_position_action()
        )

        # ---------------------------------
        # NO POSITION
        # ---------------------------------

        if not evaluation["active"]:

            return {

                "approved":
                    False,

                "decision":
                    "NO_POSITION",

                "action":
                    "NO_POSITION",

                "status":
                    "NO_POSITION",

                "symbol":
                    self.symbol,

                "reason":
                    evaluation.get(
                        "reason",
                        "Nessuna posizione Phoenix attiva"
                    ),

                "message":
                    "Position Decision Pipeline completata",
            }

        action = str(
            evaluation.get(
                "action",
                "HOLD"
            )
        ).strip().upper()

        # ---------------------------------
        # RISK GUARD
        # ---------------------------------

        risk = (
            self.check_position_risk(
                action=action
            )
        )

        # ---------------------------------
        # RISK BLOCK
        # ---------------------------------

        if not risk["approved"]:

            return {

                "approved":
                    False,

                "decision":
                    "BLOCKED",

                "action":
                    action,

                "status":
                    risk.get(
                        "status",
                        "BLOCKED"
                    ),

                "ticket":
                    evaluation.get(
                        "ticket"
                    ),

                "symbol":
                    evaluation.get(
                        "symbol",
                        self.symbol
                    ),

                "reason":
                    risk.get(
                        "reason",
                        "Risk Guard ha bloccato l'azione"
                    ),

                "risk":
                    risk,

                "evaluation":
                    evaluation,

                "message":
                    "Decisione bloccata dal Position Risk Guard",
            }

        # ---------------------------------
        # APPROVED DECISION
        # ---------------------------------

        return {

            "approved":
                True,

            "decision":
                action,

            "action":
                action,

            "status":
                "APPROVED",

            "ticket":
                evaluation.get(
                    "ticket"
                ),

            "symbol":
                evaluation.get(
                    "symbol",
                    self.symbol
                ),

            "direction":
                evaluation.get(
                    "direction"
                ),

            "volume":
                evaluation.get(
                    "volume"
                ),

            "profit":
                evaluation.get(
                    "profit"
                ),

            "profit_status":
                evaluation.get(
                    "profit_status"
                ),

            "protection_status":
                evaluation.get(
                    "protection_status"
                ),

            "reason":
                evaluation.get(
                    "action_reason",
                    "Azione approvata"
                ),

            "risk":
                risk,

            "evaluation":
                evaluation,

            "message":
                "Decisione posizione approvata dal Risk Guard",
        }





    # =====================================
    # POSITION ACTION EVALUATION
    # =====================================

    def evaluate_position_action(self):

        state = (
            self.get_position_state()
        )

        if not state["active"]:

            return {

                "active":
                    False,

                "action":
                    "NO_POSITION",

                "status":
                    "NO_POSITION",

                "symbol":
                    self.symbol,

                "reason":
                    "Nessuna posizione Phoenix attiva",

                "message":
                    "Nessuna posizione da valutare",

            }

        metrics = (
            self.get_position_metrics()
        )

        protection = (
            self.check_position_protection()
        )

        action = "HOLD"

        reason = (
            "Posizione Phoenix attiva "
            "senza condizioni immediate "
            "di chiusura"
        )

        # ---------------------------------
        # PROTECTION CHECK
        # ---------------------------------

        if not protection["protected"]:

            action = "PROTECT"

            reason = (
                "La posizione Phoenix "
                "non risulta completamente protetta"
            )

        # ---------------------------------
        # PROFIT / LOSS CHECK
        # ---------------------------------

        elif metrics["profit_status"] == "LOSS":

            action = "HOLD"

            reason = (
                "Posizione in perdita: "
                "nessuna chiusura automatica "
                "decisa dal Position Manager"
            )

        elif metrics["profit_status"] == "PROFIT":

            action = "HOLD"

            reason = (
                "Posizione in profitto: "
                "monitoraggio attivo"
            )

        elif metrics["profit_status"] == "BREAKEVEN":

            action = "HOLD"

            reason = (
                "Posizione prossima al breakeven"
            )

        return {

            "active":
                True,

            "action":
                action,

            "status":
                "POSITION_OPEN",

            "ticket":
                metrics["ticket"],

            "symbol":
                metrics["symbol"],

            "direction":
                metrics["direction"],

            "volume":
                metrics["volume"],

            "entry":
                metrics["entry"],

            "current_price":
                metrics["current_price"],

            "profit":
                metrics["profit"],

            "profit_status":
                metrics["profit_status"],

            "sl":
                metrics["sl"],

            "tp":
                metrics["tp"],

            "protection_status":
                metrics["protection_status"],

            "action_reason":
                reason,

            "message":
                "Valutazione posizione completata",

        }



    # =====================================
    # POSITION ACTION LAYER
    # =====================================

    def prepare_position_action(
        self,
        action,
        reason="",
        source="SYSTEM"
    ):

        if action is None:
            action = ""

        action = str(
            action
        ).strip().upper()

        reason = str(
            reason
        ).strip()

        source = str(
            source
        ).strip()

        allowed_actions = {
            "HOLD",
            "CLOSE",
            "PROTECT",
            "MODIFY",
        }

        if action not in allowed_actions:

            return {

                "valid":
                    False,

                "action":
                    action,

                "reason":
                    reason,

                "source":
                    source,

                "message":
                    "Azione posizione non valida",

            }

        position = (
            self.get_active_position()
        )

        if position is None:

            return {

                "valid":
                    False,

                "action":
                    action,

                "reason":
                    reason,

                "source":
                    source,

                "status":
                    "NO_POSITION",

                "message":
                    "Nessuna posizione Phoenix attiva",

            }

        return {

            "valid":
                True,

            "action":
                action,

            "reason":
                reason,

            "source":
                source,

            "status":
                "POSITION_OPEN",

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

            "message":
                "Azione posizione preparata",

        }

    # =====================================
    # POSITION ACTION EXECUTION
    # =====================================

    def execute_position_action(
        self,
        action,
        reason="",
        source="SYSTEM",
        dry_run=True
    ):

        # ---------------------------------
        # PREPARE ACTION
        # ---------------------------------

        prepared = (
            self.prepare_position_action(
                action=action,
                reason=reason,
                source=source
            )
        )

        # ---------------------------------
        # INVALID ACTION / NO POSITION
        # ---------------------------------

        if not prepared["valid"]:

            return {

                "executed":
                    False,

                "dry_run":
                    dry_run,

                "action":
                    prepared.get(
                        "action",
                        str(action).strip().upper()
                        if action is not None
                        else ""
                    ),

                "status":
                    prepared.get(
                        "status",
                        "INVALID"
                    ),

                "message":
                    prepared.get(
                        "message",
                        "Azione non eseguibile"
                    ),

                "reason":
                    prepared.get(
                        "reason",
                        reason
                    ),

                "source":
                    prepared.get(
                        "source",
                        source
                    ),

                "result":
                    None,

            }

        normalized_action = (
            prepared["action"]
        )

        # ---------------------------------
        # HOLD
        # ---------------------------------

        if normalized_action == "HOLD":

            return {

                "executed":
                    False,

                "dry_run":
                    dry_run,

                "action":
                    "HOLD",

                "status":
                    "HELD",

                "ticket":
                    prepared["ticket"],

                "symbol":
                    prepared["symbol"],

                "message":
                    "Posizione mantenuta aperta",

                "reason":
                    prepared["reason"],

                "source":
                    prepared["source"],

                "result":
                    None,

            }

        # ---------------------------------
        # PROTECT
        # ---------------------------------

        if normalized_action == "PROTECT":

            position = (
                self.get_active_position()
            )

            if position is None:

                return {

                    "executed":
                        False,

                    "dry_run":
                        dry_run,

                    "action":
                        "PROTECT",

                    "status":
                        "NO_POSITION",

                    "message":
                        "Nessuna posizione Phoenix da proteggere",

                    "reason":
                        prepared["reason"],

                    "source":
                        prepared["source"],

                    "result":
                        None,

                }

            current_sl = float(
                getattr(
                    position,
                    "sl",
                    0.0
                ) or 0.0
            )

            current_tp = float(
                getattr(
                    position,
                    "tp",
                    0.0
                ) or 0.0
            )

            result = self.bridge.modify_position(

                position=position,

                stop_loss=current_sl,

                take_profit=current_tp,

                dry_run=dry_run

            )

            return {

                "executed":
                    result.get(
                        "executed",
                        False
                    ),

                "dry_run":
                    result.get(
                        "dry_run",
                        dry_run
                    ),

                "action":
                    "PROTECT",

                "status":
                    (
                        "PROTECTED"
                        if result.get(
                            "executed",
                            False
                        )
                        else
                        "DRY_RUN"
                        if dry_run
                        else
                        "FAILED"
                    ),

                "ticket":
                    prepared["ticket"],

                "symbol":
                    prepared["symbol"],

                "message":
                    result.get(
                        "message",
                        "Protezione posizione elaborata"
                    ),

                "reason":
                    prepared["reason"],

                "source":
                    prepared["source"],

                "result":
                    result,

            }

        # ---------------------------------
        # MODIFY
        # ---------------------------------

        if normalized_action == "MODIFY":

            return {

                "executed":
                    False,

                "dry_run":
                    dry_run,

                "action":
                    "MODIFY",

                "status":
                    "NOT_IMPLEMENTED",

                "ticket":
                    prepared["ticket"],

                "symbol":
                    prepared["symbol"],

                "message":
                    "Modifica posizione non ancora collegata al Bridge",

                "reason":
                    prepared["reason"],

                "source":
                    prepared["source"],

                "result":
                    None,

            }

        # ---------------------------------
        # CLOSE
        # ---------------------------------

        if normalized_action == "CLOSE":

            position = (
                self.get_active_position()
            )

            if position is None:

                return {

                    "executed":
                        False,

                    "dry_run":
                        dry_run,

                    "action":
                        "CLOSE",

                    "status":
                        "NO_POSITION",

                    "message":
                        "Nessuna posizione Phoenix da chiudere",

                    "reason":
                        prepared["reason"],

                    "source":
                        prepared["source"],

                    "result":
                        None,

                }

            # ---------------------------------
            # DRY RUN
            # ---------------------------------

            if dry_run:

                return {

                    "executed":
                        False,

                    "dry_run":
                        True,

                    "action":
                        "CLOSE",

                    "status":
                        "DRY_RUN",

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

                    "message":
                        "Chiusura simulata: nessuna operazione reale inviata",

                    "reason":
                        prepared["reason"],

                    "source":
                        prepared["source"],

                    "result":
                        None,

                }

            # ---------------------------------
            # REAL EXECUTION
            # ---------------------------------

            try:

                result = (
                    self.bridge.close_position(
                        position,
                        dry_run=False
                    )
                )

                return {

                    "executed":
                        True,

                    "dry_run":
                        False,

                    "action":
                        "CLOSE",

                    "status":
                        "EXECUTED",

                    "ticket":
                        int(position.ticket),

                    "symbol":
                        position.symbol,

                    "message":
                        "Chiusura posizione inviata al MT5 Bridge",

                    "reason":
                        prepared["reason"],

                    "source":
                        prepared["source"],

                    "result":
                        result,

                }

            except Exception as exc:

                return {

                    "executed":
                        False,

                    "dry_run":
                        False,

                    "action":
                        "CLOSE",

                    "status":
                        "ERROR",

                    "ticket":
                        int(position.ticket),

                    "symbol":
                        position.symbol,

                    "message":
                        "Errore durante l'esecuzione della chiusura",

                    "error":
                        str(exc),

                    "reason":
                        prepared["reason"],

                    "source":
                        prepared["source"],

                    "result":
                        None,

                }

        # ---------------------------------
        # FALLBACK
        # ---------------------------------

        return {

            "executed":
                False,

            "dry_run":
                dry_run,

            "action":
                normalized_action,

            "status":
                "UNHANDLED_ACTION",

            "message":
                "Azione riconosciuta ma non gestita",

            "reason":
                prepared["reason"],

            "source":
                prepared["source"],

            "result":
                None,

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











