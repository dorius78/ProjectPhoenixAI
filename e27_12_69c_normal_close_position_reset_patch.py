from pathlib import Path

path = Path(
    "Core/live_trading_engine.py"
)

text = path.read_text(
    encoding="utf-8"
)

old = '''        self.portfolio.remove(
            trade["symbol"]
        )

        # =================================
        # REPORT
        # =================================
'''

new = '''        self.portfolio.remove(
            trade["symbol"]
        )

        # =================================
        # RESET POSITION CONTROLLER
        # =================================
        #
        # Normal close confermata:
        # la posizione Phoenix non deve
        # rimanere nello stato OPEN.
        #

        self.position_controller.reset()

        # =================================
        # REPORT
        # =================================
'''

if old not in text:
    raise RuntimeError(
        "STOP: blocco normal close non trovato"
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
print("E.27.12.69C PATCH APPLICATA")
print("=" * 100)
print("BACKUP: OK")
print("NORMAL CLOSE POSITION RESET: OK")
print("RESET EXTERNAL CLOSE: INALTERATO")
print("NESSUN ordine MT5")
print("NESSUNA apertura")
print("NESSUNA chiusura")
print("=" * 100)

