from Config.settings import MODE
"""
========================================
PROJECT PHOENIX AI
Execution Engine
Versione 10.0
========================================
"""

from Logs.logger import Logger

from Execution.execution_validator import ExecutionValidator
from Execution.execution_builder import ExecutionBuilder
from Execution.execution_report import ExecutionReport

from MT5_Bridge.mt5_execution import (
    MT5ExecutionEngine
)


class ExecutionEngine:
    """
    Execution Engine centrale di PROJECT PHOENIX AI.

    Gestisce:

    - Paper Trading
    - preparazione ordini
    - validazione
    - apertura MT5
    - chiusura MT5
    - DRY RUN
    - report
    - contratto uniforme dei risultati
    """

    def __init__(
        self,
        symbol="BTCUSD",
        magic=260813,
        mt5_enabled=False,
        mt5_dry_run=True
    ):

        self.validator = ExecutionValidator()

        self.builder = ExecutionBuilder()

        self.report = ExecutionReport()

        self.symbol = symbol

        self.magic = magic

        # PHOENIX MT5 ROUTING
        #
        # mt5_enabled e mt5_dry_run sono parametri
        # espliciti del costruttore.
        #
        # Questo permette:
        #
        # DEMO + mt5_enabled=True
        #     -> MT5 DEMO reale
        #
        # DEMO + mt5_enabled=False
        #     -> Paper Trading
        #
        # LIVE
        #     -> MT5 LIVE solo quando richiesto
        #
        # Il controllo del conto DEMO/LIVE viene
        # effettuato dal livello MT5 prima dell'ordine.

        self.mt5_enabled = bool(
            mt5_enabled
        )

        self.mt5_dry_run = bool(
            mt5_dry_run
        )

        self.mt5 = None

        if self.mt5_enabled:

            self.mt5 = MT5ExecutionEngine(

                symbol=self.symbol,

                magic=self.magic

            )

            Logger.success(
                "Execution Engine V10: "
                "MT5 Bridge configurato."
            )

        else:

            Logger.success(
                "Execution Engine V10: "
                "Paper Trading configurato."
            )

    # =====================================
    # CONNESSIONE MT5
    # =====================================

    def connect_mt5(self):

        if self.mt5 is None:

            return False

        result = self.mt5.connect()

        if result:

            Logger.success(
                "Execution Engine: "
                "connessione MT5 riuscita."
            )

        else:

            Logger.warning(
                "Execution Engine: "
                "connessione MT5 fallita."
            )

        return result

    # =====================================
    # DISCONNESSIONE MT5
    # =====================================

    def disconnect_mt5(self):

        if self.mt5 is not None:

            self.mt5.disconnect()

            Logger.info(
                "Execution Engine: "
                "MT5 disconnesso."
            )

    # =====================================
    # APERTURA ORDINE
    # =====================================

    def execute(
        self,
        trade
    ):

        # =================================
        # VALIDAZIONE
        # =================================

        valid, reason = (
            self.validator.validate(
                trade
            )
        )

        if not valid:

            Logger.warning(
                f"Trade rifiutato: {reason}"
            )

            return {

                "success": False,

                "executed": False,

                "dry_run": False,

                "message": reason,

                "reason": reason,

                "order": None,

                "mt5": None

            }

        # =================================
        # COSTRUZIONE ORDINE
        # =================================

        order = self.builder.build(
            trade
        )

        # =================================
        # PAPER TRADING
        # =================================

        if not self.mt5_enabled:

            Logger.success(

                f"Ordine Paper Trading: "
                f"{order['side']} "
                f"{order['symbol']} "
                f"@ {order['entry']}"

            )

            return {

                **order,

                "success": True,

                "executed": True,

                "dry_run": False,

                "message":
                    "Ordine Paper Trading eseguito",

                "mt5": None

            }

        # =================================
        # MT5 NON CONFIGURATO
        # =================================

        if self.mt5 is None:

            return {

                **order,

                "success": False,

                "executed": False,

                "dry_run": False,

                "message":
                    "MT5 Bridge non configurato",

                "mt5": None

            }

        # =================================
        # TRADE PER MT5
        # =================================

        mt5_trade = {

            "symbol":
                self.symbol,

            "side":
                order["side"],

            "entry":
                order["entry"],

            "stop_loss":
                order["stop_loss"],

            "take_profit":
                order["take_profit"],

            "size":
                order["size"],

            "signal":
                order.get(
                    "signal",
                    order["side"]
                )

        }

        # =================================
        # ESECUZIONE MT5
        # =================================

        result = self.mt5.execute(

            mt5_trade,

            dry_run=self.mt5_dry_run

        )

        executed = bool(
            result.get(
                "executed",
                False
            )
        )

        dry_run = bool(
            result.get(
                "dry_run",
                self.mt5_dry_run
            )
        )

        message = result.get(
            "message",
            "Ordine non eseguito"
        )

        if dry_run:

            Logger.info(
                "MT5 DRY RUN: "
                "ordine verificato."
            )

        elif executed:

            Logger.success(

                f"MT5: ordine eseguito "
                f"{order['side']} "
                f"{order['symbol']}"

            )

        else:

            Logger.warning(
                "MT5: "
                + str(message)
            )

        return {

            **order,

            "success":
                executed,

            "executed":
                executed,

            "dry_run":
                dry_run,

            "message":
                message,

            # =================================
            # MT5 RESULT PROPAGATION
            # =================================

            "mt5":
                result,

            "ticket":
                result.get("ticket")
                or (
                    getattr(
                        result.get("result"),
                        "order",
                        None
                    )
                    if result.get("result") is not None
                    else None
                ),

            "deal":
                result.get("deal")
                or (
                    getattr(
                        result.get("result"),
                        "deal",
                        None
                    )
                    if result.get("result") is not None
                    else None
                ),

            "order_ticket":
                result.get("order")
                or (
                    getattr(
                        result.get("result"),
                        "order",
                        None
                    )
                    if result.get("result") is not None
                    else None
                ),

            "execution_price":
                result.get("price")
                or (
                    getattr(
                        result.get("result"),
                        "price",
                        None
                    )
                    if result.get("result") is not None
                    else None
                ),

            "retcode":
                result.get("retcode")
                or (
                    getattr(
                        result.get("result"),
                        "retcode",
                        None
                    )
                    if result.get("result") is not None
                    else None
                ),

        }

    # =====================================
    # CHIUSURA ORDINE
    # =====================================

    def close(
        self,
        closed_position
    ):

        # =================================
        # VALIDAZIONE POSIZIONE
        # =================================

        if closed_position is None:

            return {

                "success": False,

                "executed": False,

                "dry_run": False,

                "message":
                    "Posizione da chiudere non valida",

                "position": None,

                "report": None,

                "mt5": None

            }

        # =================================
        # PAPER TRADING
        # =================================

        if not self.mt5_enabled:

            report = self.report.build(
                closed_position
            )

            Logger.success(

                f"Ordine chiuso: "
                f"{report['symbol']} "
                f"PnL {report['pnl']:.2f}"

            )

            return {

                "success": True,

                "executed": True,

                "dry_run": False,

                "message":
                    "Chiusura Paper Trading completata",

                "position":
                    closed_position,

                "symbol":
                    closed_position.get(
                        "symbol"
                    ),

                "side":
                    closed_position.get(
                        "side"
                    ),

                "entry":
                    closed_position.get(
                        "entry"
                    ),

                "exit":
                    closed_position.get(
                        "current_price"
                    ),

                "current_price":
                    closed_position.get(
                        "current_price"
                    ),

                "stop_loss":
                    closed_position.get(
                        "stop_loss"
                    ),

                "take_profit":
                    closed_position.get(
                        "take_profit"
                    ),

                "size":
                    closed_position.get(
                        "size"
                    ),

                "close_reason":
                    closed_position.get(
                        "close_reason"
                    ),

                "status":
                    closed_position.get(
                        "status"
                    ),

                "reason":
                    closed_position.get(
                        "close_reason"
                    ),

                "report":
                    report,

                "pnl":
                    report.get(
                        "pnl",
                        0.0
                    ),

                "close_time":
                    report.get(
                        "close_time"
                    ) or closed_position.get(
                        "close_time"
                    ),

                "mt5":
                    None

            }

        # =================================
        # MT5 NON CONFIGURATO
        # =================================

        if self.mt5 is None:

            return {

                "success": False,

                "executed": False,

                "dry_run": False,

                "message":
                    "MT5 Bridge non configurato",

                "position":
                    closed_position,

                "report":
                    None,

                "mt5":
                    None

            }

        # =================================
        # CHIUSURA MT5
        # =================================

        result = self.mt5.close_position(

            closed_position,

            dry_run=self.mt5_dry_run

        )

        executed = bool(
            result.get(
                "executed",
                False
            )
        )

        dry_run = bool(
            result.get(
                "dry_run",
                self.mt5_dry_run
            )
        )

        message = result.get(
            "message",
            "Chiusura elaborata"
        )

        # =================================
        # LOG
        # =================================

        if dry_run:

            Logger.info(
                "MT5 DRY RUN: "
                "chiusura verificata."
            )

        elif executed:

            Logger.success(
                "MT5: posizione chiusa."
            )

        else:

            Logger.warning(
                "MT5: "
                + str(message)
            )

        # =================================
        # CONTRATTO UNIFORME
        # =================================

        return {

            "success":
                executed,

            "executed":
                executed,

            "dry_run":
                dry_run,

            "message":
                message,

            "position":
                closed_position,

            "symbol":
                closed_position.get(
                    "symbol"
                ),

            "side":
                closed_position.get(
                    "side"
                ),

            "report":
                None,

            "pnl":
                float(
                    closed_position.get(
                        "current_profit",
                        0.0
                    )
                ),

            "mt5":
                result

        }
