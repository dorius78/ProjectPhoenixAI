"""
========================================
PROJECT PHOENIX AI
Execution Engine
Versione 9.1
========================================
"""

from Logs.logger import Logger

from Execution.execution_builder import ExecutionBuilder
from Execution.execution_report import ExecutionReport
from Execution.execution_validator import ExecutionValidator


class ExecutionEngine:

    def __init__(self):

        Logger.success(
            "Execution Engine V9.1 inizializzato."
        )

        self.orders = []

        self.validator = ExecutionValidator()
        self.builder = ExecutionBuilder()
        self.report = ExecutionReport()

    def execute(

        self,

        trade

    ):

        Logger.section(
            "EXECUTION ENGINE"
        )

        valid, message = self.validator.validate(
            trade
        )

        if not valid:

            Logger.warning(message)

            return {

                "success": False,

                "message": message

            }

        order = self.builder.build(
            trade
        )

        self.orders.append(order)

        Logger.success(
            f"Ordine {order['side']} aperto."
        )

        return order

    def close(

        self,

        position

    ):

        report = self.report.build(
            position
        )

        if report is None:

            return None

        Logger.success(
            f"Ordine {report['side']} chiuso."
        )

        return report

    def get_orders(self):

        return self.orders

    def reset(self):

        self.orders.clear()

        Logger.info(
            "Execution Engine azzerato."
        )