"""
========================================
PROJECT PHOENIX AI
Execution Engine
Versione 9.0
========================================
"""

from Logs.logger import Logger

from Execution.execution_validator import ExecutionValidator
from Execution.execution_builder import ExecutionBuilder
from Execution.execution_report import ExecutionReport

from MT5_Bridge.mt5_execution_recovered import (
    MT5ExecutionEngine
)


class ExecutionEngine:
    """
    Execution Engine centrale di Phoenix.

    Gestisce:

    - Paper Trading
    - Preparazione ordini
    - Validazione
    - Collegamento controllato al Bridge MT5
    - DRY RUN
    - Report di chiusura

    Il Core continua a utilizzare lo stesso contratto.
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
                "Execution Engine V9: "
                "MT5 Bridge configurato."
            )

        else:

            Logger.success(
                "Execution Engine V9: "
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
        # VALIDAZIONE CORE
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

                "reason": reason

            }

        # =================================
        # COSTRUZIONE ORDINE CORE
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

            return order

        # =================================
        # MT5
        # =================================

        if self.mt5 is None:

            return {

                "success": False,

                "reason":
                    "MT5 Bridge non configurato"

            }

        # =================================
        # CONVERSIONE TRADE
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
        # MT5 EXECUTION
        # =================================

        result = self.mt5.execute(

            mt5_trade,

            dry_run=self.mt5_dry_run

        )

        # =================================
        # ERRORE
        # =================================

        if not result.get(
            "executed",
            False
        ):

            # ---------------------------------
            # DRY RUN
            # ---------------------------------

            if result.get(
                "dry_run",
                False
            ):

                Logger.info(
                    "MT5 DRY RUN: "
                    "ordine verificato."
                )

            else:

                Logger.warning(
                    "MT5: "
                    + str(
                        result.get(
                            "message",
                            "Esecuzione fallita"
                        )
                    )
                )

            # ---------------------------------
            # RISULTATO COMPATIBILE CORE
            # ---------------------------------

            return {

                **order,

                "success":
                    False,

                "executed":
                    False,

                "dry_run":
                    result.get(
                        "dry_run",
                        self.mt5_dry_run
                    ),

                "message":
                    result.get(
                        "message",
                        "Ordine non eseguito"
                    ),

                "mt5":
                    result

            }

        # =================================
        # MT5 ESEGUITO
        # =================================

        Logger.success(

            f"MT5: ordine eseguito "
            f"{order['side']} "
            f"{order['symbol']}"

        )

        return {

            **order,

            "success":
                True,

            "executed":
                True,

            "dry_run":
                False,

            "message":
                result.get(
                    "message",
                    "Ordine inviato a MT5"
                ),

            "mt5":
                result

        }

    # =====================================
    # CHIUSURA ORDINE
    # =====================================

    def close(
        self,
        closed_position
    ):

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

            return report

        # =================================
        # MT5
        # =================================

        if self.mt5 is None:

            return {

                "success": False,

                "message":
                    "MT5 Bridge non configurato"

            }

        position = (
            closed_position
        )

        result = self.mt5.close_position(

            position,

            dry_run=self.mt5_dry_run

        )

        return {

            "success":
                result.get(
                    "executed",
                    False
                ),

            "executed":
                result.get(
                    "executed",
                    False
                ),

            "dry_run":
                result.get(
                    "dry_run",
                    self.mt5_dry_run
                ),

            "message":
                result.get(
                    "message",
                    "Chiusura elaborata"
                ),

            "mt5":
                result

        }