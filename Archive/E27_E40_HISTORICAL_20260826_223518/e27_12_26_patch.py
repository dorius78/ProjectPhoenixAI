from pathlib import Path

path = Path("Core/live_trading_engine.py")
text = path.read_text(encoding="utf-8")

old = '''        position = (
            self.position_controller.get_position()
        )

        self.portfolio.add(
            order["symbol"],
            position
        )

        Logger.success(
            "Posizione registrata "
            "nel Portfolio."
        )

        return True
'''

new = '''        position = (
            self.position_controller.get_position()
        )

        if position is None:

            Logger.error(
                "Position Controller: posizione "
                "non disponibile dopo l'apertura."
            )

            return False

        # =================================
        # METADATI MT5
        # =================================

        mt5_result = order.get(
            "mt5",
            {}
        )

        if not isinstance(
            mt5_result,
            dict
        ):
            mt5_result = {}

        position["mt5_ticket"] = int(
            mt5_result.get(
                "position_ticket",
                0
            )
            or 0
        )

        position["mt5_order_ticket"] = int(
            mt5_result.get(
                "order_ticket",
                0
            )
            or 0
        )

        position["mt5_deal_ticket"] = int(
            mt5_result.get(
                "deal_ticket",
                0
            )
            or 0
        )

        position["mt5_symbol"] = str(
            order.get(
                "symbol",
                ""
            )
        )

        # =================================
        # MAGIC
        # =================================

        bridge = getattr(
            self.execution,
            "mt5",
            None
        )

        if bridge is not None:

            position["magic"] = int(
                getattr(
                    bridge,
                    "magic",
                    0
                )
                or 0
            )

        # =================================
        # PORTFOLIO
        # =================================

        self.portfolio.add(
            order["symbol"],
            position
        )

        Logger.success(
            "Posizione registrata "
            "nel Portfolio."
        )

        return True
'''

if old not in text:
    raise RuntimeError(
        "STOP: blocco Portfolio di _open_position_from_order() non trovato"
    )

if '"mt5_order_ticket"' in text:
    raise RuntimeError(
        "STOP: metadati MT5 gia presenti"
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

print("E.27.12.26 PATCH APPLICATA")
print("mt5_ticket: OK")
print("mt5_order_ticket: OK")
print("mt5_deal_ticket: OK")
print("mt5_symbol: OK")
print("magic: OK")
print("Protezione position None: OK")
print("NESSUN order_send")
print("NESSUNA apertura")
print("NESSUNA chiusura")
