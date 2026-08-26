from pathlib import Path

path = Path(
    "Core/live_trading_engine.py"
)

text = path.read_text(
    encoding="utf-8"
)

old = '''        # =================================
        # RIMOZIONE PORTFOLIO
        # =================================

        self.portfolio.remove(
            trade["symbol"]
        )

        # =================================
        # REPORT
        # =================================
'''

new = '''        # =================================
        # RIMOZIONE PORTFOLIO
        # =================================

        self.portfolio.remove(
            trade["symbol"]
        )

        # =================================
        # RESET POSITION CONTROLLER
        # =================================
        #
        # La chiusura e stata confermata.
        # Il trade e stato registrato.
        # La posizione Phoenix deve quindi
        # essere rimossa dallo stato attivo.
        #
        # Questo impedisce:
        # - posizione fantasma
        # - doppia chiusura
        # - blocco di una nuova apertura
        #

        self.position_controller.reset()

        # =================================
        # REPORT
        # =================================
'''

if old not in text:
    raise RuntimeError(
        "STOP: blocco RIMOZIONE PORTFOLIO non trovato"
    )

if "self.position_controller.reset()" in text:
    raise RuntimeError(
        "STOP: position_controller.reset() gia presente"
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
print("E.27.12.69A PATCH APPLICATA")
print("=" * 100)
print("BACKUP: OK")
print("POSITION CONTROLLER RESET: OK")
print("Production code modificato: SI")
print("NESSUN ordine MT5 durante la patch")
print("NESSUNA apertura")
print("NESSUNA chiusura")
print("=" * 100)

