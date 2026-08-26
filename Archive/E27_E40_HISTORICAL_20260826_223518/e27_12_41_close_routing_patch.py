from pathlib import Path

path = Path("Core/live_trading_engine.py")

text = path.read_text(
    encoding="utf-8"
)

old = '''        # =================================
        # EXECUTION CLOSE
        # =================================

        report = self.execution.close(
            closed
        )

        # =================================
        # VERIFICA ESECUZIONE
        # =================================

        execution_success = report.get(
            "success",
            True
        )

        dry_run = report.get(
            "dry_run",
            False
        )
'''

new = '''        # =================================
        # CLOSE ROUTING
        # =================================
        #
        # Se MT5 ha gia chiuso la posizione
        # esternamente, NON dobbiamo chiamare
        # execution.close().
        #
        # La chiusura e gia avvenuta sul broker.
        # Phoenix deve solamente registrare
        # l'evento.
        #

        external_mt5_close = (
            closed.get("close_reason")
            == "MT5 EXTERNAL CLOSE"
        )

        if external_mt5_close:

            report = {

                "success": True,

                "executed": True,

                "dry_run": False,

                "message":
                    "Chiusura MT5 gia confermata",

                "symbol":
                    closed.get("symbol"),

                "side":
                    closed.get("side"),

                "entry":
                    closed.get("entry", 0.0),

                "exit":
                    closed.get(
                        "current_price",
                        closed.get(
                            "entry",
                            0.0
                        )
                    ),

                "pnl":
                    closed.get(
                        "current_profit",
                        0.0
                    ),

                "close_time":
                    closed.get("close_time"),

                "reason":
                    "MT5 EXTERNAL CLOSE",

                "mt5_ticket":
                    closed.get(
                        "mt5_ticket",
                        0
                    ),

                "trade_id":
                    closed.get(
                        "trade_id"
                    )

            }

            Logger.info(
                "MT5 EXTERNAL CLOSE: "
                "nessuna nuova esecuzione richiesta."
            )

        else:

            # =================================
            # EXECUTION CLOSE
            # =================================

            report = self.execution.close(
                closed
            )

        # =================================
        # VERIFICA ESECUZIONE
        # =================================

        execution_success = report.get(
            "success",
            True
        )

        dry_run = report.get(
            "dry_run",
            False
        )
'''

if old not in text:
    raise RuntimeError(
        "STOP: blocco CLOSE ROUTING non trovato"
    )

if "external_mt5_close" in text:
    raise RuntimeError(
        "STOP: E.27.12.41 gia applicata"
    )

text = text.replace(
    old,
    new,
    1
)

path.write_text(
    text,
    encoding="utf-8"
)

print("=" * 100)
print("E.27.12.41 PATCH APPLICATA")
print("=" * 100)
print("MT5 EXTERNAL CLOSE ROUTING: OK")
print("execution.close() BYPASS: OK")
print("CLOSED REPORT: OK")
print("NESSUN order_send DURANTE LA PATCH")
print("=" * 100)

