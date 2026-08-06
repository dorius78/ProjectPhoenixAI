"""
========================================
PROJECT PHOENIX AI
Execution Engine
Versione 8.0
========================================
"""

from Logs.logger import Logger

from Execution.execution_validator import ExecutionValidator
from Execution.execution_builder import ExecutionBuilder
from Execution.execution_report import ExecutionReport


class ExecutionEngine:
    """
    Adattatore leggero tra il Trade Manager/Risk Manager e il broker.

    Oggi il "broker" è la simulazione (Paper Trading): l'esecuzione
    è sempre accettata se il trade supera la validazione. In futuro,
    per collegare un broker reale, basta cambiare solo il corpo di
    ExecutionBuilder.build()/ExecutionReport.build() mantenendo lo
    stesso contratto, senza toccare Core.position_controller o il
    resto della pipeline.

    La responsabilità è divisa in tre componenti dedicati:
      - ExecutionValidator: controlla che il trade sia valido prima
        di provare ad eseguirlo (rifiuta segnali HOLD o non validi)
      - ExecutionBuilder: costruisce il dizionario "ordine" in apertura
      - ExecutionReport: costruisce il dizionario "report" in chiusura

    Tutta la logica di gestione della posizione (break-even, trailing
    stop, calcolo del profitto, monitoraggio SL/TP) resta invece in
    Core.position_controller.PositionController: questo modulo non
    la duplica.
    """

    def __init__(self):

        self.validator = ExecutionValidator()
        self.builder = ExecutionBuilder()
        self.report = ExecutionReport()

        Logger.success("Execution Engine V8 inizializzato.")

    # =====================================
    # APERTURA ORDINE
    # =====================================

    def execute(self, trade):

        valid, reason = self.validator.validate(trade)

        if not valid:

            Logger.warning(f"Trade rifiutato: {reason}")

            return {"success": False, "reason": reason}

        order = self.builder.build(trade)

        Logger.success(
            f"Ordine eseguito: {order['side']} {order['symbol']} "
            f"@ {order['entry']}"
        )

        return order

    # =====================================
    # CHIUSURA ORDINE
    # =====================================

    def close(self, closed_position):

        report = self.report.build(closed_position)

        Logger.success(
            f"Ordine chiuso: {report['symbol']} "
            f"PnL {report['pnl']:.2f}"
        )

        return report