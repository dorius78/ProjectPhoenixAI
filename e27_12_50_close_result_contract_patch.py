from pathlib import Path

path = Path(
    "MT5_Bridge/mt5_execution_recovered.py"
)

text = path.read_text(
    encoding="utf-8"
)

old = '''        return {

            "executed":
                result.retcode
                == mt5.TRADE_RETCODE_DONE,

            "dry_run":
                False,

            "message":
                "Posizione chiusa",

            "order":
                request,

            "check":
                check,

            "retcode":
                result.retcode,

            "result":
                result,

        }
'''

new = '''        executed = (
            result.retcode
            == mt5.TRADE_RETCODE_DONE
        )

        # =================================
        # RIFERIMENTI MT5 CHIUSURA
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

        position_ticket = int(
            getattr(
                result,
                "position",
                0
            )
            or 0
        )

        return {

            "executed":
                executed,

            "success":
                executed,

            "dry_run":
                False,

            "message":
                "Posizione chiusa",

            "order":
                request,

            "check":
                check,

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

        }
'''

if old not in text:
    raise RuntimeError(
        "STOP: return finale close_position() non trovato"
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
print("E.27.12.50 PATCH APPLICATA")
print("=" * 100)
print("executed: OK")
print("success: OK")
print("order_ticket: OK")
print("deal_ticket: OK")
print("position_ticket: OK")
print("retcode: OK")
print("result: OK")
print()
print("NESSUN ordine inviato durante la patch")
print("NESSUNA apertura")
print("NESSUNA chiusura")
print("=" * 100)

