from pathlib import Path

path = Path("MT5_Bridge/mt5_execution_recovered.py")
text = path.read_text(encoding="utf-8")

old = '''        return {

            "executed":
                result.retcode
                == mt5.TRADE_RETCODE_DONE,

            "dry_run":
                False,

            "message":
                "Ordine inviato a MT5",

            "retcode":
                result.retcode,

            "result":
                result,

            "risk_gate":
                checked["risk_gate"],

        }
'''

new = '''        executed = (
            result.retcode
            == mt5.TRADE_RETCODE_DONE
        )

        # =================================
        # RIFERIMENTI MT5
        # =================================

        order_ticket = int(
            getattr(
                result,
                "order",
                0
            )
            or 0
        )

        deal_ticket = int(
            getattr(
                result,
                "deal",
                0
            )
            or 0
        )

        position_ticket = 0

        if executed:

            try:

                positions = (
                    self.get_phoenix_positions()
                )

                if positions:

                    matching = [
                        p
                        for p in positions
                        if str(
                            getattr(
                                p,
                                "symbol",
                                ""
                            )
                        ) == str(
                            self.symbol
                        )
                    ]

                    if matching:

                        position_ticket = int(
                            getattr(
                                matching[0],
                                "ticket",
                                0
                            )
                            or 0
                        )

            except Exception as error:

                Logger.warning(
                    "Impossibile recuperare "
                    "il ticket posizione MT5: "
                    f"{error}"
                )

        return {

            "executed":
                executed,

            "dry_run":
                False,

            "success":
                executed,

            "message":
                "Ordine inviato a MT5",

            "retcode":
                result.retcode,

            "order_ticket":
                order_ticket,

            "deal_ticket":
                deal_ticket,

            "position_ticket":
                position_ticket,

            "result":
                result,

            "risk_gate":
                checked["risk_gate"],

        }
'''

if old not in text:
    raise RuntimeError(
        "STOP: blocco return execute() non trovato"
    )

if '"order_ticket"' in text:
    raise RuntimeError(
        "STOP: contratto MT5 gia modificato"
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

print("E.27.12.24 PATCH APPLICATA")
print("Contratto execute() aggiornato")
print("order_ticket: OK")
print("deal_ticket: OK")
print("position_ticket: OK")
print("success: OK")
print("NESSUN ordine inviato durante la patch")
